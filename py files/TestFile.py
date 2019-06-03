class LivingRoom:
    def __init__(self):
        self.sashalivingroomdialogue = False

    def sashadialogue(self):
        if self.sashalivingroomdialogue is False:
            print("You return to the living room once again, Sasha is sitting on the couch watching something on the television. You can talk to her or return to the entrance way to your south.")
        elif self.sashalivingroomdialogue is True:
            print("You see Sasha still, she has nothing new to say.")
        livingroomdirection = input("What will you do? ").lower()
        if livingroomdirection in ['south', 's']:
            entranceway()
        elif livingroomdirection in ['talk', 't', 'sasha', 'couch']:
            self.sashaconversastion()
        else:
            print("Invalid input")
            return self.sashadialogue()

    def sashaconversastion(self):
        player_info.player_location = 'Sasha Living Room'
        print(
            "You walk up to Sasha and sit in the chair beside the couch. The TV is playing a superhero movie involving some sort of pink titan.")
        input()
        print(
            '"Like the movie? It’s called Revengers: Titan Attack. One of the last movies in the Merkel universe. There’s one more that comes after this, but it isn’t out on disc yet"')
        input()
        print(
            '"Do you like superhero movies? I won’t say anymore about it just In-case you want to watch it at some point."')
        input()
        print(
            "You state your preference for superhero movies, saying that you haven’t really kept up with the Revengers movies since the first one")
        input()
        print(
            '"Oh boy, you are in for a treat if you ever decide to catch up on them. Definitely let me know before you do, I’d love to re-watch all of them with you."')
        print('"Anyway, you want anything or just here to chat?"')
        input()
        print(
            "You tell Sasha that you wanted to talk to her about past friends. Your recent walk in the park weighing on your mind, you’re hoping that one of your best friends can give you some advice.")  # Maybe implement a choice later? Don't really have the story options to make this optional yet.
        input()
        print('"Well… I’m gonna be honest, that’s a pretty loaded question."')
        print('"First of all, what happened to these friends? Did they move away? Lose interest in the relationship? Give me some more info."')
        input()
        print(
            "You start to provide some background information to Sasha, explaining the friends’ role in your life, how they affected you, and then eventually how it all broke down ")
        print(
            "You can remember exactly how it started, it was mid-September during your teen years. Your parents had just told you that they couldn’t afford to stay at the lake anymore and that they would be packing up and leaving by the end of the month.")
        input()
        print(
            "This was a huge change. By the end of the month, you’d be moving away from the place of your childhood, the place where you spent almost all your summer days. The place where you met your best-friends.")
        input()
        print(
            "You were gone a week after that. You didn’t have time to mention it to most of your friends since they weren’t even there at the time. In an age without smartphones and social media, those friendships essentially ended that day")
        input()
        print(
            "As you tell Sasha about the move, you remember another ordeal before the move. It involved some of your best-friends Abbey and Jane. The move ended your friendships completely, yes, but you remember that you were on surprisingly shaking terms with both of them months before moving.")
        input()
        print(
            "You started to drift apart. Your interests were changing, and as you got older you found less and less common ground. To the point where Jane said that she ‘barely knew you’. It was actually a similar case with you, you didn’t know what they were interested in anymore. It’s hard to stay friends with someone when you have no idea what to do with them. Regardless, hearing that took you down a notch. Were you ignoring them and not even realizing it? Did they just not feel like you were friends anymore?")
        input()
        print(
            "You never got to ask them why they felt that way, so you can only assume. You feel it was a combination of both parties changing their ideas and interests, as well as Jane and Abbey hanging out with a different friend group. Both parties just slowly lost interest in each other.")
        print(
            "Looking back at it, you feel that the break down of the friendship was inevitable. Even if you hadn’t moved away, it's likely the friendship would have deteriorated further and further. The move simply accelerated things")
        input()
        print(
            "You connected with Abbey and Jane on social media 3 years after moving away, but of course it wasn’t the same. There just wasn’t anything to talk about. Both groups were almost completely different people from the ones 3-4 years ago. Any connections you might have had were gone.")
        input()
        print("You should have let go at that point, but 8 years in the future and you still cling to the past.")
        print(
            "You look to Sasha after rambling on, she seems surprised to hear this from you, considering you’d never mentioned anything about it before.")
        input()
        print(
            '"“That’s quite the story. Can’t say I would have expected something like this from you. You always seemed like the kind of person to live in the present."')
        print('"Then again perhaps I just suck at reading people."')
        input()
        print(
            '"I think most of us have experienced something similar to you. A friendship breaking down for whatever reason"')
        input()
        print(
            '"I think the reason you still look back at that time with such regret is because of the way your relationship broke down. You watched your relationship with Abbey and Jane slowly drift away. With it being the fault of no one. You didn’t have anyone to deflect the blame to for this failing. And apparently, you didn’t even really get to discuss it with them, that lack of closure has no doubt helped lead to your current feelings"')
        input()
        print('"People change, and in the case of Abbey and Jane, there just isn\'t much you can do about it."')
        input()
        print(
            '"I’ve dealt with a somewhat similar situation before. I’m sure you remember me talking about one of my roommates in college dropping out because of depression, well that wasn’t the first time something like that happened."')
        input()
        print(
            '"One of my friends in high school was dealing with some serious shit. Depression, anxiety, and he never told anyone about it. He’d hid it from everyone else, there was no way to know what was going with him. He always cracked jokes, would hang out with you and do whatever, he seemed like one of the most carefree, happy guys I knew."')
        print(
            '"You probably know where this is going by now. He was dealing with serious clinical depression, didn’t want anyone to know because he didn’t want to burden them. He didn’t want people to feel sorry for him."')
        input()
        print(
            '"He ended up committing suicide by overdosing during his junior year of high school. The last guy you would have expected to have that kind of stuff going on "')
        print('"It was extremely difficult dealing with that for the first few months, hell, the first year even. Everybody at the school had trouble dealing with it."')
        input()
        print(
            '"It took me a long time to come to terms with it. And then after that, I still dealt with a mix of guilt and sadness. I felt like I should have picked up on him being depressed. I should have been able to help him in some way. I tried numerous things to try and get past it, stuff as simple as trying new hobbies or traveling, and even went to therapy."')
        input()
        print(
            '"Ultimately, what helped me the most was focusing on the friends that were still there, and on forming new friendships. It helps keep your mind off the past, and helps fill the void that was left. Instead of worrying about what happened in the past, you just try and focus on the now, and how you can make the most of it."')
        input()
        print(
            '"Of course, that’s not always easy to do. Stuff like this never is. And even if you succeed, it doesn’t completely erase the past. You’ll still have moments of weakness, you’ll still think about what could have been"')
        input()
        print(
            '"All you can do is try, and if that fails, ya know, you’ve gotta reach out to people. Family, friends, Somebody. Just letting your thoughts simmer isn’t going to help, it just puts you further down the hole."')
        input()
        print('"There’s no easy way out of these kinds of situations, and odds are, it\'s not going to be the first time you’re going to deal with it"')
        input()
        print(
            'You find yourself resonating with Sasha’s advice and past experiences, though you feel like you’re left with more questions for yourself then before having this conversation. You’re not sure if that’s a good thing or a bad thing.')
        input()
        print('You ask Sasha if she still thinks about those memories very often.')
        input()
        print(
            '"Yes, I still look back at those memories on occasion. Though I’ve found myself looking at the positives of those times rather the negatives. I’m at a point in my life where I feel I’ve moved on from that. I’m happy with how everything has worked out at this point, and that’s in no small part to my friends\' group and support group."')
        input()
        print('You thank Sasha for entertaining your thoughts and helping you out, it helped clear your mind a bit.')
        input()
        print(
            '"Of course! That’s what friends are for. I’ll see you around; oh, and make sure you tell me if you want to catch up on the Revenger’s movies! I’ll be pissed if you don’t!"')
        input()
        print('You say goodbye to Sasha and head up to the room for the night, your mind full of thoughts to process')
        input()
        player_info.player_location = 'Sasha Living Room'
        self.sashalivingroomdialogue = True
        pcbedroom()
