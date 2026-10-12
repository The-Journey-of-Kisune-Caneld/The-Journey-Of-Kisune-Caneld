label start:
    scene black
    with dissolve

    narrator "A new journey is about to begin."

    k "Hello! Are you ready?"

    menu:
        "Yes, let's start the adventure!":
            jump prologue_start
        "Give me a moment to prepare.":
            jump prologue_wait

label prologue_start:
    k "Great! Let's take the first step together."
    jump prologue_end

label prologue_wait:
    k "Take your time. We have plenty of time ahead."
    jump prologue_end

label prologue_end:
    narrator "The prologue concludes here for now."
    return
