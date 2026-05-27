"""
Build _chapter_intros.json from comprehensive multi-paragraph framings of
Osho's 39 sutra-introducing chapters in The Book of Secrets.

Schema (per chapter entry):
  - chapter:   int (odd, 3..79)
  - title:     str
  - paragraphs: list[str]   3 to 5 paragraphs of paraphrased framing
  - quotes:     list[str]   2 to 3 short attributed direct quotes (each <30 words)

The paragraphs are written by the author of this file in their own English
prose, but track Osho's argument faithfully chapter-by-chapter, drawing from
the discourse text that opens each chapter (extracted from the EPUB into
.epub_work/extracted/chNN_framing.txt). The direct quotes are short verbatim
fragments attributed to Osho.
"""

import json
import re
from pathlib import Path

CHAPTERS = [
    # ──────────────────────────────────────────────────────────────────
    # Chapter 3 — Breath: A Bridge to the Universe
    # ──────────────────────────────────────────────────────────────────
    {
        "chapter": 3,
        "title": "Breath - A Bridge to the Universe",
        "paragraphs": [
            "Before the four breath techniques are even named, Osho asks the reader to absorb a single, decisive premise: truth is not a future achievement but the present situation. You are already what you are seeking, and so the language of the spiritual quest - reaching, attaining, arriving - is structurally misleading. Every technique Shiva is about to give will only make sense once this is internalised, because each one is a way of returning attention to a fact that has never moved.",
            "The obstacle, Osho insists, is the very mechanism we are trying to use. The mind exists only as a movement between past and future; in the actual present it has no room to operate. So when the mind takes up the search for truth, it pushes truth into a tomorrow where the mind can pursue it - and in doing so guarantees that it will be missed. The seeker and the sought are always in the present together, but seeking itself is a journey forward in time and therefore moves you out of the very moment in which you would meet what you are looking for.",
            "This is why Shiva refuses to philosophise. Other masters - Buddha, Lao Tzu, Krishna - have at least framed their techniques with conceptual prologues, but Osho stresses that Shiva will not even do that. The mind is too cunning: hand it a doctrine of non-seeking and it immediately turns non-desire into a new desire and non-attainment into a new attainment, smuggling the entire problem in through the back door. People come to Osho asking 'how not to desire,' and they have not noticed that the question itself is a desire. The only way past this trap is technique, not theory.",
            "The four breath sutras, then, are simply turnings of attention. Done properly, the technique drops you into the present, and in the present the mind cannot continue - thoughts have nowhere to move. From birth to death the body changes in every other respect, but breathing is the one continuous current beneath the whole arc, and so it is where Tantra first places its lever. Each of these four techniques exploits a small natural pause in that current - between in-breath and out-breath, at the turn, at the fusion, at the still point - to slip you behind thought into pure being.",
        ],
        "quotes": [
            "You cannot seek truth. You can find it, but you cannot seek it. The very seeking is the hindrance.",
            "The truth is in the present, and mind is always in the future or in the past, so there is no meeting between mind and truth.",
            "Your being here and now is the truth, and your being here and now is the freedom, and your being here and now is the nirvana.",
        ],
    },

    # ──────────────────────────────────────────────────────────────────
    # Chapter 5 — Five Techniques of Attentiveness
    # ──────────────────────────────────────────────────────────────────
    {
        "chapter": 5,
        "title": "Five Techniques of Attentiveness",
        "paragraphs": [
            "Osho frames this set with a long anecdote about Pythagoras, who, after travelling to Egypt to be admitted to a secret esoteric school, was turned away. He had come, he said, in pursuit of knowledge - but the school replied that they were not interested in knowledge at all, only in actual experience, and that until he had completed forty days of fasting and conscious breathing he could not enter. Pythagoras had to submit. When at last he was let in, he reportedly said that the man who entered was no longer the man who had applied: his centre had moved from intellect to feeling, from concept to lived reality.",
            "That training, Osho explains, is the Indian method now appearing in Shiva's first sutra, transmitted from India to Egypt and only later to the Greeks. The technique focuses attention at a precise location - the point between the eyebrows, where Tantra locates the dormant third eye and modern anatomy locates the pineal gland. This point is unusual in two ways: it is dormant only because attention has never been placed there, and it is magnetic, in the sense that once attention is offered to it the point itself takes hold and pulls awareness deeper. Effort drops away; the technique starts working you instead of you working the technique.",
            "What follows, Osho says, is a quiet but decisive shift in identification. Until now you have lived inside your moods - you have been the anger, the desire, the worry. Once attention settles between the eyebrows, the same anger and desire become objects you can watch. Thoughts move past like clouds, weather rather than weather you are stuck inside. From this vantage you discover that you were never the contents of consciousness in the first place; you were always the witness. The sutras that follow build on this same shift - attention as the food, the field, and the doorway of awakening.",
        ],
        "quotes": [
            "For the third eye, attention is food. It has been hungry for lives and lives.",
            "From the intellect it has come down to the heart. Now I can feel things.",
            "Truth is not a concept to me, but a life. It is not going to be a philosophy, but rather, an experience - existential.",
        ],
    },

    # ──────────────────────────────────────────────────────────────────
    # Chapter 7 — Techniques to Put You at Ease
    # ──────────────────────────────────────────────────────────────────
    {
        "chapter": 7,
        "title": "Techniques to Put You at Ease",
        "paragraphs": [
            "Osho opens with a single diagnostic image: every human being has a centre, but lives off it - and this off-centre living is the structural cause of every form of inner tension. To the extent that you have wandered from the centre, you are pulled toward madness; to the extent that you return to it, you become enlightened. Most of us live in the gap between the two, neither fully out nor fully home, and it is in that swinging space that anguish breeds.",
            "From this he sketches four types of human being. The first is the so-called normal person, who has fixed an identity for himself - doctor, engineer, saint - and clings to it. He never tastes ecstasy and never tastes madness; he is, in Osho's blunt phrase, a dead man living between two points. The second is the artist, the poet, the painter, who has a liquid identity: sometimes a Buddha, sometimes a madman, anguished because he cannot pin himself down. The third is the permanently mad, who has gone outside himself completely and forgotten the way home. The fourth is the Buddha, who has returned and stays.",
            "What distinguishes the fourth state is the absence of becoming. The Buddha still eats, still sleeps, still feels the heat of the sun and the bite of the cold wind, but he never eats yesterday's meal or tomorrow's - he eats today. There is no projection, no cerebral consumption, no postponement. Wherever there is becoming - the wish to be anything other than what you are - there is tension; wherever there is acceptance of what is, there is ease. This is the structural law these techniques work with: tension is the form 'A wants to become B' takes inside you, and it dissolves the moment becoming dissolves.",
            "Osho then turns this into a question of inner economy. The desiring mind moves on and on; whatever it gets, it immediately devalues, and this perpetual hunger Buddha called trishna. To cut trishna is not to suppress desire but to accept what is so totally that the engine of becoming runs out of fuel. The techniques in this chapter are devices for that acceptance. They do not give you a new identity to wear; they let the swinging stop, so that the centre - which has always been there - can become felt as the actual ground of your being.",
        ],
        "quotes": [
            "The normal man is really a dead man, living between these two points.",
            "If there is no becoming, how can there be any tension? Tension means you want to be something else which you are not.",
            "Whatsoever you are, if you accept it in its totality, becoming ceases.",
        ],
    },

    # ──────────────────────────────────────────────────────────────────
    # Chapter 9 — Techniques for Centering
    # ──────────────────────────────────────────────────────────────────
    {
        "chapter": 9,
        "title": "Techniques for Centering",
        "paragraphs": [
            "Osho begins with a flat distinction: man is born with a centre, but not with the knowledge of the centre. Existence cannot be without it - the centre is the link, the root, the place where you are tied into the universe - but knowledge of it has to be gained. Without that knowledge, life is technically functional and existentially rootless: you drift, you postpone, you wait for death without ever having been quite alive. This frustration, he says, follows you like a shadow, and no external success can lift it because it is structural.",
            "He uses Sartre's word for the unrooted condition - thrownness. If you experience yourself as having been hurled into a foreign universe, anguish must follow, because the part can never win against the whole. Religion, for Osho, is not a set of beliefs but the inverse experience: not thrown but grown, an organic part of existence rather than a stranger to it. The same universe that feels alien to a thrown self feels like home to a grown self, and the difference between anguish and bliss is exactly the difference between these two postures.",
            "He then traces the displacement of the centre developmentally. A child is first rooted in the navel - the hara, what the Japanese still recognise in the term hara-kiri, the killing of the hara - and you can see it in any infant whose belly rises and falls with the breath. As the child grows he develops a second centre at the heart, dependent on whether love is given to him; if it is not, the heart-centre simply fails to grow, and the adult can never afterwards truly love, no matter how much he talks of it. From the heart, awareness drifts further still into the head, and the original ground is forgotten. We have all, Osho says, in this displaced sense, committed hara-kiri.",
            "These centering sutras are devices to take consciousness back. They do not ask you to acquire something new but to recover something that was always your basic nature. Only an animal, or a tree, can be unaware of its roots without consequence; the human capacity for self-awareness means that when the roots are forgotten, fear and dread and death-anxiety become the daily weather. Recognition, however, can be cultivated, and once cultivated it produces what Osho calls the only real bliss: the felt unity of an organic part with its whole.",
        ],
        "quotes": [
            "Bliss is the result of an organic unity with the universe, and anguish the result of an enmity.",
            "You are not alone, you are not atomic, you are part of this cosmic whole.",
            "Man as an outsider in the universe is bound to feel deep anxiety, dread, fear, anguish.",
        ],
    },

    # ──────────────────────────────────────────────────────────────────
    # Chapter 11 — Techniques to Penetrate the Inner
    # ──────────────────────────────────────────────────────────────────
    {
        "chapter": 11,
        "title": "Techniques to Penetrate the Inner",
        "paragraphs": [
            "Osho's diagnosis here is unusually severe. Most human beings, he says, are not so much off-centre as actually centreless - a circle whose circumference exists but whose inside has never been entered. The trouble is not that we have a poor relationship to our interior; it is that for us the word interior has no real referent at all. We use it intellectually, we repeat the spiritual phrases, but the meaning behind the words has not been earned by any actual experience.",
            "This is not solved by being alone. Even when no one is physically present, the mind continues to populate itself with the images, voices and judgements of others, and so we remain inwardly crowded. Even sleep does not deliver us - in dreams we are still rehearsing the outside world; only in deep dreamless sleep do we drop into the centre, and there we are unconscious. So the entire span of our conscious life is spent on the circumference, and the only place where our consciousness has actually been within is a place we cannot remember.",
            "Because life can only be known at the centre, life lived only at the circumference is necessarily lukewarm. We register that we exist - we say 'I am' and feel it is enough - but we never reach intensity. And, Osho adds, an inauthentic life produces an inauthentic death: the one who has not really lived cannot really die. Death will arrive as one more accident on the periphery of someone who was never quite there to be subtracted.",
            "Three techniques follow from this analysis. One closes the senses with the hands so that even the bodily exits to the outside world are sealed. One drops attention from the head into the heart. One lets the mind hover in the gap between two opposites without taking either side. They are different in form, but their function is the same: each is a device to pierce the crowded circumference and finally let consciousness fall to where the centre actually is. Until that happens, Osho warns, all talk of going within is words about words.",
        ],
        "quotes": [
            "Man is as if he is a circle without a centre.",
            "When you are conscious you are never within, and when you are within in deep sleep you become unconscious.",
            "One who has not really lived cannot really die.",
        ],
    },

    # ──────────────────────────────────────────────────────────────────
    # Chapter 13 — Inner Centering
    # ──────────────────────────────────────────────────────────────────
    {
        "chapter": 13,
        "title": "Inner Centering",
        "paragraphs": [
            "Osho opens by sketching the body as a two-dimensional mechanism. Through the senses, consciousness reaches outward and meets what we call matter; through centering, the same consciousness moves inward and meets what we then call non-matter. There is, in his view, no real division at the level of reality - it is a single x - but the two directions of approach show that reality under two completely different aspects, and Tantra is interested in cultivating the second.",
            "The seer, he insists, is never in the senses themselves; the senses are only openings. Eyes are not what see, they are what is seen through. You can verify this by closing your eyes and noticing that vision continues - dreams, images, scenes. Once that point lands, the entire problem of meditation can be redescribed: it is the gathering of this seer back from its various sensory exits into itself. Centering, in the Tantra sense, means not the absence of activity but the convergence of consciousness into a single undivided point that has no direction at all.",
            "But here Osho introduces the chapter's pivotal warning: the centre cannot be approached head-on. The very phrase 'how to remain in' is itself an outward movement, because thinking about the inner is still thinking, and every thought is a cloud that has drifted in from outside. To you, structurally, belongs only sky-like consciousness without clouds, but you cannot reach it by issuing thoughts at it. Devices and techniques exist precisely because the direct route does not work.",
            "The principle is the same as happiness in play, music or absorbing work: it is always a by-product. If you play in order to be happy, the play is poisoned; if you become totally the play, happiness arrives unsought. So the techniques that follow do not tell you to seek the centre. They ask you to look lovingly at an object, to sit with awareness in the buttocks, to sway gently, and they then let the centre arrive on its own. The mind must remain occupied with the technique, not with the result, and what is most subtle and most eternal will only appear when grabbing for it has been given up.",
        ],
        "quotes": [
            "Whatsoever is beautiful, whatsoever is eternal is so delicate that if you try to grab it directly it is destroyed.",
            "The seer is behind the senses. He moves through the senses to the world.",
            "Bliss is a by-product, you cannot grab it directly.",
        ],
    },

    # ──────────────────────────────────────────────────────────────────
    # Chapter 15 — Seeing the Past as a Dream
    # ──────────────────────────────────────────────────────────────────
    {
        "chapter": 15,
        "title": "Seeing the Past as a Dream",
        "paragraphs": [
            "Osho borrows from Gurdjieff a single, unsparing diagnostic - identification is the only real sin - and the tenth centering sutra is constructed to attack it directly. Identification, in Osho's reading, is not a moral failing but a structural confusion: you were a child once and are no longer, yet whenever you remember childhood you do not see it from outside, you fall back into it. Memory is not run as a film; it is re-inhabited. The same blurring happens with every later phase, until the stratified past has become indistinguishable from the present self.",
            "The technical move he proposes is therefore to begin with the past, where the gap is widest and the witnessing easiest. If you can see your childhood as a dream - as a sequence of images that happened to someone, but to which you can stand back as observer - something quietly extraordinary follows: you suddenly notice that the present moment, too, is on its way to becoming a dream tomorrow. Future, present and past all turn out to be inside time, while the witness that registers them is not. Witnessing consciousness, Osho insists, is itself never past and never future.",
            "He uses night dreams to make the structural point. Inside a dream you cannot recognise that it is a dream; only on waking, with the gap of distance restored, do you see it. The past is in the same situation - you wake out of it the moment you can stand far enough away to look at it. Children confuse dreamed toys with real ones; adults wake from a nightmare with the heart still racing; in both cases the dream felt absolutely real until separation was achieved. So when Shankara and Nagarjuna call the world maya, illusion, they are not denying that it is happening. They are saying that anything that can be witnessed becomes dreamlike to the witness.",
            "Osho then turns to Rousseau's Confessions as the cautionary case. Rousseau wrote what he believed was the most fearless self-exposure in literature, confessing every sin without flinching - and yet, Osho says, the deepest sin remained, because Rousseau was identified with every confession he made. The confessions made his ego stronger; his sins, too, became ornaments. What he never confessed was the very fact of his identification. That is the sin these techniques target. Liberation begins not when you change what you do but when you stop being what you do - when life, including its sins and virtues, becomes something witnessed rather than inhabited.",
        ],
        "quotes": [
            "Anything that you can look at as a witness is a dream.",
            "Identification is misery; non-identification is bliss.",
            "Your witnessing consciousness is eternal; it is not part of time.",
        ],
    },

    # ──────────────────────────────────────────────────────────────────
    # Chapter 17 — Several Stop Techniques
    # ──────────────────────────────────────────────────────────────────
    {
        "chapter": 17,
        "title": "Several Stop Techniques",
        "paragraphs": [
            "Osho prefaces this chapter by drawing a sharp line between two registers of human existence: being and doing. Being is your nature - it is already the case, you do not possess it because you are it. Doing is achievement: it produces what you have, and what you have piles up around being like a circumference around a centre. Most lives, Osho says, are lived entirely on that circumference. We accumulate possessions, accumulate roles, accumulate accomplishments, and end up identifying so completely with the periphery that the centre becomes a rumour rather than a location.",
            "The mistake to dismantle, then, is the conflation of having and doing with being. Whatever you have - money, knowledge, prestige, even sainthood - you can have or not have, and so it cannot be you. Whatever you do - run, laugh, steal, meditate - you can equally do or not do, and so it cannot be you either. Action is always a choice; being is the chooser, and the chooser cannot in turn be chosen. A saint can become a thief and a thief can become a saint, but in both transformations something underneath remains untouched: that something is what these sutras aim to expose.",
            "The 'stop' techniques attack the periphery directly. Gurdjieff borrowed them, Osho says, from Tibetan lamas who in turn took them from Vigyan Bhairav: in the middle of an ordinary movement - dancing, walking, gesturing - you simply freeze. The body still has momentum, the action still wants to complete itself, but you do not co-operate. In that imposed gap the doer and the watcher inside the doer split apart, and for an instant you actually see yourself from a position that is not your activity. The smallest cheat - rebalancing, finishing the gesture, easing into a pose - dissolves the gap and ruins the experiment.",
            "What is at stake here, Osho stresses, is not better behaviour but a different ontology of self. Until you have caught the centre directly, the circumference is hell - a hell of perpetual misery, anguish and suffering generated by clinging to what is not you as if it were. Once the centre is realised, the same circumference is harmless; you can act and possess without being eaten by your activities and possessions. The 'stop' is a precise instrument designed to produce that realisation in a moment small enough to slip past the mind's defences.",
        ],
        "quotes": [
            "Whatsoever you have is not your being, and whatsoever you do is not your being.",
            "The being is the chooser, not the chosen, and you cannot choose the chooser.",
            "The circumference is the hell. These techniques are the means to enter into this center.",
        ],
    },

    # ──────────────────────────────────────────────────────────────────
    # Chapter 19 — A Technique for the Intellectual and a Technique for the Feeling Type
    # ──────────────────────────────────────────────────────────────────
    {
        "chapter": 19,
        "title": "A Technique for the Intellectual and a Technique for the Feeling Type",
        "paragraphs": [
            "Tantra's diagnosis here, Osho says, is more radical than anything Western psychology will recognise: it is not that the mind is sometimes ill, it is that the mind itself is the illness. If the mind is the illness, then the entire project of curing the mind from within the mind is structurally hopeless. Sickness cannot rearrange itself into health; it can only be transcended. That single shift in framing is what separates Eastern Tantra and Yoga from the dominant therapeutic models of the West.",
            "Western psychology, born in clinics and case-files, takes the average mind to be healthy and intervenes only when an individual deviates from the average - usually by readjusting the deviator back to that norm. But the average mind, Osho insists, is itself 'normally ill'. Its illness is so commonly distributed that it becomes invisible; we mistake the statistical mean for the standard of health. So the standard treatment can at best return a patient from being abnormally ill to being normally ill, which is no real recovery at all.",
            "He then deepens the point through a long analogy with the body. The body, because it is always dying, can never be perfectly healthy - only relatively healthy. Health is a movement, not a state; even the most vigorous body is permanently leaking toward decay. The mind sits in a structurally similar place, suspended between matter and spirit, between the dying and the deathless, so it is bound to be tense. Treating its tension as a removable symptom misses the fact that the bridge itself is what tenses; you cannot heal a bridge into solid ground.",
            "The conclusion is severe but clarifying. Curing the mind from inside the mind is impossible; the only therapeutic move is transcendence - stepping out of the mind altogether and letting it become an object you observe rather than the place you live. The two techniques in this chapter, one for the intellectual type and one for the feeling type, are precisely calibrated to that exit. They do not improve the mind. They give the witness behind the mind enough leverage to become aware of itself, and from that vantage the entire problem of mental illness reorganises itself.",
        ],
        "quotes": [
            "It is not that you are tense within, but rather, you are the tension.",
            "If the mind is ill then the illness can be treated, but if the mind itself is the illness, then this illness cannot be treated. It can be transcended.",
            "Mind is just a fragment of your body; it cannot control it.",
        ],
    },

    # ──────────────────────────────────────────────────────────────────
    # Chapter 21 — Three Looking Techniques
    # ──────────────────────────────────────────────────────────────────
    {
        "chapter": 21,
        "title": "Three Looking Techniques",
        "paragraphs": [
            "Before introducing these three sutras, Osho lingers on the eyes themselves, because every technique in the chapter depends on a particular fact about them. Of all parts of the body, the eyes are the least bodily. They are still material, but matter has come closer to non-matter in them than anywhere else, and for that reason the distance between you and your body is shortest at the eyes. From the hand, from the heart, the inner journey is long; from the eyes, a single jump can land you at the source.",
            "This is also why eyes are the site of an inadvertent inwardness even in everyday life. When two people look directly into each other's eyes for more than a few seconds, one of them feels trespassed, because the look has reached past the body into the person. Only in deep love is sustained eye contact welcome - love is by definition the consent to be entered. Conversely, the face of a blind person carries a peculiar deadness, not from the absence of seeing but from the absence of this leakage of inwardness through the eyes; the doors are sealed, and the face loses its lit-from-within quality.",
            "Osho then makes a more clinical point: eye movement and thought movement are coupled. REM sleep registers dreaming because the eyes follow the dream the way they would follow a film; in waking life, every internal movement of thought is accompanied by a corresponding micro-motion of the eyes. This is mechanical and non-voluntary. You cannot keep a secret in your eyes the way you can in your speech, because the eyes are not under conscious command; the pupils dilate, the gaze shifts, the truth leaks. The practical implication is the inverse: still the eyes precisely and you still the thought process, because the link runs both ways.",
            "The three sutras that follow exploit this exact bridge. Closing the eyes to see the inner being in detail uses the bridge inward. Looking at a bowl while ignoring its sides and material uses the bridge to suspend the differentiating mind. Seeing an ordinary face as if for the first time uses the bridge to dismantle accumulated knowing. In each case the technique is not really about what you look at; it is about the quality of the looking. A single quiet jump from this most non-bodily of organs can take you all the way home.",
        ],
        "quotes": [
            "A single jump from the eyes can lead you to the source.",
            "Eye movements and thinking are joined together.",
            "Eyes are the meeting point of you and your body. Nowhere else in the body is the meeting so deep.",
        ],
    },

    # ──────────────────────────────────────────────────────────────────
    # Chapter 23 — Several More Looking Methods
    # ──────────────────────────────────────────────────────────────────
    {
        "chapter": 23,
        "title": "Several More Looking Methods",
        "paragraphs": [
            "Osho draws a clean three-part diagram before these sutras: consciousness sits at the centre, the senses sit on the boundary, and objects lie beyond the boundary. The senses are doors that open both ways. Through them, consciousness can move outward to the world or inward to itself, and structurally the distance is the same. We feel that nirvana is far and the world is near only because we have been in continuous outward traffic for so long. Quoting the Zen master Bokuju, Osho insists that the marketplace and the kingdom are no further apart than two opposite turnings of the same door.",
            "Why, then, does consciousness flow outward by default? Because the body has needs - food, water, shelter - that can only be satisfied in the world of objects, and consciousness is naturally pulled along the route by which the most pressing needs are met. A child reaches first for the mother, but really for the food; love is initially a shadow of feeding, which is why bottle-fed children, in Osho's view, attach less to the mother. We do not move outward because we are sinful; we move outward because outward is where the immediate biology of survival has always been answered.",
            "It follows that the inward movement does not happen on its own. A new need has to be created, a need that cannot be satisfied outside, and Osho says this need is born from one specific recognition: the awareness of one's own death. Animals see other animals die, but cannot apply the fact to themselves; for them, death is always something happening to someone else. Only a human being can see his own death as a fact at the centre of his life, and only that recognition is strong enough to reverse the long-trained outward flow of consciousness.",
            "This is why younger societies tend to be irreligious and older ones tend to be religious; it has nothing to do with intelligence or virtue and everything to do with whether death has become a concern at the centre or remains an event at the periphery. The point, Osho is careful to add, is not to become afraid of death - fear is not awareness - but to take its approach seriously enough that you begin to look back into yourself before there is no longer time to. The looking techniques in this chapter all rely on that prior turn; without it, the same techniques become exercises rather than doorways.",
        ],
        "quotes": [
            "If you are not aware of death, you have not yet become man.",
            "From the senses, doors open both ways - move to the objects or move to the centre. The distance is the same.",
            "Unless you create a need which can only be fulfilled when you move inward, you will never move inward.",
        ],
    },

    # ──────────────────────────────────────────────────────────────────
    # Chapter 25 — From Words to Pure Words to Being
    # ──────────────────────────────────────────────────────────────────
    {
        "chapter": 25,
        "title": "From Words to Pure Words to Being",
        "paragraphs": [
            "Osho opens by pointing out that Sartre titled his autobiography simply Words - and that, he says, is the autobiography of every human being. From morning to night, asleep or awake, we are saturated with words; even our dreams are subtitled. The self, however, does not live inside the verbal apparatus. It exists below it, behind it, around it, but never inside it. The fundamental error, the source from which every misery follows, is identification: we believe we are the mind, and that single misperception structures the whole field of human suffering.",
            "Why does this identification go so deep? Because thinking has been, in evolutionary and historical terms, the human survival weapon. Against animals, against the elements, against other people, the mind is the apparatus by which we have outmanoeuvred everything more powerful than us. A keen mind wins in negotiations, in business, in politics, in love. The mind has done so much for us that we have come to feel that we owe ourselves to it - and so to disidentify from it feels almost ungrateful, almost dangerous.",
            "The proof of this identification is, for Osho, embarrassingly easy to demonstrate. Tell someone their body is ill and they shrug; they regard the body as a vehicle they happen to possess. Tell someone their mind is ill and they take instant offence, because the mind is not something they have - it is something they take themselves to be. With the body, you are the master; with the mind, you are the slave who has never noticed the chain. The whole asceticism that has plagued religion, Osho argues, follows from this asymmetry: the mind, in trying to rule a body it cannot actually rule, ends up declaring war on it.",
            "These sound techniques begin to unhook us from words. The mind operates as a generator of internal speech, and silence is therefore not the absence of external sound but the loosening of that internal apparatus. Osho is careful to note the structural irony: even meditation can become an endless verbal commentary about meditation. The techniques in this chapter use sound, and then pure sound, and then the inward arc beneath sound, to walk the practitioner backwards from words into the wordless ground of being on which words have always depended.",
        ],
        "quotes": [
            "You are filled with words, and this process of words continues the whole day, even in the mind.",
            "With the body, you are the master. With the mind, you are the mind.",
            "Mind has been your protection, your security. So obviously we think of ourselves as mind.",
        ],
    },

    # ──────────────────────────────────────────────────────────────────
    # Chapter 27 — Soundlessness, Soundfulness and Total Awareness
    # ──────────────────────────────────────────────────────────────────
    {
        "chapter": 27,
        "title": "Soundlessness, Soundfulness and Total Awareness",
        "paragraphs": [
            "Osho threads modern physics into the framing for these chants. He notes that physicists have lately been forced to postulate anti-matter - a hole of nothingness in space that exists as the opposite face of every dense object - and observes that Tantra has always said the same thing about sound. Behind every sound is anti-sound: silence. The two are not separate phenomena that happen to be near one another; they are two aspects of one coin, and neither could occur without the other. The sutras to follow take this metaphysical fact as their working principle.",
            "Mind, in this register, is sound; meditation is the silence on its other side. To analyse mind is to find it built out of sound and word and thought; to enter no-mind is to step into the silence that has always been the underside of that noise. Zen masters call this the state of no-mind, and Osho is careful to point out that it is not arrived at by suppression. The silence is already there, just behind every utterance, the way the silence of a forest is just behind a single bird's call.",
            "He then surveys two opposed schools on how to cross from sound to silence. The first - exemplified by Sankhya philosophy and, in our own time, by J. Krishnamurti - holds that the mind cannot be used at all. Any technique uses the mind, and using the mind only strengthens it; the only honest move is therefore to drop technique entirely and see directly. The second - taken by Yoga and Tantra - replies that even understanding this argument is itself an act of mind, so mind cannot simply be abandoned. The viable strategy is to use mind against itself: not positively, to reinforce, but negatively, to weaken. Technique becomes a springboard from which mind takes a deliberate jump beyond itself.",
            "These chants of 'Aum' - and the soundlessness, soundfulness and total awareness sutras built around them - work on the second principle. You use sound as the rope by which you pull yourself across the thin gap into silence. The technique is precise because the gap is precise; press into the chant fully and you find that just behind it is the silence that was never absent, only unnoticed. Osho frames this whole chapter as a permission slip: the mind is not the enemy here, it is the jumping board, and these methods will only fail if you refuse to use what you have.",
        ],
        "quotes": [
            "Wherever there is sound, just behind it there is silence.",
            "Mind has to be used as a jumping board, and from that jumping board you can have a plunge into the no-mind.",
            "Mind is the word; meditation is no-mind.",
        ],
    },

    # ──────────────────────────────────────────────────────────────────
    # Chapter 29 — Methods for the Dropping of Mind
    # ──────────────────────────────────────────────────────────────────
    {
        "chapter": 29,
        "title": "Methods for the Dropping of Mind",
        "paragraphs": [
            "Tantra, Osho says, refuses the religious split between this world (sansara) and liberation (moksha). For most traditions, this world is something you have to fight your way out of in order to reach the divine; for Tantra, the divine is hidden inside the immediate, here and now, not somewhere else and later. The two are not contradictory points but two dimensions of one existence, and the apparent doubleness comes not from reality but from the limits of our knowing. The whole appears as two only because we have not yet seen it whole.",
            "The trouble is that the mind cannot help making such divisions. Mind, Osho says, works like a prism: a single ray entering it comes out as seven colours, and it cannot do otherwise - dividing is what it is. Reality is whole, but the moment the mind takes hold of it, it cuts. What is needed for perceiving wholeness is therefore not a more refined analysis but a different organ altogether: synthesis rather than analysis, no-mind rather than mind. The methods in this chapter are designed precisely to drop the prism, not to repolish it.",
            "Because Tantra denies the sin/liberation split at the root, total acceptance becomes possible, and that acceptance is what genuine relaxation rests on. Religions that brand the world or the body as sinful manufacture exactly the inner division they claim to heal: condemn the outer and you condemn yourself in parallel, because you are part of what you have condemned. The result is guilt, neurosis, dead seriousness. Osho contends that every religion has both an outer life-denying face and an inner esoteric core, and that whenever the inner core is healthy, it is invariably tantric in this acceptance.",
            "Out of acceptance, in this view, comes everything else: relaxation, joy, lightness, the capacity to laugh and play. The neurotic seriousness of the conventionally religious is the diagnostic mark of an unaccepted reality. Tantra is not less serious, but it has nothing to fight against; the world is already the divine, only the eyes need opening. The dropping-of-mind techniques in this chapter take that metaphysical permission and turn it into a practical instruction: stop dividing, stop condemning, stop becoming - and let what is already the case be what it is.",
        ],
        "quotes": [
            "Unless you accept the world totally, you cannot be at ease within.",
            "Mind works like a prism. It goes on dividing things into fragments.",
            "This sansara is the moksha. This very world is divine, this very world is the ultimate.",
        ],
    },

    # ──────────────────────────────────────────────────────────────────
    # Chapter 31 — From Sound to Inner Silence
    # ──────────────────────────────────────────────────────────────────
    {
        "chapter": 31,
        "title": "From Sound to Inner Silence",
        "paragraphs": [
            "Osho sharpens, here, the difference between three modes of inquiry that are usually run together. Philosophy thinks about ultimate truth; science discovers what is. Tantra is also a science, but its territory is the inner - it conducts a subjective experiment rather than an external speculation. The very word tantra, he reminds the reader, means technique, and so the book in his hands is not a doctrine at all but a hundred and twelve experiments. There is nothing here to argue about; there is only something to try.",
            "The cutting line between the three is whether they require an experimenter. Philosophy operates without one - it speculates about the ultimate from the comfort of armchairs and never lands. Science requires an experimenter and an apparatus, and so reaches answers, but its experimenter and his apparatus are both outside himself. Religion, properly understood, is the deeper science: the experimenter and the experiment are the same person. Whatever conclusions arise are written into your own being rather than printed in a journal.",
            "Osho then presses the warning that follows from this. The ultimate is hidden inside the immediate, and the moment you reach past the immediate to chase the ultimate you lose both at once. Philosophy, he says, is the discipline of asking puzzles while you are dying - and to make the point unmistakable he tells the joke of a priest leaning over Mulla Nasruddin's deathbed to interrogate him about the Trinity. The dying man laughs: I am dying and he is asking me puzzles. That is the position of every philosophy in the face of an actual life.",
            "The corrective Osho offers is purely practical. Do not read about meditation; do it. Do not turn the no-mind into a topic to think about; the mind is delighted to convert any subject - even meditation, even silence - into one more object of mental commentary. These sound techniques work only if they are entered as experiments rather than considered as doctrines. Tantra simply hands you a technique and lets you find the ultimate inside the immediate, where it has always been waiting.",
        ],
        "quotes": [
            "All philosophy is like this: it is asking puzzles while you are dying.",
            "The very word tantra means technique.",
            "Life's problems can be solved only when you become deeply rooted in existence.",
        ],
    },

    # ──────────────────────────────────────────────────────────────────
    # Chapter 33 — The Spirituality of the Tantric Sex Act
    # ──────────────────────────────────────────────────────────────────
    {
        "chapter": 33,
        "title": "The Spirituality of the Tantric Sex Act",
        "paragraphs": [
            "Freud said man is born neurotic. Osho calls this only half the truth. Man is not born neurotic, he is born real, with feeling intact - it is society that drives the split. The newborn is a feeling being, undivided, more like a tree or an animal in his immediate contact with the real. But to be loved by parents and teachers he has to suppress what he feels and behave according to a code, and slowly the feeling self is buried beneath the thinking self until the two become strangers.",
            "The damage of this split is that we lose contact with our authentic needs. Real needs, Osho says, can only be sensed by the feeling centre; the thinking centre invents and pursues symbolic substitutes. The need is for love, but the symbol becomes food, so we stuff ourselves and never feel filled. The need is for love, but the symbol becomes the attention of crowds, so we become political leaders and never feel met. Because the symbolic need is not the real need, no amount of fulfilment fulfils it, and we spend lifetimes refining a hunger that cannot be satisfied because it is the wrong hunger.",
            "Even our love, in this state, is head-talk. Saying 'I love you' is for most people a fragment of thought issuing a promise that the rest of the being has no idea how to keep. Sartre's complaint that every promise is bound to be false applies here precisely: a fragment cannot promise on behalf of a whole that is not present. Hypocrisy then enters as a structural inevitability rather than a moral failing - we pretend to fulfil what was given by a part that has since left the throne.",
            "Tantra's intervention is to put the person back together, and these sutras - including the famous one on sex - are instruments of that reunion. Sex, properly approached, is one of the very few situations in ordinary life where thinking is dropped and feeling momentarily takes over the whole organism, and that is why Tantra treats it not as a temptation to be overcome but as a doorway to be entered consciously. Each sutra in this chapter is calibrated to return the practitioner to the feeling centre, where the original undivided self is still waiting beneath the imposed code.",
        ],
        "quotes": [
            "Even when you say that you feel, you only think that you feel.",
            "A feeling is of the whole - your whole body, mind, everything you are, is involved.",
            "Tantra says, fall down deep within to the feeling centre.",
        ],
    },

    # ──────────────────────────────────────────────────────────────────
    # Chapter 35 — Turning Inward toward the Real
    # ──────────────────────────────────────────────────────────────────
    {
        "chapter": 35,
        "title": "Turning Inward toward the Real",
        "paragraphs": [
            "Osho opens this set with a striking diagnosis: civilisation is, in its operational core, a training in becoming unreal. Tantra is the reverse process - either preventing the unreality from being installed, or, if it has already been installed, helping you contact the real that is still hidden underneath. The first move is simply to see how the unreality is produced, because the very seeing is itself a mutation; understanding here is not preparation for change but is change.",
            "The child, he insists, is born undivided. He is not body and mind, he is body-mind - two aspects of one being, not two parts in negotiation. Education, conditioning, culture all begin by imposing the division, and once the division is in, identification follows automatically with the thinking side. The thinking process, which is structurally peripheral - you can exist without it in deep sleep, in deep meditation, in unconsciousness - is treated as the centre, while the body becomes the slave it is now obliged to manage. From that misalignment, every neurosis arises.",
            "Osho then dismantles a commonsense assumption with a startlingly simple question: where does your body actually end? At the skin? But if the sun stopped tomorrow, you would die today. The plant that opens at sunrise and closes at sunset is, in a real sense, the sun's body extended into petals. You inhale and exhale the atmosphere every few seconds; without it you stop in moments. By any consistent definition, your body has no fixed boundary - it stretches to the limits of the universe. The 'I-end-at-my-skin' picture is a useful fiction for a head-centred identity that has forgotten where it actually lives.",
            "These four sutras work to dissolve that head-centred identity. They aim to make you, in Osho's striking phrase, headless - uncentred, everywhere and nowhere - so that the body-spread that you actually are can be felt directly. Identification with thinking is what makes us false, because thinking deals in words and the word love is not love, the word God is not God. Tantra's whole effort here is to walk you back from the verbal periphery into the bodily wholeness that is, in the end, indistinguishable from existence itself.",
        ],
        "quotes": [
            "Civilization is a training in how to become unreal.",
            "Where does your body really end? There is no limit.",
            "Body and mind are two aspects of his being, not two divisions.",
        ],
    },

    # ──────────────────────────────────────────────────────────────────
    # Chapter 37 — Techniques to Witness the Flux-like Film of Life
    # ──────────────────────────────────────────────────────────────────
    {
        "chapter": 37,
        "title": "Techniques to Witness the Flux-like Film of Life",
        "paragraphs": [
            "Osho opens with the central image of the chapter: the original mind is a mirror, always pure, but covered with dust gathered through many lifetimes of travel. The purity is structural, never lost, never even capable of being lost - because if it could be lost, no method would be able to recover it. What we ordinarily call 'mind' is therefore the original mind plus a thick coating of dust, and every technique in this chapter is a way of cleaning the mirror so that what is already there can begin to reflect.",
            "He then draws a sharp line between East and West on this question. Christianity holds that something has happened to being itself - sin - and so the human being is, at some metaphysical level, damaged and condemned. The Eastern view is that nothing has happened to being itself; nothing can. The being remains in its absolute purity, untouched by anything you have ever done or thought. There has been no sin, only a false identification with the dust. You are not condemned, only confused about which layer is you.",
            "The key inversion follows: knowing is your purity, knowledge is dust. The capacity to know is the original nature; what you know - your memories, your experiences, your accumulated past - is the residue collecting on the surface. We mistake this residue for ourselves because it is what we can speak about, point to, accumulate. The pure knowing that is doing the speaking and pointing remains invisible to itself, like an eye trying to see itself by looking harder.",
            "Osho cites Buddha as the structural example. Buddha left every teacher who promised liberation in some future state, because he was interested in the here and now, where the dust is actually being noticed. He found it not by acquiring more knowledge but by simply staying in the present moment, the only place where consciousness can register itself directly. These four techniques work the same way - each is a different angle on the same wiping action. They are not mechanical, however; used mechanically they will produce only a cultivated stillness that is itself dust. Used with understanding, they uncover what was never covered to begin with.",
        ],
        "quotes": [
            "Knowing is your purity, knowledge is dust.",
            "The original mind is like a mirror - it is pure, and it remains pure, but dust can gather upon it.",
            "All your knowledge is dust. The capacity to know, the energy to know, is your original nature.",
        ],
    },

    # ──────────────────────────────────────────────────────────────────
    # Chapter 39 — From the Wave to the Cosmic Ocean
    # ──────────────────────────────────────────────────────────────────
    {
        "chapter": 39,
        "title": "From the Wave to the Cosmic Ocean",
        "paragraphs": [
            "Quoting Sri Aurobindo - 'the whole life is yoga' - Osho insists that meditation cannot be a part-time activity. Either it has happened to you and now pervades everything you do, or it has not happened at all. You cannot meditate for an hour in the morning and then live mechanically for the remaining twenty-three; that is not meditation, only an exercise. Meditation is a quality of being rather than an item on a schedule, and the moment it becomes a slot in your day you have already misunderstood it.",
            "He compares it to a second breathing. Just as you breathe air without effort whether walking, sitting or sleeping, you start breathing consciousness once meditation has truly arrived. The breathing of consciousness is not a metaphor for him - he says so explicitly - but a literal additional respiration that, once started, continues regardless of activity. It places you, in effect, in a different dimension; the same body now lives in a wider field, and the question of whether you are 'doing meditation' becomes meaningless.",
            "From this it follows that any act, properly entered, can be the doorway. Hills meditate, stars meditate, the earth itself meditates; you can join from anywhere. He gives examples: Kabir kept on weaving even after enlightenment, because the weaving was where his meditation had taken root; the potter Gora let his pots emerge on the wheel as he himself emerged on the inner wheel - one external centring, one invisible centring, both happening in the same hands. The act, in each case, is irrelevant. What matters is the quality of consciousness brought to it.",
            "The three sutras of this chapter therefore turn quite ordinary moments - wandering attention, the flicker of sensory clarity, the universe's own pulse - into doorways. They do not require special places, special hours or special postures, because the move they ask for is not topological but qualitative. Once it lands, walking down a street and sitting in a temple are exactly the same depth; once it has not landed, no posture will rescue you.",
        ],
        "quotes": [
            "Either it is - and when it is you are wholly in it - or it is not.",
            "Meditation is an inner breathing.",
            "Meditation doesn't belong to the act; it belongs to the quality you bring to the act.",
        ],
    },

    # ──────────────────────────────────────────────────────────────────
    # Chapter 41 — Tantric Methods for Awareness and Non-Judgment
    # ──────────────────────────────────────────────────────────────────
    {
        "chapter": 41,
        "title": "Tantric Methods for Awareness and Non-Judgment",
        "paragraphs": [
            "Osho frames these eight techniques with a paradox: you have to attain what you already are. Nothing has been lost; you remain natural, pure, innocent - it is only that you have forgotten. The purity has not been disturbed and the innocence has not been destroyed. There is just a deep sleep over what has always been the case, and so the spiritual task is recovery rather than acquisition. This makes the work both very simple and very difficult: simple because the home is already where you are, difficult because what is most obvious is exactly what is hardest to notice.",
            "From this it follows that sansara and nirvana - the world and the liberated state - are not two places but two attitudes toward the same reality. The same world becomes nirvana not by exchanging it for a different world but by changing focus, emphasis, choice. Once the change of attitude lands, the old missing of it becomes incomprehensible, and Osho says any Buddha laughs when he arrives because he sees retrospectively that the entire search was searching for something that had never moved.",
            "The catch in receiving such methods, however, is the ego. The ego craves difficulty, because only difficulty offers it the trophy of conquest; anything easy is felt as an insult. So when a teacher describes practices that are simple and immediately available, the mind dismisses them as too easy to be effective and looks instead for some grander, more arduous path that will let it accumulate spiritual achievement. The very simplicity that makes these methods workable is what makes the ego refuse them.",
            "Osho is therefore careful to disable that refusal in advance. Spiritual awakening, he says, is not a causal event needing time. It is more like waking from sleep: a sudden alertness in which the place, the time and the identity that had become temporarily strange snap back into recognition. There is no cause that has to take place before the effect; there is only the alertness, and the moment alertness is sufficient, the recognition has already happened. These eight sutras are devices to cultivate exactly that growing alertness, and their simplicity is part of how they work, not a defect.",
        ],
        "quotes": [
            "You are already the person you long to be, you are already where you want to reach.",
            "Sansara and nirvana are not two things - just two attitudes, just two choices.",
            "Spiritual explosion is not caused by anything; it is not a causal phenomenon.",
        ],
    },

    # ──────────────────────────────────────────────────────────────────
    # Chapter 43 — Finding the Changeless through the Changing
    # ──────────────────────────────────────────────────────────────────
    {
        "chapter": 43,
        "title": "Finding the Changeless through the Changing",
        "paragraphs": [
            "Osho draws on Northrope to contrast two civilisational orientations of mind. The Western mind has hunted what Northrope called the theoretical component of existence - the causal structure by which nature can be predicted, controlled and turned to use. The Eastern mind has hunted the aesthetic component - how to participate in nature, how to dissolve into it, how to be in friendship rather than in conflict with what surrounds you. The same world produces two utterly different sets of questions depending on which orientation you bring to it.",
            "Pushed further, Osho calls science a relationship of hatred and religion a relationship of love. Science divides, chops, defines, measures, conquers; in this it is structurally aggressive, and Osho frames it as the masculine attitude. Religion synthesises, joins, dissolves boundaries; it is structurally receptive, the feminine attitude. Tantra, in his reading, is purely Eastern in this sense - a love effort, a participation, a way of becoming undifferentiated with what one is investigating.",
            "He gives the difference one of the chapter's sharpest concrete illustrations. When Hillary climbed Everest, the Western press reported that the mountain had been conquered. A Japanese Zen monastery's wall newspaper carried a single sentence: Everest has been befriended. The two reports describe the same event with two completely incompatible metaphysics. To approach existence as an opponent is to find in it only dead matter capable of yielding to force; to approach existence as a partner is to find in it the same life that you yourself are.",
            "From this comes the practical consequence that runs through these techniques. Tantra is not a way of analysing reality into its parts; it is a way of dissolving the analytical posture so that what was always one can be felt as one. To use these methods, one has to drop the conquest reflex, the chopping reflex, the framework in which everything is broken into manipulable pieces. Find the changeless through the changing means: stop fighting the change, become part of it, and the changeless that was always present underneath becomes simply the medium in which the change is happening.",
        ],
        "quotes": [
            "If you approach it through analysis, it appears material. If you approach it through participation, it appears as life.",
            "Science is a hatred, a relationship of hatred with nature. Religion is a love relationship.",
            "Mind cuts, divides, chops everything. Religion is a dissolving of boundaries.",
        ],
    },

    # ──────────────────────────────────────────────────────────────────
    # Chapter 45 — Remaining with the Real
    # ──────────────────────────────────────────────────────────────────
    {
        "chapter": 45,
        "title": "Remaining with the Real",
        "paragraphs": [
            "Osho opens with the question Hui-neng pressed on his disciples: you are alive, you are conscious - so why don't you know who you are? The reality is not far away; it is here, surrounding and saturating you on every side. You cannot miss it - and yet you do. So the more useful inquiry is not how to know yourself but how it is that you are succeeding, despite everything, in not knowing yourself. Some device must be in operation, some barrier you yourself have built; otherwise self-recognition would be automatic.",
            "The good news, he says, is that nothing positive has to be done. Knowing happens when the barrier is not; you cannot construct knowing through additional effort. You only have to see and dismantle what is in the way. And the barrier, in his diagnosis, is the dreaming mind - the past constantly stationed between you and the present, interpreting whatever the senses bring in before you are allowed to meet it directly. You are not actually hearing this sentence; you are hearing your own simultaneous commentary on it, which the mind, manufactured out of the past, has been generating since you were a child.",
            "Look at a flower and the word 'beautiful' steps in immediately - and at that instant the flower is gone, replaced by your category for the flower. Touch a face and the dream of the face arrives faster than the face itself. You live, in this sense, inside a perpetual translation of reality into the language of memory and desire, and the translation is so fast and so seamless that you mistake it for direct experience. Religious dreams are no exception: it is possible to dream very piously about Christ or Buddha or God and never come within reach of any of them.",
            "These two sutras - the hen mothering her chicks, the many suns reflected in water - are calibrated to interrupt the translation. They ask you to remain with what is, without past and without future, without comparing the now to a remembered then or a projected later. With less words there are fewer barriers; with no words there are no barriers, and reality is met face to face. The technique is not about thinking new thoughts about reality; it is about letting thoughts subside far enough that reality, which has been there the whole time, can finally arrive without commentary.",
        ],
        "quotes": [
            "You are not hearing me; you are hearing yourself, because simultaneously you are interpreting.",
            "Knowing happens when the barrier is not. You cannot make any positive effort for it.",
            "Don't allow your eyes to be filled with thoughts and dreams. Look directly, hear directly and touch directly.",
        ],
    },

    # ──────────────────────────────────────────────────────────────────
    # Chapter 47 — Tantric Meditation Using Light
    # ──────────────────────────────────────────────────────────────────
    {
        "chapter": 47,
        "title": "Tantric Meditation Using Light",
        "paragraphs": [
            "Before turning to these light techniques, Osho redraws the map of human possibility. There are, he says, three kinds of people, not two: the normal, the abnormal and the supernormal. Western psychology, born in the clinic, has only ever studied the abnormal - those who have fallen below the norm - and it has built its entire portrait of the human being out of that material. Freud, Adler and Jung treated patients, never Buddhas, and so the very concept of a Buddha becomes impossible inside their framework: such a person can only be myth or fiction.",
            "Eastern psychology, particularly Tantra and Yoga, watches a different population. It studies those who have gone above the norm - Buddha, Patanjali, Shankara, Nagarjuna, Kabir, Nanak - and builds its image of the human being out of what such people demonstrate is possible. Both populations deviate from the average, but they deviate in opposite directions; one is below the norm and ill, the other is above the norm and exceptionally well. Calling them both 'abnormal' obscures everything that matters.",
            "The consequence of choosing one or the other as the basis of psychology is decisive. If you take the abnormal as your reference and build your image of man around illness, the whole society collapses inward into pathology; what is offered as health is only a return to the average, which is itself a milder form of disease. If you take the supernormal as your reference, growth becomes structurally possible, because someone has already actualised the possibility you are reaching toward. The map of what a human being might become widens rather than contracts.",
            "Tantra is committed to the upward map, and these three sutras - light rising along the spine, lightning between centres, the cosmos seen as translucent presence - belong to that ascent. Osho ties this directly to Maslow's notion of self-actualisation: outer success is meaningless if the inner potentiality remains unactualised, and people who have everything by external measures still come to him with the bewildered sense that they have failed at the only assignment that mattered. These light techniques are tools for the assignment that everything else has been a distraction from.",
        ],
        "quotes": [
            "One who is supernormal is abnormal because he is more healthy than any normal human being.",
            "Whatsoever you are is not the end. You are just in the middle. You can fall down, you can rise up.",
            "You succeed in everyone's eyes except your own.",
        ],
    },

    # ──────────────────────────────────────────────────────────────────
    # Chapter 49 — Conscious Doing
    # ──────────────────────────────────────────────────────────────────
    {
        "chapter": 49,
        "title": "Conscious Doing",
        "paragraphs": [
            "Osho opens with a piercing observation that he repeats in many forms throughout this chapter: when he looks into people's eyes, no one is really there - they exist absently. The body is functioning, the personality is responding, the life is being lived, but the centre of presence behind it all is missing. This absence, he insists, is the structural source of every kind of human suffering. You can be alive without being present, and once you notice the difference, the entire question of what to do becomes secondary.",
            "From this comes the chapter's basic distinction. Whatever you do, if it is done with full presence, becomes ecstasy; the same act, performed in absence, becomes hell. So there are two kinds of seeker. The first asks what to do, what action to perform, what role to take, what discipline to keep - and stays on the wrong path no matter how virtuous the action, because absence is the disease and the disease is unaffected by what the absent person happens to be doing. The second asks how to be, and only this second question opens onto meditation.",
            "He retells Buddha's encounter with the man who came asking how to serve the world. Buddha laughed. 'You cannot do anything because you are not. First be.' The story illustrates a subtle danger: doing - even compassionate, generous, useful doing - can become a sophisticated escape from the work of becoming present. You can change your character, change your morals, change your relationships, even change your life, and remain just as absent as before. Outward modifications leave the innermost core untouched, while a change in the innermost core automatically reorganises the surface.",
            "The three sutras of this chapter - the clear summer sky, space absorbed in the head, knowing yourself as light - are calibrated for that interior change. They do not give you anything new to do; they bring you to the presence that any action might or might not be performed from. Without that presence, even the holiest practices replay the original problem; with it, even the most ordinary acts become a doorway. Heaven and hell, in this framing, are not destinations but the same act performed by a present or an absent self.",
        ],
        "quotes": [
            "Hell means your absence.",
            "First be - and if you are, then whatsoever you do becomes a service, it becomes a prayer, it becomes compassion.",
            "What you do is irrelevant. What you are - absent, present, aware, unaware - that's my concern.",
        ],
    },

    # ──────────────────────────────────────────────────────────────────
    # Chapter 51 — Coming Back to Existence
    # ──────────────────────────────────────────────────────────────────
    {
        "chapter": 51,
        "title": "Coming Back to Existence",
        "paragraphs": [
            "Osho opens with a folk joke. A village postmaster is introduced to a visitor who explains that he is a Doctor of Philosophy, and the postmaster, baffled, replies that he has never heard of any case of this disease in his village. The joke, Osho says, is closer to the truth than it sounds. Philosophy is a kind of disease: abstract thinking that moves in circles, never lands, never concludes, and yet is taken so seriously that whole institutions have been built to perpetuate it.",
            "His distinction is sharp. Science reaches answers because it experiments. Religion reaches answers because it experiments. Philosophy alone speculates without experimenting, and so however much movement it generates, it produces no conclusions - only further questions disguised as answers. Every philosophical answer, dug into, turns out to be more questions, and this multiplication of unanswered questions can be enjoyed as a journey but cannot ever arrive anywhere.",
            "Religion, in this scheme, is the deeper science, because the experimenter himself is the experiment. A scientist remains aloof from his apparatus; a religious investigator places his own being in the test tube. He has no instruments outside himself; method, object and observer are one. That is why religious experimentation cannot leave you the same person, while scientific experimentation can. Once you put yourself into the apparatus, the apparatus changes you whether you wanted it to or not.",
            "Osho's warning to the reader is then very practical. The mind will gladly turn even meditation into another topic to think about. You can read about meditation, talk about meditation, accumulate techniques about meditation, and never have meditated for a single moment. All of that, he says, is dangerous, because it produces the illusion of progress while leaving the disease of philosophy untouched. The cure is to drop 'about' altogether: do not know about meditation, meditate; do not know about God, know God; do not know about love, love. Life's problems, in this view, only solve themselves once you stop thinking about existence and start being deeply rooted in it.",
        ],
        "quotes": [
            "Life's problems can be solved only when you become deeply rooted in existence.",
            "All knowledge which is 'about' is false, dangerous, because you can be deluded by it.",
            "Religion is a deeper science, because the experimenter himself becomes the experiment.",
        ],
    },

    # ──────────────────────────────────────────────────────────────────
    # Chapter 53 — From Death to Deathlessness
    # ──────────────────────────────────────────────────────────────────
    {
        "chapter": 53,
        "title": "From Death to Deathlessness",
        "paragraphs": [
            "All the enlightened ones - Buddhas, Christs, Krishnas - disagree about everything except one single point, Osho says: the ego is the only barrier between you and reality. Everything else is accidental; this one observation is essential. Where the traditions diverge in cosmology and ritual, they converge in this diagnosis, and so for Osho the basic move of any genuine spiritual work is to understand the ego with such clarity that it disappears in the seeing.",
            "Crucially, ego does not need to be dropped. It is not a thing you can throw away. It is a shadow of inattention - the way darkness is the shadow of unlit space - and so the right operation is not subtraction but illumination. Bring light into a dark room and the darkness goes; you do not have to carry the darkness out by hand. Try to look at the ego with clear awareness and the same thing happens: the very looking is what dissolves what was being looked at.",
            "Osho gives a usable test for this. When you are silent, alert, calm, you exist - but no 'I' is felt. The presence is there, the consciousness is there, but the centred sense of an I is absent. The instant anger arrives, or desire, or anxiety, the I crystallises again, hardens, takes a position. The ego, in other words, is the past mind organised at the periphery of consciousness in response to friction; in moments without friction, it is simply not produced. Memory, accumulated over a lifetime, has been pretending to be a self.",
            "From this comes the chapter's deepest claim. Love and meditation are the same phenomenon described from two sides. Both happen only when the ego has not been produced; both require, structurally, the absence of the I. That is why we talk about love so much and yet so rarely actually love - we are too occupied being someone for love to occur. And it is why Jesus could say God is love: God-realisation and ego-dissolution are not two events. Know one and you have known the other; you do not need to know about either, only to step into the silence where neither remains.",
        ],
        "quotes": [
            "If you know love, there is no need to know God - you have known him already.",
            "Whenever you are silent, the ego is not. Whenever your mind is in turmoil, the ego is there.",
            "Ego is a shadow of your non-alertness. There is no need to drop it. If you can look at it, it drops by itself.",
        ],
    },

    # ──────────────────────────────────────────────────────────────────
    # Chapter 55 — Only the Unreal Dissolves
    # ──────────────────────────────────────────────────────────────────
    {
        "chapter": 55,
        "title": "Only the Unreal Dissolves",
        "paragraphs": [
            "Osho opens with an anecdote about a small-town mayor. A visitor to the town asks the priest, the gas-station attendant and the barber what they think of him; the priest says he is no good, the attendant calls him a bum, the barber says he never voted for the rascal. When the visitor finally meets the mayor himself, the mayor explains earnestly that he has accepted the office not for any pay but solely for the honour. That, Osho says, is exactly the situation of the ego: only the person himself thinks his ego is enthroned; for everyone else it is a mild irritation at best.",
            "From this comes a clarifying inversion. The world is not actually arranged around your ego, however much you may believe it is. No one outside you cares whether you are or are not; whatever importance the ego claims is a private delusion. We live, in this regard, inside our own image of ourselves, which we then defend as if it were reality - except that reality cannot in fact support an ego, because reality is one and the ego presents itself as separate. The ego is the most impossible of objects; it is structurally false.",
            "What follows is a familiar but deeply analysed strategy: rather than risk the shocks of contact with reality, we avoid reality. We build, around the ego, a glasshouse of dreams, and live carefully inside it. Every encounter with what is, in this view, threatens to shatter the glass, and so we become connoisseurs of evasion - inventing problems we can solve from inside the dream rather than meeting the questions reality is actually putting to us. Many of the people who come to Osho with problems, he says, are dreaming the problems too; that is why no answer fits.",
            "The body's evidence for this is in our nights. Deep dreamless sleep is the one period in which the I genuinely vanishes, and that is precisely why mornings feel fresh; you have spent some hours unburdened by the impossible thing. Dream-filled nights leave you tired because the I has continued operating on the night shift, defending itself against scenarios. The wave thinks itself important, but the ocean is not worried about it. These techniques work by walking you out of the glasshouse and letting reality dissolve what was never real to begin with.",
        ],
        "quotes": [
            "You are just a wave. The wave comes and goes; the ocean is not worried about it.",
            "Reality cannot support anything which is not, and your ego is the most impossible thing.",
            "We go on escaping from reality just to protect, to defend, this impossible ego.",
        ],
    },

    # ──────────────────────────────────────────────────────────────────
    # Chapter 57 — You Are Everywhere
    # ──────────────────────────────────────────────────────────────────
    {
        "chapter": 57,
        "title": "You Are Everywhere",
        "paragraphs": [
            "Osho opens with a folk story about an old doctor whose assistant calls in a panic - a patient is choking on a billiard ball lodged in his throat. The doctor's instruction is brief: tickle him with a feather. The patient laughs, the ball flies out, and the assistant marvels at the technique. The doctor explains his lifelong rule: when you don't know what to do, do something. That rule, Osho says, is excellent for emergency comedy and fatal for meditation.",
            "The mind, in his view, is the most delicate mechanism in existence - more intricate than any other system anywhere - and improvising with it is dangerous in a way improvising with the body is not. Mix two techniques whose internal logics differ and you may produce effects that cannot be undone. Adjust a method that you have only half-understood and you may, in the name of personalising your practice, walk yourself into a knot. The first instruction, therefore, is the inverse of the old doctor's: when you do not know what to do, do nothing.",
            "Osho is also clear about the scale of what these methods are intended for. They are revolutionary rather than evolutionary - shortcuts that compress what nature would otherwise do across millions of lifetimes into a single deliberate jump. Nature will eventually deliver every being to enlightenment by the long road; technique compresses the journey into a usable lifetime. But that compression has a cost: a wrong step in a method designed to deliver in one lifetime what nature delivers across many can produce damage proportional to the speed at which it is acting.",
            "The first sutra in this chapter targets body-attachment, and Osho stresses how deep that particular attachment runs. You have been embodied in some form for so many lives that you only really know yourself as a body; whatever you have heard about the soul or the witness or pure consciousness is, for you, borrowed reading rather than direct knowing. To go past this, the technique must be entered carefully, slowly, exactly as given. Non-doing, paradoxically, becomes the most beneficial form of doing here: stay with what is given, do not reach to improve it, and let the method work the very layers of identification it was designed to reach.",
        ],
        "quotes": [
            "Non-doing will be more beneficial to you than any doing.",
            "Mind is the most complex thing in existence; there is nothing comparable to it.",
            "These techniques are revolutionary. They are shortcuts; they are not natural.",
        ],
    },

    # ──────────────────────────────────────────────────────────────────
    # Chapter 59 — Watch from the Hill
    # ──────────────────────────────────────────────────────────────────
    {
        "chapter": 59,
        "title": "Watch from the Hill",
        "paragraphs": [
            "Osho describes the human being as Janus-faced: animal in his past, divine in his potential future, and nothing very stable in the present. The animal he was is no longer; the divine he could be has not yet arrived; and so he is structurally a step from one to the other - and a step, while it is being taken, is nowhere. This homelessness in the middle is the specific tension of being human, and it is what generates the constant inner conflict every spiritual literature talks about.",
            "Whatever side of himself a person tries to satisfy, he immediately dissatisfies the other side. Indulge the animal and the divine in him revolts; indulge the divine and the animal sulks. Osho illustrates with a joke: a sports car enthusiast arrives at the pearly gates and is told heaven has beautiful highways but no cars. He asks to be sent to hell instead, where he is welcomed warmly until Satan admits, sadly, that hell has cars but no highways. That, Osho says, is the human predicament: every arrangement of pleasures has a structural absence built into it.",
            "Religions, in his diagnosis, take sides. They fight the animal in the name of the divine, or in some cases the reverse, and so they participate in the very split they claim to heal. The conflict is moved from outside to inside but never dissolved; the religious person ends up at war with himself, only with sanctioned weapons. Tantra refuses both sides. It is not for the divine against the animal and not for the animal against the divine. It is for transcendence, which means stepping out of the duality entirely rather than choosing sides within it.",
            "The technical move follows from this. Watch from the hill - that is, from a vantage point outside both forces - and the duality dissolves into a third position, what Tantra calls advait, non-duality. By staying in the present, neither shamed by the past nor reaching for the future, the practitioner discovers that the warring factions inside him were both attached to time. Cut their fuel and the war stops on its own. Tantra's techniques, on this reading, are not better weapons; they are devices for stepping off the battlefield altogether.",
        ],
        "quotes": [
            "Tantra is in the present. It is neither past nor future.",
            "These techniques are not concerned with creating a compromise within you. These techniques are to give you a transcendence.",
            "Tantra is not a struggle technique, it is a transcendence technique.",
        ],
    },

    # ──────────────────────────────────────────────────────────────────
    # Chapter 61 — Techniques to Become One with the Whole
    # ──────────────────────────────────────────────────────────────────
    {
        "chapter": 61,
        "title": "Techniques to Become One with the Whole",
        "paragraphs": [
            "Osho opens with Lord Mancroft cutting a speech short at a political rally with a small request for the audience's indulgence: 'My house is on fire.' Then comes the punchline: your house too is on fire, but you do not seem the least bit flustered. Death is approaching every moment, life is shrinking, opportunities are evaporating, and yet the inner mood is one of unhurried casualness, as though the fire were happening to someone else.",
            "He drives the point home with the devil's parable. In a hellish recession, the devil convenes his disciples to address the crisis: humans are behaving so well that hell stands almost empty. Denying God or scripture has been tried, and won't move the masses. Reassuring them that there is no hell has been tried, and won't either, because they want heaven. The cleverest disciple proposes something more devastating: not to deny anything but to convince humans that 'there is no hurry.' From that day on, he says, hell has had an over-population problem.",
            "The 'no hurry' belief, Osho says, is the structural reason why most spiritual technique fails. Postponement is the mind's most reliable tool for keeping the practitioner spiritual in name without ever becoming spiritual in fact. So long as you can quietly believe there will be time later, no method can work, because real method requires the entire being - not a fraction managing its hobbies. Crisis-level urgency is a precondition rather than an optional intensifier.",
            "From this he extracts a working principle: understanding must become action, or it is not real understanding at all. Mere acquaintance with techniques is useless; reading about them, attending talks about them, accumulating information about them, all of this can coexist indefinitely with a life utterly untransformed. These techniques to become one with the whole only do their work for someone who has understood that the house is, in fact, on fire - and that the answer, whatever it is, has to happen now, in this particular life that is currently burning.",
        ],
        "quotes": [
            "Your house is also on fire, but you don't even seem a little flustered.",
            "Unless you feel it as an emergency, a deep crisis, you will not do anything.",
            "Understanding must become action. If it is not becoming action then it is only acquaintance, not understanding.",
        ],
    },

    # ──────────────────────────────────────────────────────────────────
    # Chapter 63 — Start Creating Yourself
    # ──────────────────────────────────────────────────────────────────
    {
        "chapter": 63,
        "title": "Start Creating Yourself",
        "paragraphs": [
            "Osho begins with a sly joke. After a long, dry sermon, a minister announces that there will be a brief board meeting after the benediction. A stranger - clearly not a Christian - approaches first. The minister, assuming a misunderstanding, tries to redirect him. The stranger replies that he heard the announcement perfectly and would like to meet anyone who is more bored than he is. From the joke Osho turns serious: boredom is the diagnostic mark of being human. Look at faces in the street, or your own in a mirror, and you can read it.",
            "He distinguishes pain from boredom and locates only the second as exclusively human. Animals feel pain, but for them suffering is momentary, an accident on the periphery, never the centre. They get over it; they do not carry it into the next moment as a wound. Trees die, but death is not a problem they return to obsessively in the meantime. Only the human carries pain forward into a constant inner climate, and only the human, in the extreme of that climate, commits suicide. Aristotle called man the rational animal, but rationality is only a matter of degree; boredom, Osho argues, is the cleaner definition.",
            "What stops most people from suicide, then, is hope. He tells the story of a Chinese emperor who came to bid his condemned prime minister farewell and found him weeping - not at death, the emperor knew the man too brave for that, but at something else. The prime minister had a reason involving a flying horse and a king and a year's reprieve, and the structure of his hope is the structure of every postponement we live by. Hope keeps the bored man dragging on by promising a tomorrow in which the boredom will lift, even when nothing in the situation suggests it will.",
            "These techniques, Osho says, aim past hope at something quite different - real celebration. Not the fragile celebration that depends on circumstance, but the celebration that is built into existence itself when life is finally entered rather than endured. Trees, he reminds the reader, celebrate even while they are dying. The work of these techniques is to dismantle the boredom, dismantle the hope that compensates for boredom, and let what was always a festival become felt as one.",
        ],
        "quotes": [
            "Animals can be in pain, but they are not in suffering.",
            "Life is a festival, a celebration, a peak of joy.",
            "Boredom is human. You can define the human being through boredom.",
        ],
    },

    # ──────────────────────────────────────────────────────────────────
    # Chapter 65 — Destroy the Limits
    # ──────────────────────────────────────────────────────────────────
    {
        "chapter": 65,
        "title": "Destroy the Limits",
        "paragraphs": [
            "Osho draws a sharp distinction at the opening of this chapter: life is not a problem, it is a mystery. Science treats life as a problem and applies the mind to it - dissecting, analysing, manipulating. Religion treats life as a mystery and asks for your whole self, because a mystery cannot be solved, only lived. The two operations are categorically different, and confusing them is the source of much modern suffering.",
            "The reason a brilliant scientist can be a fool in his own life now becomes intelligible. The scientific intellect sharpens magnificently within its speciality, where the object can be cut into manageable pieces and reasoned about from outside. But life, the wider mystery, cannot be cut into pieces without ceasing to be life; the moment you bring the analytical knife to it, what you are left holding is no longer the thing you were trying to study. Hence the bewildering observation that the same mind that maps galaxies cannot manage a marriage.",
            "Osho frames this as a structural feature of the analytical mind. Analysis works downwards toward the smallest particle, which is matter; synthesis works upwards toward the highest unity, which is consciousness or, in religious vocabulary, God. Science and religion are therefore not contradictory accounts of the same territory; they are operations going in opposite directions. The deeper religion goes, the less it can answer the question 'what is God?' - because God ceases, in the journey, to be a problem with an answer, and becomes the very mystery one has dissolved into.",
            "These two short sutras - placing mind-stuff in fineness above, below and in the heart, and feeling some part of the body's form as limitlessly spacious - are not solutions. They are doorways into the mystery. Their effect is not to demystify reality but to allow reality to remain mysterious while you yourself become so saturated with it that the question of explanation falls away. The limits one is asked here to destroy are precisely the limits the analytical mind keeps drawing around what cannot, in fact, be limited.",
        ],
        "quotes": [
            "Life is not a problem but a mystery.",
            "A problem can be solved, a mystery cannot be solved - it can be lived but it cannot be solved.",
            "Science moves downwards to the lowest denominator and religion moves upwards to the highest.",
        ],
    },

    # ──────────────────────────────────────────────────────────────────
    # Chapter 67 — Go Beyond Mind and Matter
    # ──────────────────────────────────────────────────────────────────
    {
        "chapter": 67,
        "title": "Go Beyond Mind and Matter",
        "paragraphs": [
            "Osho frames these techniques with a long-running philosophical fight. What is the basic stuff of the universe - mind or matter? Materialists like Charvak in India, Epicurus in Greece, and modern Marxists insist on matter and reduce mind to a by-product. Idealists like the Vedantins insist on mind and reduce matter to a form of mind. For most of the twentieth century the materialists looked to be winning, because physics seemed to confirm them. Then physics itself cracked.",
            "Eddington was forced to say that the universe now looks more like a thought than a thing. As Max Planck and Einstein worked deeper into matter, what they found was that the deeper you penetrate, the more matter dissolves into something behind it that is not matter at all in the old sense. Individual atoms, oddly, behave somewhat like matter and somewhat like mind; they are not strictly predictable, almost as if they had a shadow of will. The clean ontological line that the whole argument depended on is no longer cleanly drawable.",
            "Tantra, Osho says, has always taken a third position. Matter and mind are both forms of an unnamed something - call it X - that lies behind both and shows up sometimes as one, sometimes as the other. This is not asserted as metaphysical doctrine, however; for Tantra it has practical weight. If matter and mind are two faces of one reality, then you can enter that reality through either face. Hatha Yoga works through the body; Raja Yoga works through the mind; Tantra uses both, switching between them as the practitioner's temperament demands.",
            "This is why Shiva's techniques sometimes ask you to do something explicitly physical and sometimes only to imagine. It is also why imagination is taken seriously here as a real intervention rather than as a daydream. For Tantra, even imagination is a mode of reality, because mind is itself a manifestation of reality; a vivid dream is not a private fiction but a shift in the very fabric you are part of. To say that something is 'just' imagined, in this framework, is to misunderstand both imagination and reality.",
        ],
        "quotes": [
            "Even imagination is a mode of reality because the mind is a manifestation of reality.",
            "The universe appears to be more like a thought than like a thing.",
            "Matter and mind are not realities, but forms of a third reality, a basic reality, which remains hidden.",
        ],
    },

    # ──────────────────────────────────────────────────────────────────
    # Chapter 69 — You Are Unknown to Yourself
    # ──────────────────────────────────────────────────────────────────
    {
        "chapter": 69,
        "title": "You Are Unknown to Yourself",
        "paragraphs": [
            "Osho opens with a stark statement: man is born alone and dies alone, and aloneness is therefore his basic reality. Society, however indispensable in the middle, is structurally accidental. The trouble is that we live so completely inside the social texture - inside the labels, names, opinions and roles that others have given us - that the self we think we know is in fact a composite of borrowed descriptions. From the outside, no one can be revealed; revelation only happens from within.",
            "Whatever identity you currently carry, then, has been handed to you. The name was given by parents, the moral image by teachers, the social role by neighbours. None of it is the immediate fact of who you are; it is a labelling system the community has used to make you usable. And the labelling has been accepted so thoroughly that even you cannot now remember what was underneath. This, Osho says, is the basic anxiety - the condition of being there but unknown to oneself.",
            "Borrowed knowledge cannot solve the problem. If someone, or some scripture, tells you that you are 'soul eternal,' that knowledge is also given by someone else, and so it cannot lift the original ignorance. Theology can swap one borrowed phrase for another, but the immediate self-encounter remains undone. Until you come to yourself directly, without passing through the social mediation, the ignorance persists, and with it the trembling that does not know what is hidden inside it.",
            "Osho cites Mahavira, who lived twelve years silent and naked in the forest. The nakedness, he insists, was not really about clothes. It was the deeper nudity of stripping away every social label - throwing the name back, throwing the form back, throwing every approved part of the inherited self back to the society that lent it. Only in that state can the original being, undecorated, be encountered. These two sutras open the same door. They are devices to remove the social mediation long enough that you can finally meet yourself without an introduction.",
        ],
        "quotes": [
            "Aloneness is his basic reality; society is just accidental.",
            "From the outside you cannot be revealed.",
            "This lack of knowledge about oneself is the ignorance, and this ignorance cannot be destroyed by any knowledge which others can give to you.",
        ],
    },

    # ──────────────────────────────────────────────────────────────────
    # Chapter 71 — Forget the Periphery
    # ──────────────────────────────────────────────────────────────────
    {
        "chapter": 71,
        "title": "Forget the Periphery",
        "paragraphs": [
            "Osho describes the surface of life as a cyclone - constant conflict, turmoil, struggle - but insists that this is only the surface. Just as the ocean has waves on top and silent depth below, life has a periphery of disturbance and a centre of stillness. The disturbance on the surface is not a problem in itself; it is even beautiful when seen from the right place. The trouble is identification with the surface, which keeps us mad.",
            "He tells the Sufi story of the fakir lost on a dark night who falls into what he believes is a bottomless abyss, catches a branch on the way down, and clings to it through hours of cold and terror. His prayers go unanswered, his hands grow numb, and at last, unable to hold any longer, he falls - to find that solid ground was less than a foot below him the whole time. He had spent the night suffering an abyss that was not there. That, Osho says, is our condition exactly: we cling to the periphery, terrified of an inner abyss that turns out to be the very ground of our being.",
            "The reason we cling is fear. The periphery is the only territory we know; the inner appears, from where we are clinging, as bottomless darkness. Tantra's techniques are not so much instructions as encouragements - devices for finding the courage to let go and discover that what looked like an abyss is in fact the place where standing is finally possible. Once you have been at the centre, you can move back to the periphery any time, but you will never again be the periphery; you will remain centred while it whirls around you.",
            "From this comes a working summary of the entire tantric programme. These techniques, taken together, are a deep relaxation into oneself. Most people are perpetually doing - manipulating, controlling, holding things in place - and that doing is the holding-on that prevents the falling-back. To stop doing is not laziness; it is the precise act by which the centre is reached. Breath comes and goes, blood circulates, the world goes on spinning, and you simply stop being the doer. In that non-doing, the periphery is forgotten and the centre, which has been there the whole time, finally becomes felt.",
        ],
        "quotes": [
            "Meditation is the deepest sleep. It is total relaxation plus something more.",
            "The very ground of your being. Once you leave the surface, the periphery, you will be centred.",
            "Tantra techniques are a deep relaxation into oneself, a total relaxation into oneself.",
        ],
    },

    # ──────────────────────────────────────────────────────────────────
    # Chapter 73 — Fear of Transformation Goes Deep
    # ──────────────────────────────────────────────────────────────────
    {
        "chapter": 73,
        "title": "Fear of Transformation Goes Deep",
        "paragraphs": [
            "Osho confronts a hard fact at the opening of this chapter. Many people seem interested in meditation; very few are actually transformed by it. If the interest were genuinely deep, it would catch fire on its own and remake the practitioner. Since this rarely happens, something must be missing - and what is missing, Osho says, is not effort but the willingness to die. The fear of transformation is, at root, the fear of death; the old self has to go before the new one can come, and most of us do not really want that.",
            "What the mind does instead is manufacture a superficial interest. There is plenty of reading, plenty of discussion, plenty of attendance at retreats and lectures, but the real intensity is missing. We deceive ourselves cheerfully because the alternative - actual transformation - feels worse than the unsatisfying status quo. The deception is subtle but lethal: it lets the spiritual seeker carry the appearance of seeking for years while the seeking itself never quite occurs.",
            "Out of this comes one of Osho's most useful diagnostic tools. Even a wrong method works if you are deeply involved in it; even the right method fails if you are using it to deceive yourself. The method is secondary; the involvement is primary. So the question is never which technique is best, but whether the practitioner has put his entire being on the table. If he has not, no technique on earth will save him. If he has, almost any technique will deliver him, because what is doing the work is the involvement, not the form.",
            "He illustrates with one of his Mulla stories. A motorist sees the village schoolhouse on fire and finds Mulla Nasruddin, the schoolmaster, sitting calmly under a tree. 'Why are you not doing anything?' the motorist shouts. 'I am doing something,' Mulla replies. 'Ever since the fire started, I have been praying for rain.' Prayer too, Osho says, can become a hideout - a way of doing something while doing nothing. These techniques only work if you stop praying for rain on your own burning house and instead become the kind of person willing to walk in.",
        ],
        "quotes": [
            "You want to be transformed, but simultaneously you want to remain the old.",
            "Even a wrong method works if you are deeply involved in it.",
            "If your soul and your heart is in your effort, no one can mislead you except yourself.",
        ],
    },

    # ──────────────────────────────────────────────────────────────────
    # Chapter 75 — Seek the Rhythm of Opposites
    # ──────────────────────────────────────────────────────────────────
    {
        "chapter": 75,
        "title": "Seek the Rhythm of Opposites",
        "paragraphs": [
            "Osho opens with a line from Walt Whitman: 'I contradict myself because I am big, because I contain all the opposites.' The same thing, he says, can be said of Shiva, and of Tantra. Tantra is the search for the rhythm of opposites: male and female, day and night, positive and negative, life and death. The river of life flows between two banks that look contradictory but are in fact cooperative; appearance is misleading on this point. Without the opposing banks, no river.",
            "This is why these one hundred and twelve techniques are so different and sometimes diametrically opposed - they are not wrong; they are different banks for different temperaments. Tantra is not partial. It does not take one side and then defend the side. It contains both, and so it is, in the strict sense, holy: not partial. Partial standpoints can be very logical, very rational, but they cannot be alive, because life itself only exists by virtue of its opposite.",
            "Osho draws on the Greek pairing of Apollo and Dionysius to make the structural point. Apollo is the god of order, discipline, virtue, culture; Dionysius is the god of chaos, freedom, dance, nature. Most religions have aligned themselves with Apollo and produced very serious gods - the Christian god, in particular, cannot easily be imagined dancing or laughing. Nietzsche complained that he could believe only in a dancing god, and never found one in his tradition; had he known of Shiva, Osho speculates, his life might have gone differently. Shiva contains both Apollo and Dionysius - serious and laughing, ascetic and sensual, immanent and transcendent.",
            "The practical instruction from this is precise. Do not try to absorb all one hundred and twelve techniques. Find the one that suits your particular temperament, the one that grips you and holds you, and forget the other one hundred and eleven. The contradictions among the techniques are not defects; they are the texture by which Tantra accommodates every possible kind of person. You only need one. The whole spectrum exists so that each kind of seeker can find his particular bank, step into the same river, and arrive at the same sea.",
        ],
        "quotes": [
            "Tantra is the search for the rhythm of opposites.",
            "Wherever life exists, it exists through its opposite.",
            "Find your technique. In these one hundred and twelve techniques, only one technique is for you.",
        ],
    },

    # ──────────────────────────────────────────────────────────────────
    # Chapter 77 — Become Each Being
    # ──────────────────────────────────────────────────────────────────
    {
        "chapter": 77,
        "title": "Become Each Being",
        "paragraphs": [
            "Osho roots these techniques in a single insight. Existence is one. Self-consciousness, however, gives each of us the false feeling of being a separate centre, and that false separation is the source of every anxiety, every fear of death, every species of human anguish. Whatever else you do, if it is built on this presumption of separateness, it will be poisoned by the presumption.",
            "Sleep, in this scheme, is the daily proof. In dreamless sleep we lose this separation entirely and merge back into the whole. That is why mornings feel reborn: a few hours without the I have refreshed everything the I had been straining. The same source that you visit nightly is the source Buddha settled into permanently; the only difference is that Buddha goes consciously, while you go unconscious. Samadhi, in the Hindu definition Osho cites, is precisely sleep made conscious - alertness retained while the I is being dissolved.",
            "The ego, on this view, is not an enemy but a developmental shell. Like the shell of an egg or the husk of a seed, it has its protective use early on; without some sense of 'I exist' the small child cannot survive the abrasions of the world. But protection that was once necessary becomes, at a certain point, the very obstacle to further growth. The shell that kept the seed safe must dissolve into the earth, or no sprout emerges. To die with the ego still hard around you is, in this metaphor, to die as a seed, never having opened.",
            "These three sutras - feeling each consciousness as your own, becoming each being - work directly to crack that shell. They use the imagination as a precise tool, asking you to extend awareness into the awareness of others until the boundary between yours and theirs becomes thin enough to break. What is being practised is not a feeling of solidarity but a structural dismantling of the felt centre. Done well, the technique returns you to the same source you visit every night, but this time with the lights on.",
        ],
        "quotes": [
            "Hindus have always believed that samadhi is conscious sleep.",
            "Existence as such is one. The human problem arises because of human self-consciousness.",
            "If someone dies with the ego, he has died as a seed.",
        ],
    },

    # ──────────────────────────────────────────────────────────────────
    # Chapter 79 — The Philosophy of Emptiness
    # ──────────────────────────────────────────────────────────────────
    {
        "chapter": 79,
        "title": "The Philosophy of Emptiness",
        "paragraphs": [
            "Osho closes the book with the most delicate techniques of all - those of emptiness. He explains that Buddha used these very four sutras with his bhikkhus, and was so badly misunderstood for it that Buddhism eventually was uprooted from the Indian soil where it had been born. The reason for the misunderstanding is that Buddha denied, in turn, God, soul, and any substantial spiritual goal - and this looked, to those listening, like atheism rather than the precise pedagogical move it actually was.",
            "The pedagogical logic is severe. If there is a God to be reached, you cannot be totally empty - the God will be there, even if you are not, and your mind will subtly hide behind the divine furniture. If there is a soul to find, you cannot be totally empty either - the ego will reorganise itself behind the word atman and pose as a spiritual self. So Buddha removed the entire inventory: no God, no soul, no goal, no destination. Only after the room had been cleared could the techniques of emptiness do their work.",
            "Osho stresses that earlier masters, before Buddha, had told seekers to become desireless - while still dangling moksha, kingdom, paradise, ultimate liberation as the prize at the end of the discipline. He calls this a basic contradiction. You cannot be desireless if you are practising desirelessness in order to attain something. The desire to be desireless is still a desire, only better dressed. Buddha removed the prize altogether, so that desirelessness could finally be real rather than a strategy.",
            "What this produces, finally, is not nothing in any nihilistic sense. It is a vacant room - and into a vacant room, existence itself can speak. The four techniques in this chapter calibrate that emptiness from different angles, but they all aim at the same condition: a self so cleared of contents that it can no longer be defended as a self. When that condition lands, what was always present and always missed becomes, for the first time, accessible. You enter the truth, Osho says, only when you are totally empty - because for as long as you are full of yourself, there is nowhere for the truth to come in.",
        ],
        "quotes": [
            "You can enter the truth only when you are totally empty.",
            "If all desires go, you simply disappear. Not that you will not exist - you will exist, but as an emptiness.",
            "He destroyed all the goals just to help you to be desireless.",
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
        "Comprehensive multi-paragraph framings (paraphrased in the file author's "
        "own English) of the opening sections of the 39 sutra-introducing chapters "
        "in Osho's discourses on Vigyan Bhairav Tantra. Each entry expands the "
        "frame of mind Osho asks the reader to bring to the techniques in that "
        "chapter, including key anecdotes, illustrations and arguments. Each entry "
        "exposes 3-4 paragraphs and 2-3 short attributed direct quotes (each "
        "under 30 words)."
    ),
    "chapter_count": len(CHAPTERS),
    "chapters": CHAPTERS,
}

# ── Validation ───────────────────────────────────────────────────────
assert len(CHAPTERS) == 39, f"Expected 39 chapters, got {len(CHAPTERS)}"
expected_nums = list(range(3, 80, 2))
actual_nums = [c["chapter"] for c in CHAPTERS]
assert actual_nums == expected_nums, (
    f"Chapter numbers don't match. Expected {expected_nums}, got {actual_nums}"
)

problems = []
total_words = 0
total_quote_words = 0
total_paragraphs = 0
total_quotes = 0
for c in CHAPTERS:
    n = c["chapter"]
    paragraphs = c.get("paragraphs", [])
    quotes = c.get("quotes", [])
    # Required: 3 to 5 paragraphs.
    if not (3 <= len(paragraphs) <= 5):
        problems.append(f"ch{n}: {len(paragraphs)} paragraphs (need 3-5)")
    # Required: 2 to 4 quotes.
    if not (2 <= len(quotes) <= 4):
        problems.append(f"ch{n}: {len(quotes)} quotes (need 2-4)")
    # Each paragraph must be substantive.
    for i, p in enumerate(paragraphs):
        wc = len(p.split())
        total_words += wc
        total_paragraphs += 1
        if wc < 60:
            problems.append(f"ch{n} p{i+1}: only {wc} words (want >=60)")
    # Each quote must be short.
    for i, q in enumerate(quotes):
        wc = len(q.split())
        total_quote_words += wc
        total_quotes += 1
        if wc >= 35:
            problems.append(f"ch{n} q{i+1}: {wc} words (want <35)")

if problems:
    print("VALIDATION ISSUES:")
    for p in problems:
        print("  -", p)
else:
    print("All validation checks passed.")

out_path = Path(__file__).parent / "_chapter_intros.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(OUTPUT, f, indent=2, ensure_ascii=False)

print(f"\nWrote {out_path}")
print(f"Chapters         : {len(CHAPTERS)}")
print(f"Total paragraphs : {total_paragraphs}")
print(f"Total quotes     : {total_quotes}")
print(f"Total body words : {total_words}")
print(f"Avg per chapter  : {total_words/len(CHAPTERS):.1f}")
print(f"Avg quote words  : {total_quote_words/total_quotes:.1f}")
