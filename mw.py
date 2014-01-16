from os.path import expanduser, exists
from os import devnull
import sys
    
from mywallet.core import Wallet 
from mywallet.prompt import Prompt 

wallet = Wallet()
dotwalletpath = expanduser("~/.mywallet")
prompt = Prompt(wallet, stdout=open(devnull, "w"))

if exists(dotwalletpath):
    dotwallet = open(dotwalletpath)
    for line in dotwallet.readlines():
        prompt.onecmd(line.strip())
        
prompt = Prompt(wallet)
dotwallet = open(dotwalletpath, 'a')

if sys.argv[1:]:
    cmd = " ".join(sys.argv[1:])
    print cmd
    prompt.onecmd(cmd)
    dotwallet.writelines([cmd, '\n'])
prompt.onecmd('amount')