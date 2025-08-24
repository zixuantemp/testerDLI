#!/usr/bin/env python3
import os,random,subprocess,nbformat as nbf
NB="Main_Model/Main.ipynb"; FAST=os.environ.get("FAST")=="1"
def wait():
  if FAST: return
  import time; t=random.randint(600,1800); print(f"wait {t}s"); time.sleep(t)
def L(): return nbf.read(NB, as_version=4)
def S(nb): nbf.write(nb, NB)
nb=L(); nb.cells+= [nbf.v4.new_markdown_cell("### A1"),
nbf.v4.new_code_cell("""ADV_REG_DEFAULT={'hidden_layer_sizes':(256,128,64,32),'alpha':0.01,'learning_rate':'adaptive','learning_rate_init':0.001,'max_iter':1500,'early_stopping':True,'validation_fraction':0.15,'n_iter_no_change':100,'random_state':42,'verbose':False}""")]
S(nb); subprocess.check_call(["git","add",NB]); subprocess.check_call(["git","commit","-m","add adv_reg config"]); wait()
nb=L(); nb.cells.append(nbf.v4.new_code_cell("""from sklearn.neural_network import MLPClassifier\ndef make_adv_reg_mlp(cfg=None):\n    cfg={**ADV_REG_DEFAULT, **(cfg or {})}\n    return MLPClassifier(**cfg)"""))
S(nb); subprocess.check_call(["git","add",NB]); subprocess.check_call(["git","commit","-m","add adv_reg factory"]); wait()
nb=L(); nb.cells.append(nbf.v4.new_code_cell("register_model('Advanced Regularization', make_adv_reg_mlp)"))
S(nb); subprocess.check_call(["git","add",NB]); subprocess.check_call(["git","commit","-m","register adv_reg"])