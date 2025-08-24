#!/usr/bin/env python3
import os,random,subprocess,nbformat as nbf
NB="Main_Model/Main.ipynb"; FAST=os.environ.get("FAST")=="1"
def wait():
  if FAST: return
  import time; t=random.randint(600,1800); print(f"wait {t}s"); time.sleep(t)
def L(): return nbf.read(NB, as_version=4)
def S(nb): nbf.write(nb, NB)
nb=L(); nb.cells+= [nbf.v4.new_markdown_cell("### C1"),
nbf.v4.new_code_cell("""from sklearn.preprocessing import RobustScaler,StandardScaler\ntry:\n    from imblearn.over_sampling import SMOTE\n    _SMOTE_OK=True\nexcept Exception:\n    _SMOTE_OK=False\n\ndef make_robust_scaler(): return RobustScaler()\ndef make_standard_scaler(): return StandardScaler()\ndef make_smote(random_state=42): return SMOTE(random_state=random_state) if _SMOTE_OK else None""")]
S(nb); subprocess.check_call(["git","add",NB]); subprocess.check_call(["git","commit","-m","add preprocessing components"]); wait()
nb=L(); nb.cells.append(nbf.v4.new_code_cell("""def build_preproc_unfitted(use_smote=True):\n    return {'robust_scaler':make_robust_scaler(),'smote': make_smote() if use_smote else None}"""))
S(nb); subprocess.check_call(["git","add",NB]); subprocess.check_call(["git","commit","-m","add preprocessing builder"]); wait()
nb=L(); nb.cells.append(nbf.v4.new_code_cell("""PREPROC_META={'name':'Advanced Preprocessing','order':['robust_scaler','smote']}"""))
S(nb); subprocess.check_call(["git","add",NB]); subprocess.check_call(["git","commit","-m","add preprocessing meta"])