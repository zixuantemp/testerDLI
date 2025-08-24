#!/usr/bin/env python3
import os,random,subprocess,nbformat as nbf
NB="Main_Model/Main.ipynb"; FAST=os.environ.get("FAST")=="1"
def wait():
  if FAST: return
  import time; t=random.randint(600,1800); print(f"wait {t}s"); time.sleep(t)
def L(): return nbf.read(NB, as_version=4)
def S(nb): nbf.write(nb, NB)
nb=L(); nb.cells+= [nbf.v4.new_markdown_cell("### D1"),
nbf.v4.new_code_cell("""from dataclasses import dataclass\nfrom typing import Optional,List\n@dataclass\nclass ThresholdConfig:\n    grid: Optional[List[float]] = None""")]
S(nb); subprocess.check_call(["git","add",NB]); subprocess.check_call(["git","commit","-m","add threshold config"]); wait()
nb=L(); nb.cells.append(nbf.v4.new_code_cell("""def compute_optimal_threshold_stub(*_, **__):\n    return None"""))
S(nb); subprocess.check_call(["git","add",NB]); subprocess.check_call(["git","commit","-m","add threshold function"]); wait()
nb=L(); nb.cells.append(nbf.v4.new_code_cell("""class ThresholdOptimizedModel:\n    def __init__(self, model=None, threshold: float=0.5, scaler=None):\n        self.model=model; self.threshold=threshold; self.scaler=scaler\n    def predict(self, X): raise NotImplementedError('stub')\n    def predict_proba(self, X): raise NotImplementedError('stub')\n\nregister_wrapper('ThresholdOptimizedModel', ThresholdOptimizedModel)"""))
S(nb); subprocess.check_call(["git","add",NB]); subprocess.check_call(["git","commit","-m","add threshold wrapper"])