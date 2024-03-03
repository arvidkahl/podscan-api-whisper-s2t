Local usage: (on a Mac)

KMP_DUPLICATE_LIB_OK=TRUE python main.py --file "./4af5d7c4.mp3" --model tiny --device cpu --compute_type int8 --initial_prompt "Arvid Kahl, The Bootstrapped Founder, Solopreneur" --batch_size 1

Server usage:

python main.py --file "./4af5d7c4.mp3" --model medium