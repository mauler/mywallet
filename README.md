# mywallet

I created this project to test [Cloud9 IDE](http://c9.io/) Cloud9 IDE features and 
also create a full distributed software hosted at [Ubuntu PPA](https://launchpad.net/ubuntu/+ppas/)

The idea is a simple wallet with transactions schedulings and repetitions that 
works without using a pré-defined syntax but writing what you want, like:
    
    $ mw deposit 500 monthly at day 5
   
    
or:

    $ mw deposit monthly at day 5 500


## notes

 * The code is not pep8 validated because I didn't find any helper on editor (Cloud9) to do this (yet).

 
## usage

Define a deposit every day 5 monthly as My salary:
    
    $ mw deposit 1000 monthly at day 5 My salary
    

Define a withdraw every month (day 1):
    
    $ mw withdraw 100 monthly
    

Return balance in the next 5 months:
    
    $ mw balance 5 months
