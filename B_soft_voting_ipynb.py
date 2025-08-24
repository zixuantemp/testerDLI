#!/usr/bin/env python3
import os,random,subprocess,nbformat as nbf
NB="Main_Model/Main.ipynb"; FAST=os.environ.get("FAST")=="1"
def wait():
  if FAST: return
  import time; t=random.randint(600,1800); print(f"wait {t}s"); time.sleep(t)
def L(): return nbf.read(NB, as_version=4)
def S(nb): nbf.write(nb, NB)
nb=L(); nb.cells+= [nbf.v4.new_markdown_cell("### B1"),
nbf.v4.new_code_cell("""from sklearn.ensemble import VotingClassifier,RandomForestClassifier\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.neural_network import MLPClassifier\n\ndef _mlp1(): return MLPClassifier(hidden_layer_sizes=(128,64),max_iter=1000,random_state=42,verbose=False)\ndef _mlp2(): return MLPClassifier(hidden_layer_sizes=(200,100,50),learning_rate_init=0.01,alpha=0.01,max_iter=1000,random_state=43,verbose=False)\ndef _mlp3(): return MLPClassifier(hidden_layer_sizes=(100,),max_iter=1000,random_state=44,verbose=False)\ndef _rf():   return RandomForestClassifier(n_estimators=100,random_state=42)\ndef _lr():   return LogisticRegression(max_iter=1000,random_state=42)""")]
S(nb); subprocess.check_call(["git","add",NB]); subprocess.check_call(["git","commit","-m","add voting base estimators"]); wait()
nb=L(); nb.cells.append(nbf.v4.new_code_cell("""def make_soft_voting():\n    return VotingClassifier(estimators=[('mlp1',_mlp1()),('mlp2',_mlp2()),('mlp3',_mlp3()),('rf',_rf()),('lr',_lr())],voting='soft')"""))
S(nb); subprocess.check_call(["git","add",NB]); subprocess.check_call(["git","commit","-m","add voting factory"]); wait()
nb=L(); nb.cells.append(nbf.v4.new_code_cell("register_model('Ensemble', make_soft_voting)"))
S(nb); subprocess.check_call(["git","add",NB]); subprocess.check_call(["git","commit","-m","register voting"])