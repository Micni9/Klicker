
def generate_level_after(jump_list,stage_list):
    level_after = {10:1,25:2}
    for i, jump in enumerate(jump_list):
        if i == 0:
            continue
        level_after[jump] = level_after[jump_list[i-1]] + (jump - jump_list[i-1])//stage_list[i-1]
    return level_after

def Display(title:str,message:str):
    print(f"{title}: {message}")
    
def str2title(title:str):
    n = (50-len(title))//2
    return "*"*n + title.upper() + "*"*n+"\n"