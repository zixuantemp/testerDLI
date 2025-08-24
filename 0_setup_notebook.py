#!/usr/bin/env python3
import os, sys, subprocess
import nbformat as nbf
NB_DIR="Main_Model"; NB_PATH=os.path.join(NB_DIR,"Main.ipynb")
def need_git_identity():
  for k in ["user.name","user.email"]:
    try: subprocess.check_output(["git","config",k])
    except subprocess.CalledProcessError:
      print("set git:\n  git config user.name \"Your Name\"\n  git config user.email you@example.com"); sys.exit(1)
need_git_identity()
os.makedirs(NB_DIR, exist_ok=True); os.makedirs("data", exist_ok=True)
if not os.path.exists(NB_PATH):
  nb=nbf.v4.new_notebook()
  md=lambda t: nbf.v4.new_markdown_cell(t); code=lambda t: nbf.v4.new_code_cell(t)
  nb.cells=[md("# Main Model"),
            code("REGISTERED_MODELS={}\nWRAPPERS={}\nRESULTS_SCHEMA=['Model','Training_Time','Train_Accuracy','Test_Accuracy','Train_F1','Test_F1','Train_Recall','Test_Recall','Train_Precision','Test_Precision']\n\ndef register_model(n,f): REGISTERED_MODELS[n]=f\n\ndef register_wrapper(n,c): WRAPPERS[n]=c\n\ndef log_result_stub(n):\n    return dict(zip(RESULTS_SCHEMA,[n,'0s',0,0,0,0,0,0,0,0]))"),
            md("## Baseline"), md("## Improvement 1 — A"), md("## Improvement 2 — B"),
            md("## Improvement 3 — C"), md("## Improvement 4 — D"), md("## Improvement 5 — E"),
            md("## Ultimate Model")]
  nbf.write(nb, NB_PATH)
  subprocess.check_call(["git","add",NB_PATH])
  subprocess.check_call(["git","commit","-m","create Main.ipynb"])