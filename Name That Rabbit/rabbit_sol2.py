import operator
import string

let_vals = range(1,27)
letters = string.ascii_lowercase
let_scores = dict(zip(letters, let_vals))

def answer(name_list):
	score_list = []
	for name in name_list:
		name_score = 0
		for let in name:
			name_score += let_scores[let]
		score_list.append([name_score, name])
	score_list.sort(reverse=True)
	ranked = rank_lex(score_list)
	answer = []
	for i in ranked:
		answer.append(i[1])
	print(answer)
	return(answer)

def rank_lex(NameScores):
	name_index = range(len(NameScores)-1)
	for i in name_index:
		if NameScores[i][0] == NameScores[i+1][0]:
			name1 = NameScores[i][1]
			name2 = NameScores[i+1][1]
			new1, new2 = (rank_name(name1,name2))
			NameScores[i][1] = new1
			NameScores[i+1][1] = new2
	return NameScores

def rank_name(name1, name2):
	min_len = range(min(len(name1),len(name2))-1)
	for i in min_len:
		let1 = let_scores[name1[i]]
		let2 = let_scores[name2[i]]
		if let1>let2:
			return(name1,name2)
		elif let2>let1:
			return(name2,name1)
		elif i == min_len:
			if len(name1)>len(name2):
				return(name1,name2)
			else:
				return(name2,name1)

list1 = ["annie", "bonnie", "liz"]
list2 = ["abcdefg", "vi"]
list3 = ["caa", "daa", "cab"]
answer(list3)