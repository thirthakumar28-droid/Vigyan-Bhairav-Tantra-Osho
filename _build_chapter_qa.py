"""
Build _chapter_qa.json from one paraphrased Q&A entry per even-numbered
chapter of Osho's The Book of Secrets (chapters 4, 6, ..., 80).

In the book, the even-numbered chapters are Q&A sessions in which Osho
answers questions arising from the techniques given in the immediately
preceding odd chapter. The most piercing of those questions are often
the very questions a modern reader would put to the same techniques,
and so we surface one per even chapter as an expandable callout at the
end of the corresponding odd-chapter section in the merged book.

Schema (per entry):
  - chapter:             int (even, 4..80) — the Q&A session number
  - follows_chapter:     int (odd, chapter-1) — the chapter being asked about
  - title_hint:          str — title of the even chapter (for context only)
  - question_paraphrase: str — the questioner's question, paraphrased into
                               1-2 modern sentences
  - answer_paragraphs:   list[str] — 2-3 paragraphs of paraphrased answer,
                               in the file author's own English prose,
                               tracking Osho's argument faithfully
  - answer_quotes:       list[str] — 1-2 short attributed direct quotes
                               (each under 35 words) drawn from Osho's
                               actual answer
"""

import json
from pathlib import Path

QA = [
    # ─────────────────────────────────────────────────────────────────
    # Chapter 4 — Overcoming the Deceptions of the Mind (1 question)
    # ─────────────────────────────────────────────────────────────────
    {
        "chapter": 4,
        "follows_chapter": 3,
        "title_hint": "Overcoming the Deceptions of the Mind",
        "question_paraphrase": (
            "How can a method as simple as noticing the gap between two breaths "
            "be enough to bring enlightenment? It seems impossible that such a "
            "small act could close so vast a distance."
        ),
        "answer_paragraphs": [
            "Osho says the question rests on a hidden assumption that needs to be removed before any of these techniques will make sense: the assumption that spirituality is an attainment, something you do not yet have and must labour to acquire. If that were true, then of course no method, however refined, could be enough - and equally, no amount of effort either, because effort by someone who is not already divine cannot create divinity out of nothing. The very framing of the spiritual life as a long climb to a far peak is the deepest deception of the mind.",
            "His counter-claim is that you are already what you are reaching for. The treasure is not somewhere else; it is hidden inside the house, and you are begging in the streets only because you have not yet bothered to look. From this angle, the size of the technique becomes irrelevant: a small act of digging is enough because there is so little earth between you and the treasure. The distance between Gautam Siddhartha and Gautam Buddha was infinite, yet it was crossed in a single moment of recognition - not by gradual accumulation.",
            "So a small technique works the way a small operation works on a blind eye: nothing is added, nothing is built. The seer was always there behind the closed eyes, and the moment the windows are opened, sight becomes immediate. Awareness of the gap between two breaths is just such an opening - so simple it is easy to dismiss, and so precise that, taken seriously, it is enough.",
        ],
        "answer_quotes": [
            "It is not an attainment, but a discovery.",
            "You have not yet recognized it, but it is there already in you. You are the treasure, but you go on begging.",
        ],
    },

    # ─────────────────────────────────────────────────────────────────
    # Chapter 6 — Devices to Transcend Dreaming (2 questions)
    # ─────────────────────────────────────────────────────────────────
    {
        "chapter": 6,
        "follows_chapter": 5,
        "title_hint": "Devices to Transcend Dreaming",
        "question_paraphrase": (
            "What are the other factors that can make one conscious while "
            "dreaming, beyond the techniques you have already given?"
        ),
        "answer_paragraphs": [
            "Osho begins by widening the question. Dreaming is not something that happens only at night; it continues all day, suppressed by activity the way the stars are suppressed by sunlight. Close your eyes in the middle of the afternoon and the dreaming is already there, instantly available - the daytime mind only covers it. Until that constant inner film stops, you cannot honestly call yourself awake; you are only somewhat less asleep in the day than you are at night.",
            "This, he says, is what every spiritual tradition means when it calls man asleep. Buddha is named the awakened one not because he opens his eyes more often than the rest of us, but because the inner dreaming has ceased completely. Until that ceases, the dreamer is lost in the dream the way a viewer becomes lost in a film and forgets, for three hours, that there even is a viewer. The film of life is much longer, but the structure is identical: total absorption in what is on the screen, total forgetting of who is watching.",
            "Becoming conscious in a dream, then, is a doorway. Practically, Osho recommends watching the breath as you fall asleep, watching whatever images arise without interfering, and treating each remembered dream as an object rather than as a place you fall into. The aim is not control of the dream content but recognition that you are not the content. As that recognition deepens, the same loosening transfers to waking life, and the day-long film begins to thin.",
        ],
        "answer_quotes": [
            "Dreaming creates a film over the consciousness.",
            "The dreamer is lost in the dreaming. You see everything except yourself; you feel everything except yourself; you know everything except yourself.",
        ],
    },

    # ─────────────────────────────────────────────────────────────────
    # Chapter 8 — Total Acceptance and Non-Division (1 question)
    # ─────────────────────────────────────────────────────────────────
    {
        "chapter": 8,
        "follows_chapter": 7,
        "title_hint": "Total Acceptance and Non-Division: The Meaning of Tantric Purity",
        "question_paraphrase": (
            "What does Tantra mean by purity? Is it different from the moral "
            "purity that other traditions speak of?"
        ),
        "answer_paragraphs": [
            "Osho says ordinary religious language equates purity with goodness: certain qualities are 'good' and certain qualities are 'bad,' and being pure means having more of one and less of the other. Every tradition draws the line in a slightly different place - Christians here, Jains there, Gurdjieff in his own way - but they all draw a line, and they all measure purity against it. For Tantra, this is not purity at all. It is moralism, and the moralist is a divided person whose whole life is spent on one side of an inner war.",
            "Tantra's purity is something else: undifferentiated innocence. A child gets angry, but the anger does not leave a residue, because there is no inner judge measuring the anger against an ideal. The act is total, complete, and gone. That total presence-without-division is what Tantra calls pure. The sage's purity is the same purity, but achieved on the far side of knowledge rather than on the near side - innocence regained rather than innocence not yet lost.",
            "The Adam and Eve story carries this exactly, Osho says. They were expelled from the garden by eating from the tree of knowledge, and the kingdom can be re-entered only by becoming like a child again - not by becoming more moral, but by becoming undivided. Tantra, properly understood, is the path of that second innocence: not below morality, but past it.",
        ],
        "answer_quotes": [
            "To divide is impure and to live in non-division is purity.",
            "A child is pure because there is no mind. The more mind grows, the more the child will become impure.",
        ],
    },

    # ─────────────────────────────────────────────────────────────────
    # Chapter 10 — Self Actualization: The Basic Need (5 questions)
    # ─────────────────────────────────────────────────────────────────
    {
        "chapter": 10,
        "follows_chapter": 9,
        "title_hint": "Self Actualization: The Basic Need",
        "question_paraphrase": (
            "Is self-actualization a basic need? Why does the felt sense of "
            "missing something never go away even when the visible needs of "
            "life have all been met?"
        ),
        "answer_paragraphs": [
            "Osho borrows Maslow's term and presses it past its psychological meaning. Man is born as a seed, not as an actuality - the destiny is potential rather than complete - and so a particular kind of restlessness is built into being human. You may achieve every external thing the world offers and still feel that something is missing, because what is missing is not external. The seed has not yet become the tree it was meant to become.",
            "This explains, he says, why even the most outwardly successful person can come into a quiet room and discover that he is unhappy without knowing why. Riches, position, prestige, power - none of these touch the inner growth. They can mask the felt absence with motion, but they cannot end it, because they are answers to a different question. The question being asked from inside is not 'what do I have?' but 'have I become what I was?'.",
            "When self-actualization happens, the felt absence ceases - and Osho ties this to Maslow's 'peak experience.' A self-actualised person experiences ordinary moments as peaks because the inner restlessness has stopped manufacturing comparisons. Buddha sat under a tree as a beggar and was already an emperor; the throne was internal. That is why this need is the basic need: it organises every other need, and no other can satisfy in its place.",
        ],
        "answer_quotes": [
            "Self-actualization becomes a peak experience, and only a self-actualized person can attain peak experiences.",
            "Buddha was a beggar, but yet an emperor.",
        ],
    },

    # ─────────────────────────────────────────────────────────────────
    # Chapter 12 — On the Roots of Centering (4 questions)
    # ─────────────────────────────────────────────────────────────────
    {
        "chapter": 12,
        "follows_chapter": 11,
        "title_hint": "On the Roots of Centering",
        "question_paraphrase": (
            "Tantra and Yoga speak of many different centres - the navel, the "
            "heart, the third eye, the spine, the sex centre. Which one is the "
            "real centre, and which should I work with?"
        ),
        "answer_paragraphs": [
            "Osho's answer dissolves the question. The centre you work with is not what matters - the act of centering is. Buddhists count nine chakras, Hindus seven, Tibetans thirteen; Tantra uses the sex centre, Taoists sometimes use the big toe. None of these schemes is wrong, because the moment you are gathered totally at any one point, you fall automatically to the navel - the existential root - regardless of where you began. The functional centre may be anywhere; the existential centre takes care of itself.",
            "He is unusually practical here. Choose whatever centre your nature most naturally flows toward. If you are sexually charged, do not fight the energy; let the sex centre be your centring point and the energy itself will change quality once awareness settles in it. If you live in your head, you can use even doubt as a centring force, provided the doubt becomes total enough to turn on itself. The shape of the centre matters far less than the totality with which you arrive at it.",
            "The reason this works, Osho says, is that centring is the catalyst, not the destination. Once you are gathered at any point, the energy crystallises into a kind of spiritual atom - and then it explodes. After that explosion there is no centre at all, or, equivalently, the centre is everywhere. What looks like a method of one-pointedness is in fact the precise device by which one-pointedness dissolves itself.",
        ],
        "answer_quotes": [
            "The thing happens because of centering, not because of the center.",
            "The center is not significant, centering is significant.",
        ],
    },

    # ─────────────────────────────────────────────────────────────────
    # Chapter 14 — Changing the Direction of Energy (3 questions)
    # ─────────────────────────────────────────────────────────────────
    {
        "chapter": 14,
        "follows_chapter": 13,
        "title_hint": "Changing the Direction of Energy",
        "question_paraphrase": (
            "If samadhi is total, all-pervading consciousness, why is the path "
            "to it called centering, when centering implies one-pointedness? "
            "The two seem contradictory."
        ),
        "answer_paragraphs": [
            "Osho draws a clean line. Centring is the path, not the goal. Samadhi itself is not centring; centring is only the technique by which samadhi can occur. The two appear contradictory because the path and the result use different logics: the path narrows you to a point, the result broadens you to everywhere. Jacob Boehme captured the same paradox in another idiom, saying that when one comes to the divine you can describe it equally as 'the centre is everywhere' or 'the centre is nowhere.' Both are accurate, because the point has exploded.",
            "Why centring works, then: scattered energy cannot detonate. When you are spread thin across a thousand interests, fears and identifications, there is no concentration of force at any one location, and so the explosion that ends seeking can never gather. Centring is the procedure by which scattered energy is brought to a single atomic point, and at that density the explosion becomes inevitable. After it, the energy returns - but no longer through any particular centre. The centre has become the field.",
            "This, Osho says, is also why religion talks endlessly about method and refuses to talk about result. Method is impersonal, scientific, and transmissible: do this, that follows. The result is personal, poetic, and untransmissible: every realised being expresses it differently because every being arrives at it through their own life. Buddha says one thing, Krishna another, Lao Tzu a third - not because they disagree, but because the result, unlike the method, cannot be standardised.",
        ],
        "answer_quotes": [
            "Centering is just to gather yourself totally at one point. Once you are gathered at one point, crystallized at one point, that point explodes automatically.",
            "Method is scientific; centering is scientific; but when the explosion comes to you, it is poetic.",
        ],
    },

    # ─────────────────────────────────────────────────────────────────
    # Chapter 16 — Beyond the Sin of Unconsciousness (4 questions)
    # ─────────────────────────────────────────────────────────────────
    {
        "chapter": 16,
        "follows_chapter": 15,
        "title_hint": "Beyond the Sin of Unconsciousness",
        "question_paraphrase": (
            "When we try the technique of refusing to project a mood onto the "
            "person it arose against, it feels like suppression. The anger "
            "becomes a complex inside. How do we use this technique without "
            "creating that suppression?"
        ),
        "answer_paragraphs": [
            "Osho's first move is to dismantle the dichotomy in the question. Expression and suppression are two sides of the same coin: in both, the other person is at the centre of the operation. Whether you throw your anger at someone or push it down inside yourself to spare them, you are still organising the energy around them rather than around yourself. The technique he gave is neither - it is a third option that the ordinary mind has never considered.",
            "The third option is to stop doing anything with the anger and use it as a path. The energy has come to the surface; instead of expressing or suppressing it, walk back along it to the source from which it arose. The point is not to become a better-behaved person but to find the place inside you that produces anger in the first place. Once you are centred there, anger has no force, because it is no longer the unexamined emergency it was when you only met it at the surface.",
            "Suppression fails, Osho stresses, because the energy will leak out somewhere - on the children, on the servant, on a stranger in traffic, on a smaller and weaker target than the one you were originally angry with. You can only postpone, never abolish, an energy you have refused to trace. Tracing it backwards through your own being, on the other hand, releases the energy at its source rather than displacing it onto someone else's life.",
        ],
        "answer_quotes": [
            "Expression and suppression are two aspects of one coin.",
            "Do not do anything with anger. Just go deep down into it to know from where this has arisen.",
        ],
    },

    # ─────────────────────────────────────────────────────────────────
    # Chapter 18 — Remaining with the Facts (4 questions)
    # ─────────────────────────────────────────────────────────────────
    {
        "chapter": 18,
        "follows_chapter": 17,
        "title_hint": "Remaining with the Facts",
        "question_paraphrase": (
            "Western youth are now expressing anger and sex more openly than "
            "Indian youth do. Is this permissiveness a movement toward becoming "
            "more authentic in emotional expression?"
        ),
        "answer_paragraphs": [
            "Osho refuses the easy yes. To be authentic is to be totally factual - to live without the layers of cultivated face that society installs in childhood. But Western permissiveness is not authenticity; it is the swing of a pendulum away from previous repression, and a pendulum is still controlled by the wall it is swinging against. Acting out is not the same as being real, and the act of breaking a rule is just as conditioned as the act of obeying it.",
            "He sketches the developmental trap. A child left to itself would be authentic, but only as an animal - real, but never reaching the human possibility. Society therefore must do something to it, and whatever society does will distort the original self. The child becomes a man but a divided man, with the animal alive inside and the cultivated person performing outside. Western permissiveness does not resolve this division; it lets the animal speak more loudly. The split is unchanged.",
            "The third possibility, the one Tantra opens, is unconditioning. Not regression to the animal, not double life under the social face, but a deliberate undoing of the conditioning that has been imposed - resulting in a being who is real but no longer animal, more than a man rather than less. The techniques are designed for that third movement. Permissiveness, by contrast, only swings between the first two and never finds the door to the third.",
        ],
        "answer_quotes": [
            "The more you are cultivated, the less real you are.",
            "All techniques of meditation are really 'unconditionings.' Whatsoever society has given to you can be taken away again.",
        ],
    },

    # ─────────────────────────────────────────────────────────────────
    # Chapter 20 — Ordinary Love and the Love of a Buddha (3 questions)
    # ─────────────────────────────────────────────────────────────────
    {
        "chapter": 20,
        "follows_chapter": 19,
        "title_hint": "Ordinary Love and the Love of a Buddha",
        "question_paraphrase": (
            "It feels impossible to love someone for twenty-four hours a day. "
            "Should love be a continuous process, and at what point does love "
            "become devotion?"
        ),
        "answer_paragraphs": [
            "Osho identifies the hidden mistake in the question. Love is being treated as an act - something you do - and any act, no matter how skilled, exhausts the actor. If love is a doing, it must alternate with rest, and the rest can only happen in the opposite direction: hate. That is exactly why ordinary love and ordinary hate orbit the same person, and why the lover is bewildered to find both feelings pointed at the same face. The doing has gotten tired, so the doing has flipped.",
            "Real love, in his vocabulary, is a state of being rather than an act. It does not need to be sustained by effort, any more than breathing needs to be sustained by effort while you walk down the street. When a person is in this state, the love is not aimed at anyone in particular - it is the climate in which they meet whatever person is in front of them. Focused on a single person, this state is what we call love. Unfocused, it is what we call prayer. Devotion is the same energy without an addressee.",
            "Osho gives Jesus's famously difficult command - love your enemy - as the test of this distinction. As an act, loving an enemy is a contradiction; as a state, it is unremarkable. You do not stop breathing because the air around you happens to belong to someone you dislike. If love is breathing of the soul, it is not directed; it is the medium in which everyone, friend or enemy, is met.",
        ],
        "answer_quotes": [
            "Love is just like breathing: it is a higher plane of breathing.",
            "If you are not in love, your spirit cannot be born.",
        ],
    },

    # ─────────────────────────────────────────────────────────────────
    # Chapter 22 — Unblocking the Third Eye (3 questions)
    # ─────────────────────────────────────────────────────────────────
    {
        "chapter": 22,
        "follows_chapter": 21,
        "title_hint": "Unblocking the Third Eye",
        "question_paraphrase": (
            "What is the relationship between the two ordinary eyes and the "
            "third eye? How do the looking techniques actually affect the "
            "third eye?"
        ),
        "answer_paragraphs": [
            "Osho clarifies a point most readers get wrong about the third eye. There is no separate energy that runs it - the very same energy that moves through your two ordinary eyes is what would move through the third. The third eye is already there, complete, but non-functioning, because all the available seeing-energy is currently being drawn out through the two physical eyes. When that flow is interrupted, the energy is automatically diverted, and the third begins to function. The two will go on existing afterwards, but they will become structurally unseeing while the third sees.",
            "He then makes the more delicate point that the third eye is not actually part of the physical body at all. It belongs to the sukshma sharir, the subtle body, and has only a corresponding location in the physical skull. This is why physiology cannot find it: there is no organ to dissect, no nerve cluster to map. Looking techniques work because they manipulate the energy flow rather than any physical organ - close the physical sight long enough, totally enough, and the energy goes where it is structurally meant to go.",
            "From this, the practical advice follows. The looking sutras are not about strength of gaze or duration of stare; they are about completeness of attention. Once attention is total, the energy automatically pools, the physical channel saturates, and the spillover finds the dormant point between the brows. What is invisible to the physical eyes - which can only register the physical - becomes immediately accessible to the third, which sees in a different dimension altogether.",
        ],
        "answer_quotes": [
            "The third eye is already there, but non-functioning, and it cannot see unless these ordinary eyes become unseeing.",
            "The two eyes are physical. Through these eyes you cannot see anything which is not physical.",
        ],
    },

    # ─────────────────────────────────────────────────────────────────
    # Chapter 24 — Doubt or Faith, Life or Death (3 questions)
    # ─────────────────────────────────────────────────────────────────
    {
        "chapter": 24,
        "follows_chapter": 23,
        "title_hint": "Doubt or Faith, Life or Death: The Bases of Different Paths",
        "question_paraphrase": (
            "I do not feel I am clearly the intellectual or the feeling type - "
            "I seem to be a mix. Should I alternate between two kinds of "
            "techniques?"
        ),
        "answer_paragraphs": [
            "Osho's reply is sharp and surprisingly diagnostic. The very fact that you experience yourself as confused about which type you are tells him you are the intellectual type. The feeling type is never confused; emotion is structurally whole and undivided, while intellect is structurally fragmented and self-doubting. Doubt cannot ever be total - it doubts even itself, layering uncertainty over uncertainty - whereas trust, when it lands, lands as one piece.",
            "The implication is liberating once you accept it. If you have been alternating between methods because you 'might be either,' you have been wasting energy on a false dilemma. Choose the techniques designed for the intellectual type and commit to them. A Ramakrishna cannot be made to doubt because doubt is not what he is built out of; equally, you cannot be made to feel uncomplicated trust on demand, because that is not how your wiring works. Your basic type cannot be changed.",
            "What can change is the relationship to the type. The intellectual works by pushing doubt to its absolute limit until even doubt itself collapses, and the collapse is what opens the centre. The feeling type works by surrendering, by letting trust become so total that the seeker dissolves into what is being trusted. Different paths, but the same ending. The mistake is not having a type; the mistake is using the type wrongly.",
        ],
        "answer_quotes": [
            "Whenever you feel that you are neither the intellectual type nor the emotional type, know well that you belong to the intellectual type, because confusion is part of it.",
            "You cannot doubt a thing totally. If you doubt a thing totally, it becomes faith.",
        ],
    },

    # ─────────────────────────────────────────────────────────────────
    # Chapter 26 — Acceptance of the Peaks and the Valleys (2 questions)
    # ─────────────────────────────────────────────────────────────────
    {
        "chapter": 26,
        "follows_chapter": 25,
        "title_hint": "Acceptance of the Peaks and the Valleys",
        "question_paraphrase": (
            "If the unconscious instincts come from our animal heritage, isn't "
            "it actually good to channel and regulate them through the "
            "intelligence of the conscious mind, instead of accepting them?"
        ),
        "answer_paragraphs": [
            "Osho rejects the framing. Man is an animal, but he is also more, and the 'more' cannot proceed by denying the animal - it has to absorb it creatively. Once you treat your animal heritage as something to be regulated, controlled or condemned, you have started a war you cannot win, because the conscious mind is roughly one percent of you and the animal is ninety-nine. The flower cannot defeat the roots that are feeding it. Every effort in that direction is a losing battle and produces frustration that is mistaken for moral failure.",
            "The split itself, he says, is hell - and hell is not a geography but a psychology. A divided personality cannot be blissful no matter what it achieves; an undivided personality, however ordinary, is in heaven. The animal in you is not bad; it is the soil from which the future grows, and treating it as enemy means treating your own ground as enemy. The intelligence of the conscious mind is real, but its task is not to defeat the animal - its task is to inform and integrate it.",
            "The technique, then, is not regulation but absorption. Watch the instinct, follow it back to its source, recognise that it is part of the same energy that runs every higher capacity, and stop fighting. What looked like a beast to be tamed turns out to be a potential to be matured. Sex becomes love, anger becomes clarity, fear becomes alertness - but only if the war between conscious and unconscious is set down. Where the war continues, the energy is wasted on the war.",
        ],
        "answer_quotes": [
            "If you are divided against yourself, you can never attain anything which is blissful.",
            "Hell is not something geographical, hell is psychological - and heaven also.",
        ],
    },

    # ─────────────────────────────────────────────────────────────────
    # Chapter 28 — Meditation: An Unburdening of Repressions (3 questions)
    # ─────────────────────────────────────────────────────────────────
    {
        "chapter": 28,
        "follows_chapter": 27,
        "title_hint": "Meditation: An Unburdening of Repressions",
        "question_paraphrase": (
            "Repression has become so automatic that we don't even notice it. "
            "How can we tell the difference between a false image of ourselves "
            "and the real one?"
        ),
        "answer_paragraphs": [
            "Osho gives an unsettling reply: every face you currently have is false. There is no real face among them to be sorted out from the rest by careful comparison. The real face is what Zen calls the original face - the face you had before your birth and the face you will have after your death - and it is not visible from inside the gallery of social masks you presently inhabit. The question 'which one is real?' assumes a real one is in there somewhere, and it is not.",
            "The falseness, he says, begins early. The newborn quickly discovers that smiling is a bribery, that some behaviours are accepted and others punished, and from then on the child is a small politician adjusting expressions to optimise the supply of love. Every face that emerges from this process is utilitarian, not true. The faces are useful, which is exactly why they were adopted, but utility is not authenticity. Some faces produce more reward than others, but none of them is real.",
            "The deeper trap, Osho warns, is what happens when you finally see the falseness. The mind reacts: it manufactures a new face to replace the discovered fakes, often a 'spiritual' or 'renunciate' face that feels truer because it was chosen instead of imposed. But a face produced as a reaction to other faces is just one more face. The real cannot be produced by reaction. It can only be uncovered by dropping all of them - including the one you are tempted to put on tomorrow morning to look real.",
        ],
        "answer_quotes": [
            "All your faces are false; you do not have any real face.",
            "By reacting to a false face you will create another false face.",
        ],
    },

    # ─────────────────────────────────────────────────────────────────
    # Chapter 30 — Surrendering in Sex and Surrendering to a Master (2 questions)
    # ─────────────────────────────────────────────────────────────────
    {
        "chapter": 30,
        "follows_chapter": 29,
        "title_hint": "Surrendering in Sex and Surrendering to a Master",
        "question_paraphrase": (
            "You have said Tantra is total acceptance, and also that Tantra is "
            "the middle path between extremes. In sexual life, how does one "
            "tell the difference between indulgence and repression?"
        ),
        "answer_paragraphs": [
            "Osho's first move is to redraw the geometry. Indulgence and repression are not opposites with the middle path between them; both are extremes, and both arise from the same basic move - choosing. The moment you choose against an aspect of life, you have already left the middle, and which extreme you end up at is just a question of which choice you happened to make. Denial of sex moves you to celibacy; denial of celibacy moves you to indulgence. The structure is identical; only the destination differs.",
            "Acceptance of totality, by contrast, is not a third position you reach by choosing. It is what is left when choosing stops. You are no longer for or against any particular configuration of life; you are floating in the stream rather than steering against it. Tantra calls this a let-go, and it is recognisable by the absence of the inner divide that both indulgence and repression require. Where there is no divide, there is no extreme to fall into.",
            "The practical sign Osho gives is precise. Once choosing stops, the ego stops manufacturing problems out of every situation, because the ego is the chooser. Existence in itself has no problems; the chooser brings problems with him wherever he goes. So the test of whether your sexual life is in the middle is not how much you have or refuse - it is whether the chooser is operating. If choice has dissolved, whatever is happening is in the middle by definition. If choice is still operating, no amount of measuring frequency will move you out of the extremes.",
        ],
        "answer_quotes": [
            "When you choose, you are moving against the whole universe - you have your own choice.",
            "There are no problems in life itself. Existence is problem-less. You are the problem.",
        ],
    },

    # ─────────────────────────────────────────────────────────────────
    # Chapter 32 — "No Fight" Is the Central Teaching (3 questions)
    # ─────────────────────────────────────────────────────────────────
    {
        "chapter": 32,
        "follows_chapter": 31,
        "title_hint": "No Fight Is the Central Teaching",
        "question_paraphrase": (
            "Many of the techniques you have given so far seem to belong to "
            "yoga rather than to Tantra. What is Tantra's actual central "
            "subject matter, and how is it different from yoga?"
        ),
        "answer_paragraphs": [
            "Osho explains that the techniques themselves overlap - the same methods can appear in both yoga and Tantra - but the philosophy framing them is opposite. Yoga is the path of will: it diagnoses your suffering as a defect of will and prescribes its perfection. Tantra is the path of total surrender: it diagnoses your suffering as caused by the very existence of will and prescribes its dissolution. Both diagnoses are coherent; both, Osho says, are right within their own frame. But they are not compatible.",
            "The two paths therefore feel different from inside even when the technique looks the same on paper. A yogic practitioner doing breath awareness is sharpening the will against scattered attention; a tantric practitioner doing breath awareness is letting the will drop and noticing what continues without it. The outer act looks identical and the inner orientation is opposite. This is why the same hundred-and-twelve sutras can serve both schools, and why Tantra can claim them without contradiction.",
            "Osho is also candid about why yoga is more popular. Tantra is easier - it is natural, effortless, surrender-based - and precisely for that reason the ego cannot find a project in it. Yoga offers the ego a long, arduous path with milestones; Tantra offers nothing for the ego to do. Most people therefore feel drawn to yoga, work at it for lifetimes, and only at some late point turn to Tantra when the will-project finally exhausts itself. The exhaustion of will is the real beginning of Tantra.",
        ],
        "answer_quotes": [
            "Yoga believes in struggle; Yoga is basically the path of will. Tantra is the path of total surrender.",
            "Tantra is easy, natural, and you can attain through Tantra very easily, very naturally, effortlessly. And because of this, Tantra never appeals to you as much.",
        ],
    },

    # ─────────────────────────────────────────────────────────────────
    # Chapter 34 — Cosmic Orgasm through Tantra (4 questions)
    # ─────────────────────────────────────────────────────────────────
    {
        "chapter": 34,
        "follows_chapter": 33,
        "title_hint": "Cosmic Orgasm through Tantra",
        "question_paraphrase": (
            "When you tell us to enjoy the love act totally, to be the shaking "
            "as it shakes us - is that not just teaching indulgence?"
        ),
        "answer_paragraphs": [
            "Osho rejects the question's vocabulary as the voice of an unreal personality - the cultivated face that society has been training us to wear since childhood. That cultivated face is structurally against enjoyment. It always favours sacrifice, always frames pleasure as selfishness, and always experiences the moment of well-being as a moral failure. The word 'indulgence' is one of the tools that personality uses to ensure you do not actually enjoy your own life.",
            "Tantra's claim is the inverse: until you can enjoy yourself, you are dangerous to others. People who sacrifice themselves for others almost always become sadists, because the sacrifice is unconsciously billed back to the recipients - the mother who gave up her life for her children, the husband who gave up his interests for his wife. The sacrificer tortures by the very act of having sacrificed. Genuine altruism is a by-product of overflowing personal happiness, not a substitute for it.",
            "So when Osho tells the practitioner to be totally in the act of love and to be the shaking as it shakes through, he is not endorsing more pleasure for its own sake; he is removing the shame that prevents pleasure from completing itself. A pleasure that is welcomed completely passes through and leaves stillness; a pleasure that is met half with desire and half with self-judgement gets stuck and demands repetition. Sacrifice, duty, service - these are the words of a personality that has not yet learned to be happy with itself.",
        ],
        "answer_quotes": [
            "Unless you can enjoy yourself you cannot help anyone to enjoy.",
            "Be selfish; only then can you be altruistic. Otherwise the whole concept of altruism is nonsense.",
        ],
    },

    # ─────────────────────────────────────────────────────────────────
    # Chapter 36 — From Illusion to Reality (3 questions)
    # ─────────────────────────────────────────────────────────────────
    {
        "chapter": 36,
        "follows_chapter": 35,
        "title_hint": "From Illusion to Reality",
        "question_paraphrase": (
            "How does the practice of self-remembering actually transform the "
            "human mind? What is it doing inside?"
        ),
        "answer_paragraphs": [
            "Osho begins from the disease that self-remembering is the medicine for. Every child is born centred in itself, but society - the family, the school, the culture - cannot allow that natural state to continue, because a fully self-centred child cannot be governed. So a second centre is constructed: a social, conscious, responsive identity that knows what to do to receive love and what to avoid in order to escape punishment. The original centre is pushed into the dark, and the manufactured centre takes its place as 'me.'",
            "The split between conscious and unconscious that psychology describes is, in his view, exactly this displacement. There is no real division in consciousness; the division is created by the act of installing a substitute centre. Eventually you become so unconscious of your real centre that you do not know it exists, and your whole life is lived from the manufactured one. This is the 'disease' meditation is medicine for. If a society could be built on freedom rather than on cultivation, no medicine would be needed.",
            "Self-remembering, then, is the patient act of bringing the real centre back into consciousness. Whenever you do something - eat, walk, listen, react - you remember that you are the one doing it, not by adding a thought but by including yourself in your own perception. Slowly, the manufactured centre loses its monopoly on the inner life and the real centre re-emerges. The transformation is not the construction of a new self; it is the recovery of the self that has been there all along, displaced by the clever child's politics.",
        ],
        "answer_quotes": [
            "The society creates the disease, and then the disease has to be treated.",
            "Your natural center has moved into the unconscious, into the dark, and your unnatural center has become your conscious.",
        ],
    },

    # ─────────────────────────────────────────────────────────────────
    # Chapter 38 — Toward the Authentic Being (4 questions)
    # ─────────────────────────────────────────────────────────────────
    {
        "chapter": 38,
        "follows_chapter": 37,
        "title_hint": "Toward the Authentic Being",
        "question_paraphrase": (
            "How does the original mind become identified with the dust of "
            "past knowledge and experience? What exactly is happening when "
            "this identification takes place?"
        ),
        "answer_paragraphs": [
            "Osho draws a clean structural distinction. The mind itself is pure - it is what Buddhists call the buddha-nature, the simple awareness that is. What gets impure is not the mind but the self that uses the mind, the I that is built up out of accumulated experiences. You are the dust; the mind is the mirror. So the question of how the mind becomes identified with dust is really the question of how the mind becomes identified with you, which is to say with everything you happen to be carrying.",
            "He demonstrates the mechanism with a thought experiment. If someone asks you who you are, the verbal answer points entirely to the past: a name, a family, a country, a religion, a profession. None of those is happening now; all of them are accumulated. You have moved through them and they have stuck. But if you drop the verbal answer and stay with what is actually present, the answer becomes simply 'I am' - and even the 'I' is not really needed. What remains is am-ness, formless and nameless.",
            "Identification, then, is the gluing of awareness to its accumulated contents. The original mind, which is pure awareness, gets fused with the inventory of name and form because the inventory is socially required - you cannot survive interactions without a label. The error is not having the label; the error is forgetting that the label is a utility, not a self. The dust is not the problem; identification with the dust is. The technique reverses the gluing without needing to throw the inventory away.",
        ],
        "answer_quotes": [
            "The mind is just the buddha-nature - the ultimate. You are the impurity.",
            "The deeper you move, the more you will feel just 'am-ness,' existence.",
        ],
    },

    # ─────────────────────────────────────────────────────────────────
    # Chapter 40 — Sudden Enlightenment and Its Obstacles (4 questions)
    # ─────────────────────────────────────────────────────────────────
    {
        "chapter": 40,
        "follows_chapter": 39,
        "title_hint": "Sudden Enlightenment and Its Obstacles",
        "question_paraphrase": (
            "You said the world and the ultimate are not gradually bridged - "
            "but in practice we feel a gradual increase in clarity and "
            "presence. What is this gradual growth, if the real event is "
            "always sudden?"
        ),
        "answer_paragraphs": [
            "Osho separates two questions that are usually fused. Enlightenment itself is sudden; the preparation for it is gradual. The mind cannot conceive of a sudden event - mind is a divider, and what it cannot break into degrees it tends to deny - so it converts the description into a story of incremental progress. The story is comforting and partly accurate: there really is preparation, and the preparation really is gradual. But the event at the centre of the preparation is not.",
            "He notes that many enlightened teachers have actually accommodated this confusion in compassion. They allowed students to believe in gradual growth because students who believe enlightenment is sudden often refuse to start - the very simplicity feels too much to begin from. So the masters spoke in the vocabulary of degrees, knowing that as the student worked the gradient up to its limit, the sudden thing would happen on its own. The talk of degrees is a doorway, not the room.",
            "What you experience as gradual increase, then, is the slow purification of the equipment, not the gradual approach of the event. Awareness becomes more refined, the distractions less heavy, the silence longer. None of this is itself enlightenment, but each refinement makes the explosion more possible. When the explosion comes, it does not arrive as the next step in a sequence; it arrives as a complete change of dimension that retroactively reframes everything that preceded it as a preparation.",
        ],
        "answer_quotes": [
            "In a sudden explosion, the beginning and the end are both the same.",
            "If it is said that enlightenment is only sudden and no gradual growth is possible, you are not even going to start.",
        ],
    },

    # ─────────────────────────────────────────────────────────────────
    # Chapter 42 — Alertness through Tantra (5 questions)
    # ─────────────────────────────────────────────────────────────────
    {
        "chapter": 42,
        "follows_chapter": 41,
        "title_hint": "Alertness through Tantra",
        "question_paraphrase": (
            "Surely an immoral life creates obstacles to meditation? "
            "How can one meditate while living without ethical discipline?"
        ),
        "answer_paragraphs": [
            "Osho refuses the framing's central assumption. Meditation is not a quality of your character; it is a quality of your consciousness. The question is not whether your acts are moral or immoral but whether you bring alertness to them. You can perform every socially-approved act while completely asleep, and society will reward you handsomely for it - in fact, sleeping morality is the most convenient kind of citizen society can produce. Morality without awareness is sleep with good manners.",
            "He sketches what asleep morality actually does inside a person. Because the morality is imposed from without while the person is unconscious, it can only be a layer of suppression on top of an unchanged inner life. The result is one of two things: either the person stays honest with the suppression, in which case the build-up eventually drives them mad, or the person becomes a hypocrite who maintains the surface morality while finding cunning ways to leak the suppressed material out. Hypocrisy is the saner of the two, which is why most asleep moral people end up there.",
            "Real morality, Osho says, is a by-product. It cannot be installed; it can only flower. When awareness becomes the centre, certain acts simply cease - not because they are forbidden but because the person can no longer perform them while remaining present to themselves. That is morality without suppression. It looks the same from outside as the imposed kind, but inside it has no shadow, no constant struggle, no leaking. The shortcut is therefore not to enforce morality and then meditate; it is to cultivate awareness, and let morality follow.",
        ],
        "answer_quotes": [
            "Meditation is not your character, it is not what you do. It is what you are.",
            "While asleep, real morality cannot happen to you.",
        ],
    },

    # ─────────────────────────────────────────────────────────────────
    # Chapter 44 — Secrets of Love and Liberation (4 questions)
    # ─────────────────────────────────────────────────────────────────
    {
        "chapter": 44,
        "follows_chapter": 43,
        "title_hint": "Secrets of Love and Liberation",
        "question_paraphrase": (
            "If Tantra is a love technique, why have modern men and women "
            "become so incapable of love?"
        ),
        "answer_paragraphs": [
            "Osho diagnoses the modern incapacity precisely. Love is not something you do; it is something you allow to happen. The modern mind has trained itself to be excellent at doing - we are the most efficient century at any task that admits of method - but in developing the doing-dimension we have lost the being-dimension on which love depends. Love cannot be performed; it can only be received and inhabited. Your presence, in the active sense of trying to make love happen, is the very obstacle.",
            "He extends the diagnosis to everything that cannot be done. Meditation cannot be done; play cannot be done; joy and happiness cannot be done. The modern mind, which has staked its identity on being able to do anything, has therefore become incapable of all of them at once. The shared structure of these capacities is that they require the doer to step aside, and a person whose entire self-worth rides on doing finds stepping aside intolerable. Where doing is the only mode, all the let-be capacities atrophy.",
            "There is a deeper fear underneath the technical incapacity. Love, like joy and meditation, possesses you - it is something larger than the doer that takes the doer over - and the modern psyche is built around the refusal to be possessed. We want to master things, never to be mastered. But mastery is only possible over the inanimate. Anything alive must be entered as a participant, not commanded as a tool. Love is alive in this sense, which is why no quantity of doing produces it.",
        ],
        "answer_quotes": [
            "Love is spontaneous. It cannot be controlled. The more you do, the more you will miss it.",
            "Modern man wants to be the master of everything, and you can only be the master of things - not of happenings.",
        ],
    },

    # ─────────────────────────────────────────────────────────────────
    # Chapter 46 — The Tantric Way to Freedom from Desires (3 questions)
    # ─────────────────────────────────────────────────────────────────
    {
        "chapter": 46,
        "follows_chapter": 45,
        "title_hint": "The Tantric Way to Freedom from Desires",
        "question_paraphrase": (
            "You said the motivation toward liberation is itself a barrier - "
            "but isn't that motivation an aspiration, not a desire? An "
            "intrinsic thirst rather than just another wanting?"
        ),
        "answer_paragraphs": [
            "Osho dismisses the sophistry. Desire is desire regardless of what it points at. Religious traditions have spent considerable energy giving spiritual desires nicer names - aspiration, longing, thirst, calling - so that practitioners can keep desiring in the dressing room of the spiritual life without recognising what they are doing. But the structure of the mental movement is identical: a present incompleteness, a future fulfilment, a tension between the two. The label on the object does not change the structural fact.",
            "He defines desire mechanistically. Desire is what happens when your mind is not at ease in this moment and projects its ease onto a future moment. The future does not exist - it is fantasy - but it has the appearance of a place where your peace is waiting. Whether the projected peace is wealth or paradise or moksha is irrelevant; the projection itself is the desire, and the projection is what keeps you out of the present where peace actually lives.",
            "From this it follows that liberation cannot be desired. The desire to be liberated displaces you from the only moment in which liberation could happen, exactly as the desire for money does. Liberation arrives only as a consequence of no-desire, never as the result of a desire for it. The technique, then, is not to desire better things; it is to notice the structure of desire itself, and let desiring fall away. What is left, when desire has stopped, is what was being aimed at all along.",
        ],
        "answer_quotes": [
            "Every desire is a bondage. Even if you desire God, it is a bondage; even if you desire liberation it is a bondage.",
            "Desire means that right now you are not okay.",
        ],
    },

    # ─────────────────────────────────────────────────────────────────
    # Chapter 48 — The Potentiality of the Seed (3 questions)
    # ─────────────────────────────────────────────────────────────────
    {
        "chapter": 48,
        "follows_chapter": 47,
        "title_hint": "The Potentiality of the Seed",
        "question_paraphrase": (
            "You say to have an ideal is a mistake, but you also describe "
            "Krishna, Christ and Buddha as the climax of human possibility. "
            "What is the difference between an inspiration and an ideal?"
        ),
        "answer_paragraphs": [
            "Osho draws a distinction the question itself almost contains. Buddha, Krishna and Christ are not ideals; their states - buddhahood, christhood - are. The ideal is the inner quality, never the outer person. If you take the person as your ideal, you will become an imitation, and the imitation will block the very state the original person had attained. Imitation is the structural opposite of attainment; the imitator is reaching for what they look like, not for what they are.",
            "He uses Meera and Buddha to make the point unforgettable. A real Meera dances in mad ecstasy; a real Buddha sits silent under the bodhi tree. Each is a perfect expression of the same inner reality - a zero-point at the centre - through a different temperament at the periphery. Try to put Buddha into Meera's dance and you destroy Buddha; try to seat Meera under Buddha's tree and you destroy Meera. The expression must come from the actual person, not be borrowed from a famous one.",
            "Inspiration, then, is the contact with the inner state via someone who has attained it; the ideal would be the imitation of their outer form. Inspiration is permission to bloom in your own way; the ideal is a constraint that prevents you from blooming at all. Tantra refuses ideals because ideals always produce imitations, and imitations can never reach the zero-point that the master they imitate is actually pointing toward.",
        ],
        "answer_quotes": [
            "Buddhahood is the ideal, not Buddha. Christhood is the ideal, not Jesus.",
            "Two 'somethings' can never be the same and two 'nothings' can never be different.",
        ],
    },

    # ─────────────────────────────────────────────────────────────────
    # Chapter 50 — Moving to the Roots (4 questions)
    # ─────────────────────────────────────────────────────────────────
    {
        "chapter": 50,
        "follows_chapter": 49,
        "title_hint": "Moving to the Roots",
        "question_paraphrase": (
            "Aren't right food, right work, right sleep, right behaviour also "
            "important factors for inner transformation? Isn't it a mistake to "
            "ignore the outer completely?"
        ),
        "answer_paragraphs": [
            "Osho offers a more careful position than the question implies. The outer cannot in itself produce the inner change, but it can prepare the situation in which the inner change becomes more likely - or, worse, it can become an absorbing project that lets you postpone the inner change indefinitely. The outer is not to be neglected; it is to be put in its place. It is the field; it is not the harvest.",
            "He warns about the obsession that can grow up around outer-work. The outer is infinite. There is always one more thing to refine - another diet, another posture, another adjusted habit - and a person can lose entire lives polishing the outer while the inner remains untouched. Without inner change, the outer can never be perfect; the obsession with outer perfection is therefore self-perpetuating, and the perfection is always a year away. The mind loves this work because it is endless and never confronts the actual self.",
            "He tells the Panchatantra fable to make the point unforgettable. A mouse, terrified of a cat, is turned by a magician into a cat - and immediately becomes terrified of the dog. Turned into a dog, it becomes terrified of the tiger. The body changes, the fear does not, because the inner mouse has not changed. So with the spiritual seeker who polishes the outer life: the form may keep upgrading, but the same inner anxiety chases the upgrade through every form. Inner work is the only kind that addresses the actual mouse.",
        ],
        "answer_quotes": [
            "The outer cannot change the inner, but the outer can help, or it can hinder.",
            "You can go on changing for lives and you will never be satisfied.",
        ],
    },

    # ─────────────────────────────────────────────────────────────────
    # Chapter 52 — Entering This Moment (6 questions)
    # ─────────────────────────────────────────────────────────────────
    {
        "chapter": 52,
        "follows_chapter": 51,
        "title_hint": "Entering This Moment",
        "question_paraphrase": (
            "If philosophies are anti-meditation, why do enlightened sages "
            "leave behind massive philosophical structures - Tantra, Yoga, "
            "Vedanta? Why didn't they just point and stay silent?"
        ),
        "answer_paragraphs": [
            "Osho corrects a translation problem at the root of the question. The Sanskrit word darshan does not mean philosophy at all - it means perception, seeing. Western philosophy is built on thinking; Eastern darshan is built on seeing. Hermann Hesse coined 'philosia' to capture the difference, fusing 'philo' with 'sia,' to see. Calling the writings of Patanjali, Buddha or Kapil 'philosophy' imports a thinking-frame they do not belong in. They are not philosophers. They are seers writing down what they have seen.",
            "The two operations are not just different; they are diametrically opposite. When you can see, you do not need to think. Thinking, in Osho's reading, is what you do in the absence of seeing - it is groping in the dark with the available memories. A Buddha who has actually seen produces no philosophical conclusions; he produces transmissions of perception. The structure may look like a philosophical treatise from outside, but its function is completely different.",
            "So the writings of the realised are not anti-meditation; they are pointers from inside meditation. The Western philosophical tradition is what Osho is calling anti-meditation - the project of arriving at truth by thinking harder, with no eye opened. Reading Patanjali or Buddha as philosophy in that Western sense is what makes them anti-meditation; reading them as records of perception is what restores them to their original function.",
        ],
        "answer_quotes": [
            "Darshan means perception, philosophy means thinking.",
            "You only think when you cannot see. If you can see, there is no reason to think.",
        ],
    },

    # ─────────────────────────────────────────────────────────────────
    # Chapter 54 — The Fire of Awareness (3 questions)
    # ─────────────────────────────────────────────────────────────────
    {
        "chapter": 54,
        "follows_chapter": 53,
        "title_hint": "The Fire of Awareness",
        "question_paraphrase": (
            "A meditator who is open and vulnerable feels harmed by negative, "
            "tense vibrations from the world around them. How can one preserve "
            "such a vulnerable psyche from harmful influences?"
        ),
        "answer_paragraphs": [
            "Osho's reply is sharp. If you are really vulnerable, nothing is negative for you - because the negative is your interpretation. Nothing is harmful, because the harmful is your interpretation. To be open is precisely to drop the interpretive frame in which some currents are 'good vibrations' and some are 'harmful.' The questioner has confused vulnerability with sensitivity to a story. Real openness has no story.",
            "He locates the supposed enemy. The enemy exists because you are protecting yourself, and the protection creates the relationship in which something appears as enemy. Drop the protection and the universe is friendly - although, he is careful to add, you will not even feel it as friendly, because friendliness as a feeling can only exist in contrast with the felt possibility of enmity. Once enmity is gone, the friendliness becomes simply the medium in which everything is happening.",
            "What looks like vulnerability in the modern sense, then, is often only a refined form of resistance. A person who is genuinely vulnerable is ready to live in insecurity, ready even to die without protest, and therefore has no surface for harm to land on. Lao Tzu's whole teaching, Osho says, rests on this: when you stop denying anything, the universe stops appearing as a system of enemies, because the enemies were always your interpretation rather than the universe's intention.",
        ],
        "answer_quotes": [
            "If you are really vulnerable, nothing is negative for you - because the negative is your interpretation.",
            "The enemies are your creation. They are not there outside; they exist in your interpretation.",
        ],
    },

    # ─────────────────────────────────────────────────────────────────
    # Chapter 56 — Discovering Emptiness (4 questions)
    # ─────────────────────────────────────────────────────────────────
    {
        "chapter": 56,
        "follows_chapter": 55,
        "title_hint": "Discovering Emptiness",
        "question_paraphrase": (
            "When the I drops in meditation and an emptiness appears, the "
            "frustration is that nothing arrives to fill it. How can one "
            "learn to live with that emptiness?"
        ),
        "answer_paragraphs": [
            "Osho dismantles the question's hidden expectation. Emptiness IS the unknown. The questioner is waiting for something - some divine arrival, some unknown force - to descend and fill the emptiness, but as long as the waiting is there, the emptiness is not real. A waiter is a fullness disguised as emptiness; a hoper has not yet emptied. Don't wait. Don't even hope. Simply be empty, and the unknown is already present in the emptiness, with no gap whatsoever.",
            "What feels like frustration, then, is a structural mistake. After the ego falls away, the absence of the ego is felt for a while as a vacancy where something should be. This is the residue of the long habit of being filled. First the ego goes; then the felt absence of the ego goes; only after both have gone is the practitioner really empty. To be really empty, in Osho's vocabulary, is already to be really filled - because the inner space the ego was occupying turns out to have been the divine all along, hidden by the very thing complaining about its absence.",
            "He cites Buddha. When asked what he had attained in his enlightenment, Buddha replied that he had not attained anything; he had only discovered what was already there. The treasure was always under the floor; the work was the digging, not the manufacturing. So with the meditator: nothing new will come, because nothing was ever absent. The frustration of the unfilled emptiness is the last form of the ego pretending to wait for itself.",
        ],
        "answer_quotes": [
            "When you are really empty the unknown has descended upon you. There is not a single moment's gap.",
            "Buddha said: I have not achieved anything. I have only discovered what was already there.",
        ],
    },

    # ─────────────────────────────────────────────────────────────────
    # Chapter 58 — Go Beyond Karma (4 questions)
    # ─────────────────────────────────────────────────────────────────
    {
        "chapter": 58,
        "follows_chapter": 57,
        "title_hint": "Go Beyond Karma",
        "question_paraphrase": (
            "You call these techniques shortcuts, revolutions - but isn't a "
            "shortcut against Tao, against swabhav, against nature itself?"
        ),
        "answer_paragraphs": [
            "Osho concedes the point and then turns it. Yes, every technique is against Tao, because every effort is against Tao. The instant you make any effort - including the effort to surrender, including the effort not to make effort - you have stepped out of swabhav. So if you can leave everything to Tao, no technique is needed. That is the ultimate technique: a non-technique, complete surrender, a deep let-go in which time itself is offered up alongside everything else.",
            "But he is realistic about who can actually do this. Real surrender cannot be practised; the moment you practise it, you are doing something rather than letting go, and the doing reintroduces the very effort that surrender is supposed to dissolve. Most people, asked to surrender, immediately begin to manage their surrender, and the management becomes another form of holding on. So in practice, very few can take the Tao route - and those who can have usually taken it as a final step after many techniques have already exhausted the will.",
            "Tantra and Yoga are therefore offered as honest second-best paths for those who cannot surrender outright. They use technique knowingly, as a structured way of weakening the very faculty that makes surrender impossible. The shortcut is not against nature in any final sense; it is a calibrated detour through unnatural effort by which the unnatural effort is eventually used up. After it, surrender becomes possible because there is no longer anyone left to manage it.",
        ],
        "answer_quotes": [
            "Surrender is non-temporal; it is beyond time.",
            "If you practice surrender, it is not surrender.",
        ],
    },

    # ─────────────────────────────────────────────────────────────────
    # Chapter 60 — Liberate Yourself From Yourself (5 questions)
    # ─────────────────────────────────────────────────────────────────
    {
        "chapter": 60,
        "follows_chapter": 59,
        "title_hint": "Liberate Yourself From Yourself",
        "question_paraphrase": (
            "You speak of religion as total freedom, moksha, and you also "
            "stress surrender. Aren't freedom and surrender contradictory in "
            "their very meanings?"
        ),
        "answer_paragraphs": [
            "Osho says the contradiction is linguistic, not existential. As long as you remain who you are - a separate ego operating against the universe - freedom is structurally impossible, because the very fact of being a separate ego is the bondage you are asking to be free of. Freedom of an ego is a contradiction in terms; the ego is the wall. So 'freedom from bondage' has to be freedom from the ego, and freedom from the ego is what the word 'surrender' actually means in this tradition.",
            "He sketches the geometry. You are not separate from existence; you are an organic part of it, breathing it and being breathed by it. The ego gives you the false feeling of being separate, and on the basis of that false feeling you start fighting the universe. The fight is doomed - the part cannot defeat the whole - and every defeat in that doomed fight is felt as bondage and limit. Wherever you turn, you hit the wall, but the wall is not in existence; it is moving with the ego.",
            "Surrender, in this vocabulary, is the dropping of the false self, not the giving up of a real one. You are not surrendering anything that exists; you are surrendering an illusion. The moment that illusion drops, the wall drops with it, and what was experienced as bondage becomes recognised as the universe in which you were always free. So freedom and surrender are not opposites at all; they are two descriptions of the same event from outside and inside.",
        ],
        "answer_quotes": [
            "You cannot be free remaining as you are, because as you are is your bondage.",
            "By surrender it is meant that you surrender the ego. You are not surrendering reality; you are just surrendering a false attitude.",
        ],
    },

    # ─────────────────────────────────────────────────────────────────
    # Chapter 62 — Right Now Is the Goal (3 questions)
    # ─────────────────────────────────────────────────────────────────
    {
        "chapter": 62,
        "follows_chapter": 61,
        "title_hint": "Right Now Is the Goal",
        "question_paraphrase": (
            "Yesterday you said one should hurry, because there is little "
            "time. Earlier you said the whole process should be effortless "
            "play. How can hurry and play be reconciled?"
        ),
        "answer_paragraphs": [
            "Osho refuses to reconcile them. The two instructions are different techniques aimed at different temperaments, and only confusion comes from trying to perform both at once. The let-go, no-effort, effortless-play approach is suited to the feminine mind - the mind that can wait, surrender, and receive. The hurry-up, the-house-is-on-fire approach is suited to the masculine mind - the mind that needs effort, urgency, an objective. Half of humanity belongs to each, regardless of biological sex.",
            "He is careful to clarify that 'feminine mind' and 'masculine mind' are not the same as female and male bodies. There are women whose minds are masculine and men whose minds are feminine, and the whole point of the type-distinction is to direct each practitioner to the technique their actual mind can use. A feminine mind making effort produces only anguish without progress; a masculine mind waiting passively produces only stagnation without breakthrough. The mismatch between mind and method is what derails most spiritual practice.",
            "So the practical advice is to choose. Find which kind of mind you are - by feeling, not by ideology - and then commit to the matching technique without trying to harmonise it with its opposite. Reconciliation across types is a job for after the breakthrough, not before. Right now, mixing them only adds confusion to whichever pure form would have worked. The hurry-up belongs to one path; the play to the other; and both lead home, but never together.",
        ],
        "answer_quotes": [
            "Don't try to reconcile different techniques. This is suitable only for a part of humanity.",
            "If a feminine mind makes effort, the effort will be the undoing for it.",
        ],
    },

    # ─────────────────────────────────────────────────────────────────
    # Chapter 64 — Choicelessness Is Bliss (2 questions)
    # ─────────────────────────────────────────────────────────────────
    {
        "chapter": 64,
        "follows_chapter": 63,
        "title_hint": "Choicelessness Is Bliss",
        "question_paraphrase": (
            "Are these really the only two alternatives - a life of bliss or "
            "a life of suffering? And why have most people chosen the path "
            "of suffering, if both options are open?"
        ),
        "answer_paragraphs": [
            "Osho restates the question to expose its hidden mistake. People do not, as the questioner imagines, choose suffering. People always choose bliss; that is precisely what creates the suffering. The real choice is not between bliss and misery; the real choice is between choosing and not choosing. When you choose bliss, you have already cut life into two and rejected one half - and the rejected half does not vanish. It waits, gathering force, ready to assert itself the moment your grip on the chosen half slips.",
            "Choice itself, then, is the source of misery, regardless of what is chosen. Life is a totality. The moment you say 'I want this and not that,' you have set yourself against half of life, and life cannot be defeated. Whatever you push down comes up; whatever you cling to begins to flow away. The result is the constant inner war we mistake for the human condition - bliss perpetually escaping, suffering perpetually returning, despite the best intentions.",
            "Bliss, in this analysis, is what is left when choosing stops. It cannot be selected; it can only be allowed by a witness who no longer takes sides. Life is also change - flux - and clinging to any moment of happiness is therefore structurally doomed, because the moment refuses to stay still. The non-chooser does not lose happiness when it changes; the non-chooser is also unmoved when suffering arrives, because both are part of the totality being witnessed. That witnessing posture, not the things being witnessed, is the bliss.",
        ],
        "answer_quotes": [
            "If you choose to be in bliss, you will be in suffering, because to be in bliss means to be choiceless.",
            "Life is a totality. If you choose something and deny something, that which you deny will come to you.",
        ],
    },

    # ─────────────────────────────────────────────────────────────────
    # Chapter 66 — A Buddha Is a Nobody (4 questions)
    # ─────────────────────────────────────────────────────────────────
    {
        "chapter": 66,
        "follows_chapter": 65,
        "title_hint": "A Buddha Is a Nobody",
        "question_paraphrase": (
            "I feel an inner emptiness in deepening meditation, but I do not "
            "feel anything that I would call mystery. What do you mean by "
            "mystery, and how is it actually felt?"
        ),
        "answer_paragraphs": [
            "Osho's answer is structural rather than descriptive. The inner emptiness itself is the mystery. You do not feel it the way you feel a sensation, because feeling implies a feeler separate from what is felt. When the inner is really empty, there is no observer left over to register the emptiness. So if you are saying you feel emptiness, you are not yet empty - some residual ego is still present, observing itself observing, and reporting the observation as 'I feel empty.'",
            "He cites Bokuju's encounter with his master to make the point sharp. Bokuju came proudly to his master and said, 'Now there is nothing, I have become empty.' The master's reply was: go out and throw out this nothingness too. As long as the nothingness is something you have, the having is the residual ego - the same problem in subtler dress. The mystery is not a felt nothingness but the dissolution of the one who would feel it.",
            "What this means practically is that a real arrival at the mystery looks like nothing from inside; there is no 'aha.' If there were an 'aha,' there would still be a someone collecting the experience, and that someone is exactly what blocks the mystery from being revealed. So the felt emptiness the questioner reports is a useful waystation, but it is not the destination. The destination is unreported and unreportable, because the reporter has gone too.",
        ],
        "answer_quotes": [
            "When the inner space is there, then you are not. You cannot observe it.",
            "When the inner is really empty, you are not, because you are the thing by which the inner is filled.",
        ],
    },

    # ─────────────────────────────────────────────────────────────────
    # Chapter 68 — Energy Enjoys Itself Playing (4 questions)
    # ─────────────────────────────────────────────────────────────────
    {
        "chapter": 68,
        "follows_chapter": 67,
        "title_hint": "Energy Enjoys Itself Playing",
        "question_paraphrase": (
            "If desire creates bondage, isn't a positive imagination of bliss "
            "and happiness also a kind of desire? Doesn't imagination "
            "therefore also create tension?"
        ),
        "answer_paragraphs": [
            "Osho draws a careful distinction. Imagination is not desire; imagination is play. The two get confused only because we are so used to running everything through the engine of desire that we cannot conceive of doing anything without an end-point. But imagination, used as a technique, is not aimed at any future state - it is its own occupation. Played as play, it produces no bondage. Pressed into the service of desire, it instantly becomes bondage, exactly as any other action would.",
            "He extends this to meditation itself. Meditation is the ultimate play. It is not a means to enlightenment; enlightenment is what happens inside it, not what it produces. Treat meditation as a means to anything - liberation, peace, even health - and it ceases to be meditation, because the moment a means is in the air, the future is in the air, and meditation lives in the present. The masters who have known have always insisted on meditation for meditation's sake, not as an instrument but as the thing itself.",
            "The mind, however, refuses to do anything without a future hanging on it. It manufactures projections it can chase, real or imaginary, just so it can stay in motion. This is what desire is, structurally: working in the present for the future. The technique-user who turns imagination into desire does so habitually rather than choosingly, and the practice quietly becomes another form of work. The corrective is to play imagination as a child plays - absorbed, present, and wanting nothing on the far side of the play.",
        ],
        "answer_quotes": [
            "Imagination is not desire. Imagination is just a play.",
            "Meditation is the ultimate play, it is not a means to enlightenment.",
        ],
    },

    # ─────────────────────────────────────────────────────────────────
    # Chapter 70 — Suffer the Pain of Aloneness (5 questions)
    # ─────────────────────────────────────────────────────────────────
    {
        "chapter": 70,
        "follows_chapter": 69,
        "title_hint": "Suffer the Pain of Aloneness",
        "question_paraphrase": (
            "Confronting myself in aloneness is genuinely fearful and "
            "painful. The fear feels almost impossible to face. What can "
            "I do with it?"
        ),
        "answer_paragraphs": [
            "Osho says: do nothing. Suffer it. Do not divert the mind, do not distract yourself, do not escape. The fear and the pain are real but they are also a good sign - every real birth is preceded by pain, and what is dying in this case is not you but the constructed self that cannot survive without others. The traditional Sanskrit word for this deliberate enduring of inner pain is tapas, austerity, and it is not a moral discipline; it is a passage.",
            "He explains why the pain is so specific. Your ego was built in relationship - it is, in effect, a contribution from others. People told you that you were a good person, or a bad person, or interesting, or boring, and out of those reflections you assembled the image you have been carrying. In aloneness, the contributors are gone, and the image they were sustaining begins to lose its foundation. What feels like death is not your death; it is the death of an image that was never really you.",
            "Even the 'bad' image, Osho notes, was a way of getting attention - a negative form of social existence. Bad people and good people are not as different as they look; both depend on the gaze of others. Aloneness withdraws all gazes at once, and both kinds of image collapse together. What is left, after the collapse, is whatever was underneath the imagery the whole time. The pain of aloneness is the pain of that excavation. Sit with it. It is not punishment; it is preparation.",
        ],
        "answer_quotes": [
            "Your ego gets ill. Your ego can exist only with others.",
            "Bad men and good men are not basically different - both are gaining their egos.",
        ],
    },

    # ─────────────────────────────────────────────────────────────────
    # Chapter 72 — Start Living in Insecurity (4 questions)
    # ─────────────────────────────────────────────────────────────────
    {
        "chapter": 72,
        "follows_chapter": 71,
        "title_hint": "Start Living in Insecurity",
        "question_paraphrase": (
            "You have said that real love is possible only with death. Then "
            "what about Buddha's love? How does that fit?"
        ),
        "answer_paragraphs": [
            "Osho first describes the love most people know. For an unawakened mind, love is always tied to hate; the two are aspects of the same coin and trade places like night and day. When the love is tired, it falls into the unconscious and the hate side surfaces; when the hate is exhausted, the love returns. The lover is bewildered to find both feelings pointed at the same person, because the structure of ordinary love guarantees the alternation.",
            "A Buddha's love is not love in this sense at all. Buddha himself avoided the word and used compassion instead - though Osho notes that compassion in your usage is also mixed with cruelty, exactly as your love is mixed with hate. In a Buddha, the dualism has dissolved entirely. The opposite is no longer present. So whatever quality flows out of him is one-sided in a way ordinary feeling never is, and the word for it is therefore approximate however you translate it.",
            "The phenomenology is opposite to ours. Ordinary love is hot, because hatred is just below the surface and gives the love its temperature. Buddha's love is cool, because there is no hatred underneath providing heat. To us, cool love sounds like indifference, because we have never tasted love without the volatile pressure of its opposite. But Buddha's coolness is a deeper warmth - a quality of climate rather than temperature - that does not flicker, does not exhaust, and does not turn into its opposite. It cannot, because the opposite has been absorbed.",
        ],
        "answer_quotes": [
            "For the ignorant mind hate and love are just two aspects of the same coin.",
            "Your love is a dis-ease; Buddha's love is total relaxation.",
        ],
    },

    # ─────────────────────────────────────────────────────────────────
    # Chapter 74 — Sensitivity Is Awareness (4 questions)
    # ─────────────────────────────────────────────────────────────────
    {
        "chapter": 74,
        "follows_chapter": 73,
        "title_hint": "Sensitivity Is Awareness",
        "question_paraphrase": (
            "As meditation deepens, sensitivity to objects, events and people "
            "increases - and this seems to deepen attachment. How does one "
            "become sensitive and yet remain detached?"
        ),
        "answer_paragraphs": [
            "Osho dissolves the supposed conflict. Sensitivity and attachment are not the same thing; sensitivity is awareness, and awareness is precisely what breaks attachment. The questioner has confused the two because they often arrive together in the unawake life, but in the awake life sensitivity rises while attachment falls. A Buddha is at the maximum of sensitivity - he feels everything, completely - and at the minimum of attachment, because the bridge attachment runs over has dissolved.",
            "He locates the bridge. Attachment is not constructed of feeling; it is constructed of unconsciousness. Where you are unaware, the energy of relation slides into possession - the unconscious mind cannot help making the move from 'this matters to me' to 'this is mine.' Where you are conscious, the same feeling does not produce ownership, because consciousness sees the boundary and respects it. Attachment, in this sense, is a gross quality, not a subtle one. Animals are attached more easily than humans, exactly because animals are more unconscious.",
            "He notes a sad cultural symptom of the same dynamic. In societies where human relationships have grown thin and distant, people have begun to attach more deeply to animals - dogs, cats - because animals can be possessed in a way humans increasingly resist. The depth of feeling is not greater there; only the unconsciousness is greater, and so the attachment is more freely manufactured. Sensitivity to a human, fully met, would not be possessive. The deeper the awareness, the cleaner the contact.",
        ],
        "answer_quotes": [
            "Sensitivity is not attachment, sensitivity is awareness.",
            "Attachment is a very gross quality, it is not subtle. For attachment you need not be aware and alert.",
        ],
    },

    # ─────────────────────────────────────────────────────────────────
    # Chapter 76 — Life is Sex Energy (4 questions)
    # ─────────────────────────────────────────────────────────────────
    {
        "chapter": 76,
        "follows_chapter": 75,
        "title_hint": "Life Is Sex Energy",
        "question_paraphrase": (
            "Tantra is usually understood as concerned only with sex energy "
            "and sex-centre techniques. If that is true, most of the sutras "
            "in Vigyan Bhairav don't seem to be tantric at all. Is the "
            "popular understanding wrong?"
        ),
        "answer_paragraphs": [
            "Osho corrects the vocabulary first. When Tantra says 'sex energy,' it does not mean what modern usage means - the narrow energy of reproduction. It means life energy itself; sex is synonymous with life. The same applies to Freud, who Osho says was widely misread for the same reason: when Freud reduced human behaviour to sex, he meant the wide field of life-force, not the bedroom. Reproduction is one expression of that field, but it is one note among many.",
            "He gives a strikingly broad example. Two people in conversation - a speaker and a listener - are in a sexual relationship in this Tantric sense, because the speaker is penetrating with words and the listener is receiving. If the listener stops being receptive and begins to argue internally, the listener has become male in the conversation, and no real listening occurs. The structure of any meeting between active and passive, positive and negative, is the structure of sex. Wherever polarities meet, sex has happened.",
            "From this it follows that the tantric techniques are exactly as broad as life. A breath technique meets the in-breath and out-breath, a sound technique meets the call and the silence, a looking technique meets the seer and the seen - every one of these is a meeting of polarities, and every one therefore qualifies as a sex technique in Tantra's sense. Reading Tantra as narrowly genital is a Western mistake that misses the entire metaphysics. The bedroom-sex sutra is one technique among the hundred and twelve; the rest are no less tantric for using different polarities.",
        ],
        "answer_quotes": [
            "When Tantra says 'sex' energy it means 'life' energy.",
            "Wherever polarities meet, opposites meet, it is sex.",
        ],
    },

    # ─────────────────────────────────────────────────────────────────
    # Chapter 78 — The Inner Guide (3 questions)
    # ─────────────────────────────────────────────────────────────────
    {
        "chapter": 78,
        "follows_chapter": 77,
        "title_hint": "The Inner Guide",
        "question_paraphrase": (
            "Some of the techniques look more like end-states than methods - "
            "'become universal consciousness,' 'be this one.' Are these "
            "techniques meant only for very advanced practitioners?"
        ),
        "answer_paragraphs": [
            "Osho corrects a common misunderstanding. These suggestion-techniques are not for advanced practitioners; they are for innocent ones. The advanced practitioner has accumulated too much - too much practice, too much vocabulary, too much investment in the technique-as-process - to receive a bare suggestion as if it were enough. The innocent person, who has not yet built up that apparatus, can take a suggestion and have the inner being open instantly, because what the suggestion points to was never far away.",
            "The structural reason is straightforward. Most spiritual techniques work by removing barriers, and barrier-removal takes time because the barriers were laid down over time. But these particular techniques operate from the assumption that you are already what you are reaching for. A seed must grow into a tree; that is a process. But you are not a seed - you are a tree behind a curtain, and a suggestion can pull the curtain aside if there is enough trust to let it. The work is one of attention, not of construction.",
            "This is why the tradition places so much weight on shraddha, trust. The advanced practitioner often cannot trust because the very development that made them advanced was a development of effort. Effort is the ego's contribution; trust is its cessation. So the apparently 'advanced' techniques are, paradoxically, easiest for the genuinely simple, and hardest for those who have spent years preparing for them. The path of trust does not bypass effort - it ends it.",
        ],
        "answer_quotes": [
            "Such techniques were meant, not for very advanced persons, but for very innocent persons.",
            "These techniques are not for advanced people; they are for simple, innocent people.",
        ],
    },

    # ─────────────────────────────────────────────────────────────────
    # Chapter 80 — All and Nothing Mean the Same (5 questions)
    # ─────────────────────────────────────────────────────────────────
    {
        "chapter": 80,
        "follows_chapter": 79,
        "title_hint": "All and Nothing Mean the Same",
        "question_paraphrase": (
            "You say there is no one inside us, only a void, an emptiness. "
            "But then why do you also so often call it the being, the centre? "
            "Aren't these contradictory descriptions?"
        ),
        "answer_paragraphs": [
            "Osho says the contradiction is grammatical, not real. The total and the zero look opposite in dictionaries but converge in life, because both are absolute terms that admit no degrees. Saying 'I love no one' and 'I love everyone' produces the same lived behaviour; the difference between them only appears when love is partial - directed at this person and not that one. Once love is total or zero, the surface labels stop mattering, because the difference they were tracking has dissolved.",
            "This is why some realised teachers describe the inner state in negative terms - shunya, emptiness, no-self - and others in positive terms - brahma, atma, supreme being. Both descriptions are accurate, both fall short, and both are pointing at the same thing. Each is forced into its choice of vocabulary by the language available, not by the reality being described. A reader who treats the two vocabularies as competing schools has missed what both are pointing at.",
            "He notes that some teachers refused to choose between the two and stayed silent. The moment you label the absolute - whether positively or negatively - you have erred, because the absolute includes both poles of every distinction language uses. To call God 'life' is to assign death to someone else, and the someone else then becomes a second God or a devil. To call the inner state 'being' is to oppose it to non-being, but it includes both. Silence is the only fully accurate description, and in absence of silence either label is a usable approximation.",
        ],
        "answer_quotes": [
            "All and nothing mean the same. In dictionaries they are opposites but in life they are not.",
            "The total and the zero have no degrees. So you can call the total a zero, or you can call a zero the total.",
        ],
    },

    # __APPEND_MARKER__
]


# ─────────────────────────────────────────────────────────────────────
# Output assembly + sanity checks
# ─────────────────────────────────────────────────────────────────────
OUTPUT = {
    "source_book": "The Book of Secrets (Vigyan Bhairav Tantra) by Osho",
    "description": (
        "One paraphrased Q&A pull per even-numbered chapter (4..80) of Osho's "
        "discourses on Vigyan Bhairav Tantra. Each entry surfaces the most "
        "piercing question of that Q&A session and a paraphrased summary of "
        "Osho's answer, written in the file author's own English prose but "
        "tracking the original argument faithfully. The pulls are intended "
        "to be rendered as expandable callouts at the end of the preceding "
        "odd chapter's section in the merged book, so that a reader who has "
        "just finished a chapter's techniques sees the questions those "
        "techniques actually elicited from real listeners."
    ),
    "qa_count": len(QA),
    "qa": QA,
}

# ── Validation ───────────────────────────────────────────────────────
assert len(QA) == 39, f"Expected 39 Q&A entries, got {len(QA)}"

expected_chapters = list(range(4, 81, 2))
actual_chapters = [q["chapter"] for q in QA]
assert actual_chapters == expected_chapters, (
    f"Chapter numbers don't match. Expected {expected_chapters}, "
    f"got {actual_chapters}"
)

problems: list[str] = []
total_q_words = 0
total_a_words = 0
total_quote_words = 0
total_a_paragraphs = 0
total_quotes = 0
for q in QA:
    n = q["chapter"]
    # follows_chapter must be the immediately preceding odd chapter
    if q.get("follows_chapter") != n - 1:
        problems.append(
            f"ch{n}: follows_chapter is {q.get('follows_chapter')!r}, "
            f"expected {n - 1}"
        )
    qp = q.get("question_paraphrase", "")
    paragraphs = q.get("answer_paragraphs", [])
    quotes = q.get("answer_quotes", [])

    qp_wc = len(qp.split())
    total_q_words += qp_wc
    if not (15 <= qp_wc <= 60):
        problems.append(
            f"ch{n}: question_paraphrase is {qp_wc} words "
            f"(want 15-60)"
        )

    if not (2 <= len(paragraphs) <= 4):
        problems.append(
            f"ch{n}: {len(paragraphs)} answer paragraphs (want 2-4)"
        )
    for i, p in enumerate(paragraphs):
        wc = len(p.split())
        total_a_words += wc
        total_a_paragraphs += 1
        if wc < 60:
            problems.append(
                f"ch{n} answer p{i+1}: only {wc} words (want >=60)"
            )

    if not (1 <= len(quotes) <= 3):
        problems.append(
            f"ch{n}: {len(quotes)} answer quotes (want 1-3)"
        )
    for i, qstr in enumerate(quotes):
        wc = len(qstr.split())
        total_quote_words += wc
        total_quotes += 1
        if wc >= 35:
            problems.append(
                f"ch{n} quote {i+1}: {wc} words (want <35)"
            )

if problems:
    print("VALIDATION ISSUES:")
    for p in problems:
        print("  -", p)
else:
    print("All validation checks passed.")

out_path = Path(__file__).parent / "_chapter_qa.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(OUTPUT, f, indent=2, ensure_ascii=False)

print(f"\nWrote {out_path}")
print(f"Q&A entries          : {len(QA)}")
print(f"Avg question words   : {total_q_words/len(QA):.1f}")
print(f"Avg answer paragraphs: {total_a_paragraphs/len(QA):.1f}")
print(f"Avg answer words     : {total_a_words/len(QA):.1f}")
print(f"Avg quotes per entry : {total_quotes/len(QA):.1f}")
print(f"Avg quote words      : {total_quote_words/total_quotes:.1f}")
print(f"Total body words     : {total_a_words + total_q_words}")
