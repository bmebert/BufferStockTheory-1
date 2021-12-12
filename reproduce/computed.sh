#!/bin/bash

scriptDir="$(dirname "$0")"
cd "$scriptDir/.."

echo '' ; echo 'Installing requirements' ; echo ''
#[[ ! -e binder/requirements.out ]] && pip install -r binder/requirements.txt | tee binder/requirements.out 

echo '' ; echo 'Producing figures' ; echo ''

cd "."
ipython BufferStockTheory.ipynb

[[ -e latexdefs.tex ]] && rm -f latexdefs.tex # Delete junk file that might be created

./test_Harmenbergs_method.sh

# Execute sims showing near-constant growth of mean c and cov(c,p), Ω_{M[c]} and Ω_{cov}
if [[ "$#" -gt 0 ]]; then
    if [[ "$1" != "MAX" ]]; then
	if [[ "$1" != "MIN" ]]; then
	    echo ''
	    echo "Only command line options are 'MIN' and 'MAX':"
	    echo ''
	    echo "./reproduce.sh MIN"
	    echo ''
	    echo 'Skips execution of the notebook Code/Python/ApndxBalancedGrowthcNrmAndCov.ipynb'
	    echo ''
	    echo "./reproduce.sh MAX"
	    echo ''
	    echo 'executes it.'
	    echo ''
	    echo 'That script requires large memory capacity, and takes'
	    echo 'many hours to run.  (You might want to do it overnight).'
	    echo ''
	else
	    if [[ "$1" == "MAX" ]]; then
		echo ipython ApndxBalancedGrowthcNrmAndCov.ipynb
	    fi
	fi
    fi
fi
