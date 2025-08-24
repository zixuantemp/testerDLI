#!/usr/bin/env python3
import os,random,subprocess,nbformat as nbf
NB="Main_Model/Main.ipynb"; FAST=os.environ.get("FAST")=="1"
def wait():
  if FAST: return
  import time; t=random.randint(600,1800); print(f"wait {t}s"); time.sleep(t)
def L(): return nbf.read(NB, as_version=4)
def S(nb): nbf.write(nb, NB)
nb=L(); nb.cells+= [nbf.v4.new_markdown_cell("### E1"),
nbf.v4.new_code_cell("""from sklearn.ensemble import StackingClassifier,RandomForestClassifier\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.neural_network import MLPClassifier\n\ndef _stack_bases():\n    return [\n        ('mlp1', MLPClassifier(hidden_layer_sizes=(128,64,32),early_stopping=True,random_state=42,verbose=False)),\n        ('mlp2', MLPClassifier(hidden_layer_sizes=(256,128,64),learning_rate='adaptive',early_stopping=True,random_state=43,verbose=False)),\n        ('mlp3', MLPClassifier(hidden_layer_sizes=(200,100,50),early_stopping=True,random_state=44,verbose=False)),\n        ('rf', RandomForestClassifier(n_estimators=200,random_state=42)),\n        ('lr', LogisticRegression(max_iter=1000,random_state=42)),\n    ]\n\ndef _stack_meta():\n    return LogisticRegression(C=1.0, max_iter=1000, random_state=42)""")]
S(nb); subprocess.check_call(["git","add",NB]); subprocess.check_call(["git","commit","-m","add stacking base models"]); wait()
nb=L(); nb.cells.append(nbf.v4.new_code_cell("""def make_stacking():\n    return StackingClassifier(estimators=_stack_bases(), final_estimator=_stack_meta(), cv=5, stack_method='predict_proba', verbose=0)"""))
S(nb); subprocess.check_call(["git","add",NB]); subprocess.check_call(["git","commit","-m","add stacking factory"]); wait()
nb=L(); nb.cells.append(nbf.v4.new_code_cell("register_model('Stacking Ensemble', make_stacking)"))
S(nb); subprocess.check_call(["git","add",NB]); subprocess.check_call(["git","commit","-m","register stacking"])