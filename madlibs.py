def madlibs_office():
    print("Welcome to Mad Libs: Office Drama Edition \n")

   
    name = input("Enter a colleague's name: ")
    job_title = input("Enter a ridiculous job title: ")
    adjective1 = input("Enter an adjective: ")
    noun1 = input("Enter a piece of office equipment: ")
    verb1 = input("Enter a verb ending in -ing: ")
    emotion = input("Enter an emotion: ")
    buzzword = input("Enter a corporate buzzword (e.g., synergy): ")
    insult = input("Enter a mild insult (e.g., buffoon): ")
    drink = input("Enter an after-work drink: ")

 
    story = f"""
    It was a {adjective1} Monday morning when {name}, the office's very own {job_title}, 
    spilled coffee on the communal {noun1} while {verb1}. Naturally, chaos followed.

    With an expression of pure {emotion}, the manager walked in, shouting, 
    "This is not how we embrace {buzzword}!"

    Everyone froze — except {name}, who simply muttered, "Relax, you {insult}..." and 
    casually walked out to get a {drink} at 11 AM.

    And that’s how {name} became a legend in the office Slack channel.
    """

    print("\n--- Your Mad Libs Story ---")
    print(story)


madlibs_office()
