def next_stage(amount_now,multi_stage,multi_jump)->int:
    stage = -1
    for i,jump in enumerate(multi_jump):
        if amount_now>=multi_jump:
            stage = i
    if stage == -1:# amount_now < 25
        return 10 if amount_now<10 else 25
    # amount_now >= 25
    return multi_stage - ((amount_now - multi_jump[stage])%multi_stage)