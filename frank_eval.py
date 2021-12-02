from questeval.questeval_metric import QuestEval
import json

path = '/projects/tir5/users/apagnoni/frank/data/benchmark_data.json'
out_path = '/projects/tir5/users/apagnoni/frank/data/baseline_factuality_metrics_outputs.json'
out_2_path = '/projects/tir5/users/apagnoni/frank/data/baseline_metrics_outputs.json'

with open(path) as infile:
    frank = json.loads(infile.read().strip())

with open(out_path) as infile:
    baselines = json.loads(infile.read().strip())

questeval = QuestEval()
for example in frank:
    hypothesis = example['summary']
    source = example['article']
    score = questeval.compute_all(hypothesis, source)
    score = score['scores']
    for i, elt in enumerate(baselines):
        if elt['hash'] == example['hash']:
            elt['QuestEval_P'] = score['precision']
            elt['QuestEval_R'] = score['recall']
            elt['QuestEval_F'] = score['fscore']
            print(baselines[i])
            break
    break
# with open(out_2_path, 'w') as outfile:
#     json.dump(baselines, outfile, indent=4)

