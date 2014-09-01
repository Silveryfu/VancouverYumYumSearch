cd ~/Yumcouver.com
python ServerForQuery.py 2>error/query.error 1>log/query.log &
python ServerForSelfCorrection.py 2>error/self_correction.error 1>log/self_correction.log &
