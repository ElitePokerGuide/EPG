# Concept cards digest - cash-6max

357 cards (27 consensus, 330 single-source) | by status: {'draft': 339, 'needs-review': 18} | source refs by school: {'2cc': 74, 'cc': 118, 'rio': 130, 'br79': 198}

Review legend: ✅ approve as is · ✏️ approve with edit · ❌ reject (say why: wrong / obvious / not content-worthy / duplicate)


## PART 1. Consensus cards (cross-school)  (27)

### Most of your flop check-raises belong against the small c-bet on low and paired boards
`c-cash-6max-x-bb-check-raise-vs-small-cbet-001` · intermediate · flop · srp · bb · consensus 1.00 · sources: 2cc,rio · **draft**

**Claim.** As the caller, check-raise most often against a quarter- to third-pot c-bet, and most often on low, mid-low and paired flops. Baseline around 15% against a small bet, over 20% on the best textures, a few percent against an overbet. Two-Broadway flops are low, but low is not zero.

**Why.** A small c-bet is made with a wide weak range and offers you a cheap raise that puts real pressure on it, so solvers raise far more there than against a big polarized bet. Low boards favour the caller: suited connectors and small pairs make sets, two pairs and strong draws while the raiser's high cards whiff. On paired boards the raiser bets small with almost everything, so a raise with trips, pairs and good draws attacks a range that is mostly air; even second and third pairs raise some of the time to fold out six-out overcards before the turn. Draws that raise need extra equity: a flush draw with straight backdoors, or a high card holding one card of the flush suit. Passive players who skip these raises usually also fold too much in the same spot, so fixing one fixes the other.

**Common mistake.** Defending against a 25% bet almost entirely by calling, and check-raising mostly on high-card boards where you hit top pair and the raise does least.

**Numbers.** Check-raise vs a small c-bet: baseline ~15%, over 20% on low paired boards like 774, ~13% on king-high boards

**Hooks.** _The bet size you should attack most is the smallest one._ · _Why pocket fives check-raises 774._ · _Your check-raise leak lives in one spot. Here it is._

Review: [ ]

### Big hand, big pot; medium hand, small pot
`c-cash-6max-x-big-hand-big-pot-001` · beginner · multi-street · srp · any · consensus 1.00 · sources: br79,cc,rio · **draft**

**Claim.** Match the pot you build to the hand you hold. Nutted hands want a fast-growing pot and bet near pot on every street, especially against players who call with any piece. Second pair and other medium hands have a low ceiling: bet them small or check, and never bet big just because your range is ahead.

**Why.** Each hand can value bet comfortably up to a certain pot size and no further. A set is happy in any pot and benefits from geometric growth that leaves a river shove on the table; second pair that bets big on three streets arrives at a river where it can no longer be a value bet, so the money went in for nothing. Against sticky opponents the first half of the sizing trade-off disappears: they call the same whether you bet half pot or pot, so the only lever left is size, and three near-pot bets get the stack in while three small bets leave most of it behind. Big pots are built with big bets, and only the hands that can stand a big pot should build them. Before sizing up, ask what pot your hand still wants to be in on the river.

**Common mistake.** Betting small with a monster 'to keep them in' against someone who was never leaving, or betting big with a medium hand to find out where you are.

**Numbers.** Nutted hands against callers: bet near pot on every street

**Hooks.** _Second pair, three big bets, river: now what?_ · _Betting small 'to keep them in' against someone who was never leaving._ · _The pot your hand can afford._

Review: [ ]

### C-bet most on high, dry and paired flops; least on middling connected and monotone ones
`c-cash-6max-x-cbet-flop-texture-map-001` · beginner · flop · srp · ip · consensus 1.00 · sources: 2cc,br79,cc,rio · **draft**

**Claim.** In position as the raiser, bet almost everything on high-card rainbow flops and on paired flops. Slow right down on middling connected boards like 876 or T98, especially two-tone, and on monotone flops. The caller's range is built from medium suited and connected cards; yours from big cards.

**Why.** The caller's preflop range is weighted to small cards, suited connectors and gappers, while the raiser holds the broadways and big pairs. High flops miss the caller and give you top pairs and overpairs, so bets get through and the hands that continue are weak. Paired flops remove most of the caller's two-pair and set combos. Rainbow textures take away flush draws, so fewer hands can continue. Middling connected flops do the opposite: the caller has pairs, two pair, straight draws and combo draws, and your two overcards have about six outs and little fold equity. Monotone boards hand the caller proportionally more flushes. Score a flop on these features before you look at your hand and the c-bet frequency falls out, from near 100% down to a range check.

**Common mistake.** C-betting a fixed percentage on every flop, which under-bets the boards where the whole range profits and fires on 876 two-tone with two overcards and no plan.

**Numbers.** Paired A/K/Q-high and rainbow high-card flops: c-bet close to 100% · Middling connected two-tone flops (876, T98 type) with no equity: check

**Schools disagree.** When a middling connected flop does get bet, some coaches use about 75% pot while others keep the small third-pot size on every low board. / Some coaches range-check the worst flops in position because a 20% c-bet cannot be executed, while others keep a small c-bet with the top 20-60% of hands there. / Ace-high flops split the schools: some range-bet them small, others check them back a third of the time or more.

**Hooks.** _The flop you should never c-bet, and the one you should always bet._ · _Three features decide your c-bet before you look at your hand._ · _Four courses agree on which flops to bet. They fight over one texture._

Review: [ ]

### Commit to your answer before the solver or trainer shows it
`c-cash-6max-x-commit-before-the-solver-answers-001` · beginner · consensus 1.00 · sources: cc,rio · **draft**

**Claim.** In every drill, say what you think before you look: the equity after a call, whether a hand is a clear bet, a clear check or a mix, how confident you are. Then compare. Reading the answer first trains nothing; a committed guess that turns out wrong is the feedback that moves your game.

**Why.** Estimation is a motor skill: you improve through feedback on your own attempts, not by studying the physics. Players who write down a number and see they were ten points low learn why, for example that the opponent must call many unpaired hands on a dry board. Trainers show frequencies, not just right or wrong, and that extra information only improves your model if you had a prediction to test it against. Declaring 'pure' versus 'mix' reveals whether you systematically see mixes as pures (too rigid) or pures as mixes (too random), a leak no score can show. Saying 'loose but fine' before a call that turns out pure, or 'clear fold' before one that turns out to be a call, is where the learning happens. Nodding at the solver and thinking 'I knew that' is the failure mode.

**Common mistake.** Opening the solver, nodding at the numbers, and never testing whether you could have produced them yourself.

**Hooks.** _The one-second habit that makes solver study actually stick._ · _You didn't know that. You read it._ · _Say it out loud before you click. Here's why it works._

Review: [ ]

### Check the flop, bet the turn: the delayed c-bet is a line, not a give-up
`c-cash-6max-x-delayed-cbet-001` · intermediate · turn · srp · ip · consensus 1.00 · sources: br79,cc,rio · **draft**

**Claim.** Checking back the flop in position and betting the turn is a strong plan, especially against players who attack c-bets or who have just lost a pot to you. The opponent never had to call a bet, so their range is still full of air and folds well above the break-even rate. What you must never do after checking back is show down a hand with no showdown value.

**Why.** A flop c-bet filters the opponent's range; a check does not. So on the turn after a check-back they still hold junk, and against a small bet they fold far more than symmetric ranges would, which makes the delayed bet more bluff-friendly than a double barrel. Against fickle players who raise c-bets after losing a pot, checking removes the trigger and lets them take the lead with air. Building more flop checks into a plan also routes the pot into turn probes, delayed bets and check-check-check rivers that opponents study less and play worse. Betting the turn or waiting to bet the river are close in EV; checking all the way down with air while your range still holds the advantage is the serious error.

**Common mistake.** Checking the flop, checking the turn, then checking the river with queen-high 'because I never showed strength'.

**Hooks.** _You checked the flop. Your bluff just got better._ · _The c-bet that works better one street late._ · _Checked twice with queen-high? You're not done yet._

Review: [ ]

### Against a small bet, fold almost nothing
`c-cash-6max-x-fold-little-to-small-bets-001` · beginner · flop · srp · oop · consensus 1.00 · sources: br79,cc,rio · **draft**

**Claim.** Facing a quarter-pot c-bet, a min-bet or a tiny lead, continue with nearly anything that has a pair, a draw, a backdoor plus an overcard or showdown potential. The price is 5-to-1 or better, and folding more than the bare minimum hands the bettor a profitable bet with any two cards. Against an overbet, the line moves to strong bottom pair or a real draw.

**Why.** A quarter-pot bet offers odds that almost any hand with equity and a path to improve can take. Weak players also use tiny bets with both monsters and nothing, so the bet narrows their range very little. When your range is far stronger than the bettor's, fold nothing at all: even your worst hand is entitled to a big share of the pot. The structural exceptions are high monotone boards without a suit card and high paired boards where unpaired low cards have no way to win; even there the fold rate stays under a third. The threshold is driven by price, so a backdoor draw is a reason to call a small bet and no reason at all to call a big one. If your pool uses both sizes you need two thresholds per texture, not one.

**Common mistake.** Folding bottom pair, ace-high or a gutshot to a quarter-pot bet because the hand 'missed', which lets the bettor print with a range bet.

**Numbers.** Facing ~25% pot or less: continue with any pair, draw, or overcard plus backdoor; fold only pure air

**Hooks.** _The bet you should almost never fold to._ · _5-to-1 and you folded bottom pair?_ · _Small bet, big mistake: why folding here pays the bettor._

Review: [ ]

### Open marginal hands from early position only when weak players sit behind
`c-cash-6max-x-marginal-early-opens-need-weak-callers-001` · beginner · preflop · utg · consensus 1.00 · sources: br79,cc · **draft**

**Claim.** Hands at the edge of an early-position opening range, deuces and threes, 76 suited, T3 suited, are a fold against regulars and a raise when a loose passive player is in the blinds or left to act. The chart gives the answer against the hardest table; who is sitting behind you moves it.

**Why.** Equilibrium charts tell you what is barely losing against opponents who punish you correctly. The margin on these hands is tiny, so table composition swings the answer. Against regulars who 3-bet or fold, a speculative hand has nothing going for it out of position; against a weak player who calls and pays off two pair or a set, the same hand gains more after the flop than the chart says it loses before it. Fewer tables means more focus to extract from those spots, which also shifts the marginal hands from fold to raise. Treat the chart as a baseline for the hardest conditions and move off it when the conditions are softer, not as a rule to follow regardless of who is at the table.

**Common mistake.** Following a preflop chart rigidly and folding small pairs from early position at a table full of players who will call and pay off.

**Hooks.** _Your preflop chart assumes the worst table. You're not at it._ · _Fold 76s from UTG. Unless this guy is in the big blind._

Review: [ ]

### MDF is not a defense target: fold by equity and by whose range is ahead
`c-cash-6max-x-mdf-is-not-a-target-001` · intermediate · flop · srp · oop · consensus 1.00 · sources: 2cc,br79,cc,rio · **draft**

**Claim.** Minimum defense frequency tells you how often to continue so a bettor's pure bluffs break even, assuming roughly equal ranges. Ranges are rarely equal. When your range is well behind, folding more than MDF is correct; when your range dwarfs theirs or the bet is tiny, fold almost nothing. Build your flop defense from hand-class thresholds, not a percentage.

**Why.** Against a range much stronger than yours the bettor is simply profitable; trying to hold them to break-even means calling with hands that lose money, and solvers show the disadvantaged side folding well above the MDF rate on flops the raiser dominates. The reverse holds too: facing a small lead with a range that dominates the board, continue with everything, because even your worst hand is entitled to a big share of the pot. On early streets equity realization and future play matter more than one ratio, so write down the weakest hand class that still continues per texture and bet size, such as 'two overcards or a combination backdoor', and move that line against specific opponents. At micro stakes the same logic says fold medium pairs to raises more readily, since the population raises with real hands, while never folding to a one-blind bet.

**Common mistake.** Forcing yourself to call 'to meet MDF' as the big blind on a flop where the raiser's range is far ahead, or defending to a percentage instead of a hand class.

**Schools disagree.** Some coaches say fold more than MDF whenever your range is behind, while others show the big blind folding well under MDF to small c-bets on most flops despite being behind, with folds above MDF only on high monotone and high paired boards. / Some coaches would never fold a pair or a draw to a small bet, while others say that against micro-stakes aggression a middle pair facing a raise is a fold without a read.

**Hooks.** _'Defend MDF or you're exploitable' is wrong most of the time._ · _The math says fold 20%. The solver folds 35%. Here's why._ · _Four courses, one acronym, two opposite warnings._

Review: [ ]

### Monotone flops: c-bet far less, and never big
`c-cash-6max-x-monotone-flop-cbet-001` · intermediate · flop · srp · ip · consensus 1.00 · sources: 2cc,cc,rio · **draft**

**Claim.** On a flop where all three cards share a suit, check back much more than usual as the raiser, and when you do bet, use the small size. Flushes and flush draws beat every overpair, and the caller's range holds proportionally more suited hands than yours.

**Why.** The raiser's edge normally lives in overpairs and high-card pairs. On a monotone board both players hold made flushes and strong draws, and those beat any pair, so that edge is irrelevant. The caller's defending range is built heavily from suited hands while the raiser's opening range contains many offsuit broadways, so the share of flushes is higher on the caller's side and the nut advantage flips. With no nut edge and a thin range edge the correct play is to bet infrequently and small; a big bet just loads money against a range that can have it. These boards are rare, so learn the two rules above, note which hands raise or float without a suit card, and do not chase every nuance.

**Common mistake.** Applying the 'high board equals big bet' rule mechanically and overbetting a KQ3 flop that happens to be all one suit.

**Numbers.** Monotone flops: when betting, ~25-33% pot; no monotone flop wants an overbet

**Hooks.** _The flop where your overpair is just a pair._ · _You have KK on a monotone flop. Why checking is right._ · _Three courses, one texture, zero disagreement: here's the monotone rule._

Review: [ ]

### 'They could have the nuts' is not a reason to check or fold
`c-cash-6max-x-possible-nuts-is-not-a-reason-to-check-001` · beginner · multi-street · srp · any · consensus 1.00 · sources: br79,cc,rio · **draft**

**Claim.** The opponent can nearly always hold something that beats you. Ask how big a share of their range it is. If trips are a few percent and the rest is worse than your hand, value bet and accept the occasional cooler; on a paired board a wide player who raises is drawing far more often than holding trips. Replace the fear with a frequency.

**Why.** Only two cards in the deck make trips, while a wide range holds many more flush and straight draw combinations, so on a wet paired board a raise from a loose player is a draw far more often than a nine. In a checked-down pot a four-straight on the river is rarely in the opponent's hand because nobody showed strength, so a strong ace or top pair still bets, often big. The same instinct makes players stop bluffing: if you only bluff when the nuts are impossible you never bluff. Fear of the worst case is wired in and gets louder when running badly, which is exactly when thin value and bluffs disappear from a game. Tight preflop stats do not earn automatic credit either; judge the action in the hand, not the label.

**Common mistake.** Checking a strong hand or abandoning a bluff because 'there are sets in his range', without asking how big that part of the range is.

**Hooks.** _He could have the nuts. He could also have the other 95% of his range._ · _Why a four-straight river is still a value bet._ · _The fear that quietly deletes your thin value bets._

Review: [ ]

### Range-bet high paired flops small; low paired flops are the exception
`c-cash-6max-x-range-bet-high-paired-flops-001` · beginner · flop · srp · ip · consensus 1.00 · sources: 2cc,br79,cc,rio · **draft**

**Claim.** On AAx, KKx and QQx flops the preflop raiser can bet the whole range for a small size, about a quarter to a third of the pot. The caller flat-called with a range whose strong aces and kings mostly 3-bet preflop, so the trips belong to you and they mostly hold air. Lower paired boards, around TTx and below, need a different plan.

**Why.** A paired flop is hard to hit: only two cards in the deck make trips, and the caller's strong Ax and Kx mostly 3-bet preflop instead of calling. So on a high paired board one player owns the trips and the other has small pairs and nothing. Every reason to bet improves at once, which is why solvers bet close to 100%. The size stays small because the caller does hold some trips and few hands can raise you, so a quarter-pot bet taxes the junk without exposing your medium hands. As the pair rank drops, the caller holds the paired card more often, the correct defense (pairs, straight draws, suited cards) becomes obvious, and check-raises rise, so the solver mixes in checks and the schools stop agreeing on what to do.

**Common mistake.** Slowing down on KK4 because 'nobody has anything', and checking back a range that would print money betting.

**Numbers.** High paired flops (AAx/KKx/QQx): c-bet close to 100% at ~25-33% pot

**Schools disagree.** On low paired boards some coaches keep range-betting but go big (about 75% pot) because overpairs keep ~90% equity, others bet a third of the pot, and others keep the solver's checks and only range-bet the high pairs.

**Hooks.** _Nobody has anything on KK4. That's exactly why you bet everything._ · _Paired boards: four courses agree on the high ones, split on the low ones._ · _Why the ace on AA7 belongs to you, not the caller._

Review: [ ]

### Study flops as texture groups from aggregate solver reports, not one board at a time
`c-cash-6max-x-study-flops-by-texture-not-by-board-001` · intermediate · flop · srp · consensus 1.00 · sources: 2cc,rio · **draft**

**Claim.** Do not memorise solver output flop by flop. Run an aggregate report or a representative subset of around a hundred flops, sort by check frequency and by size, and read off which features (high card, pairing, suits, connectivity) drive the decision. Build categories from what the solver does, not from how the board looks, and compress each into a short rule.

**Why.** There are 1755 strategically distinct flops, but solver choices cluster strongly by texture, so a well-chosen subset reveals the same rules a full study would. Sorting by chosen size or by betting frequency makes the shared features of each group jump out, and those are what you can recognise at the table. Drawing the boxes first ('ace-high', 'king-high') produces groups that mix a range-bet texture with a mostly-check texture, and the rule you write is wrong for half of them. Write each texture's answer as a phrase short enough for a flash card: the size, the frequency, the weakest hand class that still continues. Aggregate reports work for the flop c-bet node; from the turn on, switch to individual sims because the bet-size sequences diverge.

**Common mistake.** Opening single flops in a solver, memorising specific hand mixes, and having nothing transferable when a slightly different board appears.

**Numbers.** 1755 strategically distinct flops; a subset of roughly 100 is enough to extract the texture rules

**Hooks.** _1755 flops. You need to study about 100._ · _Sort the solver report, don't read it._ · _Why 'ace-high board' is the wrong category._

Review: [ ]

### Bet thin for value on the river at about half pot and do not fear the raise
`c-cash-6max-x-thin-river-value-half-pot-001` · intermediate · river · srp · ip · consensus 1.00 · sources: br79,cc,rio · **draft**

**Claim.** When the opponent's range is capped, bet medium-strength hands for value on the river, second pair and even small pocket pairs, sizing around half pot so worse hands can call. If you never get called by a better hand you are not betting thin enough. A river raise is rarely a bluff at low stakes, so bet and fold to it without regret.

**Why.** A capped opponent holds many weak pairs and unpaired hands. A half-pot bet gets called by enough of them to make medium-strength value profitable while keeping the loss small when you run into something better; going big with everything folds out exactly the hands you want to be called by. Judge the bet by your equity against the hands that continue, not against the whole range before you bet. The fear of a raise is the most common reason players leave value unbet, yet typical pools raise rivers only with strong hands, so the raise carries little risk: fold and lose one bet. Solvers mix half-pot and pot partly to protect against river check-raises; against players who almost never raise rivers, size your strongest hands bigger and keep half pot for the thin ones.

**Common mistake.** Checking back middle pair or a low pocket pair on the river because it does not feel strong enough for a pot-sized bet, instead of sizing down.

**Numbers.** Thin river value against a capped or sticky range: about half pot

**Schools disagree.** Facing a river raise after a thin value bet, some coaches treat every hand as a bluff-catcher to call at a mixed frequency, while others say at micro stakes the raise is almost always the nuts and the fold is automatic.

**Hooks.** _Getting called by a better hand sometimes means you're doing it right._ · _Half pot on the river wins more than pot. Here's why._ · _River raise: hero call or snap fold? The courses don't agree._

Review: [ ]

### When a weak hand raises or floats, it should hold a card of the board's suit
`c-cash-6max-x-backdoor-suit-picks-the-bluff-001` · intermediate · flop · any · consensus 0.88 · sources: 2cc,br79,cc,rio · **draft**

**Claim.** Among marginal hands, the one with a backdoor flush draw in the flop's suit is the one that check-raises, 3-bets or continues; the same hand without the suit calls if it has showdown value and folds if it does not. Two suited cards in a suit not on the board add almost nothing, and never bluff with zero ways to improve.

**Why.** Raising builds a pot you want to keep playing in, so the raising hand should be the one that improves on the most turn cards and blocks the opponent's strongest continuing combos. A backdoor flush draw does both: it adds turn cards to barrel on and removes suited combos from their range. Solvers consistently raise the suited version of a hand class and flat or fold the unsuited one, and the most common drilling error coaches report on themselves is taking the aggressive line with the wrong-suit version. Facing a check-raise, a direct flush draw continues, the strongest suited backdoors continue, and offsuit air folds. On the turn the same idea becomes blocker logic: the worst bluff is the one that blocks the hands that would fold and unblocks the draws that call.

**Common mistake.** Check-raising ace-high or king-high with no backdoor suit because it feels too weak to call, while flatting the same hands when they do have the suit.

**Schools disagree.** Some coaches never bluff without at least a backdoor draw or a gutshot, while others say that in favourable spots pure air should bluff too and demanding a 'get-out clause' before bluffing makes your betting range far too strong.

**Hooks.** _The suit of your cards decides more bluffs than the rank._ · _Diamonds on a two-spade board are not a draw._ · _Need a draw to bluff? Three courses say yes. One says that's your leak._

Review: [ ]

### Against typical opponents, c-bet more than theory where the right defense is hard to find
`c-cash-6max-x-cbet-more-than-theory-vs-overfolders-001` · intermediate · flop · srp · ip · consensus 0.88 · sources: 2cc,br79,cc,rio · **draft**

**Claim.** Before copying a solver's 60-80% c-bet frequency, look at what the caller is supposed to do. If the correct defense relies on hands most players never find, bet your whole range. Real pools fold the flop too much and raise too little, so the hands theory checks for showdown now profit from betting. Where the pool raises more than theory, do the opposite.

**Why.** A solver's checks exist to stop a perfect opponent from exploiting you, and most opponents do not. On a flop like K72 two-tone, both a cautious and a maximum exploit against population data say bet 100% instead of about 80%, because the pool folds more and does not raise more. At micro stakes the effect is stronger: players continue only when they connect and rarely float or check-raise light, so in position against one opponent a bet wins often enough that your hand matters less. The adjustment is board-specific. On low paired two-tone boards the pool check-raises more than theory, and there the right exploit is to bet less and with a stronger range. So the question is not 'am I the raiser' but 'is their correct response obvious or awkward'.

**Common mistake.** Checking back ace-high and queen-high on K72 against players who fold the flop too often, giving away the fold equity a range bet collects.

**Numbers.** High dry flops like K72 vs typical pools: c-bet 80-100% rather than the solver's mixed strategy

**Schools disagree.** Some coaches set the default at 80-90% of all flops in position because micro opponents fold, while others cap the same flops at 55-80% and check real hands to stay balanced; against passive recreational pools the first works, against regulars the second. / The adjustment flips by texture: on low paired two-tone flops the population raises more than theory, so some coaches cut the c-bet to about 37% there while still range-betting king-high boards.

**Hooks.** _The solver checks 20% here. Against real players, don't._ · _Micro coaches say c-bet 80%. Solver coaches say 57%. Both have a point._ · _One number the solver gets 'wrong' against humans._

Review: [ ]

### Check strong hands to induce only when the opponent will actually bet
`c-cash-6max-x-do-not-check-to-induce-vs-passive-001` · beginner · multi-street · srp · any · consensus 0.88 · sources: 2cc,br79,cc,rio · **draft**

**Claim.** Slow-playing or betting small to let the opponent raise works only against players who put money in on their own: aggressive, tilted, or known to attack checks. Against the passive player who calls everything but bets nothing, and against a weak range that will check back, bet yourself and bet big. The player with the strong range should do the betting.

**Why.** A check to induce has two costs when it fails: you miss a full street of value and you give a draw a free card. It pays off only when the chance they bet is very high. The typical low-stakes opponent is passive by nature, calling a lot and betting rarely, and a weak range facing a board that smashes you will mostly check behind, so the trap never springs while their equity gets realised for free. The same logic governs size: a small bet with a strong hand is a trap play that relies on the opponent raising with draws and weaker pairs. If they mostly call or fold, the pot stays small and you lose one or two streets of value, so keep a big size against passive opponents. The exception is a spot where the raise really is coming, such as an opponent who check-raises far too much; there the slow-play earns.

**Common mistake.** Checking top set 'to let them catch up' against a passive player, then watching the hand check through two streets.

**Schools disagree.** Some coaches slow-play strong hands on turns against opponents who check-raise too much, while others warn that inducing fails far more often than hand-history forums suggest; the difference is whether the opponent is actually aggressive.

**Hooks.** _You checked the nuts to trap. They checked back. Twice._ · _Why 'let them bet it for me' loses a street._ · _Slow-play the maniac, bet pot into the station. Courses agree on the rule, not the player._

Review: [ ]

### High Broadway flops like KQ3 and JT6 take the big c-bet or overbet
`c-cash-6max-x-big-cbet-high-card-flops-001` · advanced · flop · srp · ip · consensus 0.83 · sources: 2cc,cc,rio · **draft**

**Claim.** In position as the raiser, flops with two high cards and few straights, such as JT6, KQ3 or KJ3, are where you bet big: 75% pot at minimum, and most solver-based coaches use an overbet. The caller 3-bet most of their big pairs and broadways preflop, so after a call you own nearly all the top pairs, two pairs and sets.

**Why.** Size follows the nut region. On these boards the caller's flat range is almost empty of QQ+, AK, AQ and KQ while the raiser has all of them, and the caller can rarely hold the nuts. When one side has most of the strongest hands and the other almost none, the big size is what gets paid, and the bluffs ride along. Count the possible straights as a proxy: with three live straights the caller catches more robust hands and the size comes down to medium. Low flops never overbet, because the caller's small suited and connected cards make sets, two pair and big draws. Paired boards where the caller holds the paired rank (QQT) and monotone boards lose the overbet for the same reason: the top of the ranges is shared.

**Common mistake.** Betting the same half or two-thirds pot on every high-card board, which leaves value behind when you hold the nut advantage and overcommits when you do not.

**Numbers.** Overbet on two-Broadway, few-straight flops: ~115-150% pot; 75% is the conservative alternative · Boards with three possible straights: medium size ~75% pot

**Schools disagree.** Some coaches cap the big c-bet at about 75% pot and say an ace or king on the flop removes the nut edge, while others overbet 115-150% on exactly those king- and ace-high Broadway boards. / On two-Broadway flops some coaches keep two sizes (quarter pot and overbet) and remove the check entirely, others use one size per texture everywhere.

**Hooks.** _The flop where a pot-sized bet is too small._ · _Why the big blind can't have it on KQ3, and what that means for your size._ · _75% or 150%? Two courses, same board, different answer._

Review: [ ]

### Out of position, the flops you skip c-betting should be the marginal ones
`c-cash-6max-x-cbet-less-out-of-position-001` · intermediate · flop · oop · consensus 0.83 · sources: br79,cc,rio · **draft**

**Claim.** Position changes the price of a c-bet that gets called. In position you can check the turn and take a free card; out of position you act first with no information. So keep a very high frequency in position and let most of your non-c-bets happen from the blinds, especially on middling boards and on dry jack-to-king-high flops where a small stab gets few folds.

**Why.** Out of position a called c-bet leaves you first to act on the turn, and a bluff on a bad texture compounds across streets. As the 3-bettor with a wide range on a board like Q73, a quarter-pot bet folds only about 13% of the caller's range, so checking the whole range costs almost nothing and routes the pot into check-raise and delayed lines where your value hands do better. In position the same flop is often a bet, because if called you still control the turn. Position is a proxy, not the whole story: on boards that heavily favour the out-of-position player, such as a paired king-high flop as the 3-bettor from the blinds, you should still bet everything, because the player with the strong range should do the betting.

**Common mistake.** Using the same c-bet frequency in and out of position, which means bluffing too much from the blinds and too little from the button.

**Schools disagree.** Some coaches frame the rule as position, while others say position only changes the cost of being wrong and an out-of-position range that dominates the board should still bet everything.

**Hooks.** _Same flop, same hand: bet on the button, check from the blinds._ · _Why your c-bet frequency should be two numbers, not one._ · _Three courses say check more from the blinds. One says position isn't even the reason._

Review: [ ]

### Medium-strength hands check the turn even when your range is ahead
`c-cash-6max-x-medium-hands-check-the-turn-001` · beginner · turn · srp · ip · consensus 0.83 · sources: 2cc,br79,cc · **draft**

**Claim.** Range advantage means more of your hands want to bet; it never tells a specific hand to bet. A hand too weak to be called by worse and too strong to turn into a bluff checks: pocket nines on an ace-high board after one bet, kings through jacks on an ace turn, a strong but non-nut hand when a bet only folds out what you beat. One bet, then pot control.

**Why.** The reasons to bet have not changed: value, bluffing, a little denial. A middling hand gains none of them when the opponent's range splits into hands far ahead of you and hands far behind. The better hands call or raise, the worse hands fold, so a second bet buys nothing it did not already have, while a check keeps the pot small when behind and often earns a river call or bluff from the worse hands when ahead. In position, your checking range should contain some strong-but-not-nutted hands for exactly this reason. The exception is the very dry turn where the caller must continue with ace-high and unpaired hands: there second pair and small pairs become thin value bets, because they are ahead of what calls. Ask what calls before you decide which world you are in.

**Common mistake.** Barrelling nines on an ace-king-x board to 'find out', folding out the pairs you beat and paying off every ace.

**Schools disagree.** Some coaches bet second pair and even small pairs for value on very dry turns because the caller must continue with ace-high, while others make one bet with a medium pair and then stop regardless of texture.

**Hooks.** _You have the range advantage. Your hand still says check._ · _Pocket nines on A-K-x: one bet, then stop._ · _Second pair on the turn: one course value bets it, another pot controls. Here's the split._

Review: [ ]

### Protection is a tiebreaker, not a reason to bet
`c-cash-6max-x-protection-is-not-a-reason-to-bet-001` · intermediate · flop · srp · any · consensus 0.83 · sources: 2cc,cc,rio · **draft**

**Claim.** Decide first whether a bet is for value or as a bluff. Only then let protection nudge a close call. A hand that 'needs protection' is often a hand not strong enough to bet at all, and a bet only protects you against hands that hold real equity and actually fold.

**Why.** Protection means ending the hand before a free card lets a worse hand overtake you. That only happens against hands with live equity that release to your bet; a flush draw that calls was not protected against, and a hand with two undercards was never a threat. A denial bet asks a hand with 15-25% equity to fold, so the gain is at most that slice of the pot, while a value bet or a bluff can justify the chips on its own. Weak pairs under two or three overcards feel vulnerable, but they are often already behind, so betting builds a pot you are losing and exposes you to raises. Top pair on an ace-high flop is the opposite case: it rarely gets outdrawn by a folding hand, so it does not need the bet either. If denial is the only reason you can name, check.

**Common mistake.** Saying 'I bet to protect against the flush draw' when the flush draw calls, or betting pocket deuces on Q96 so they don't see a free card.

**Schools disagree.** Some coaches list protection as one of three drivers of c-bet frequency alongside nut advantage and fold equity, while others say it can never produce a bet on its own and only breaks ties between betting and checking.

**Hooks.** _'I bet to protect my hand' is the most expensive sentence in poker._ · _The flush draw calls. So what exactly did you protect?_ · _Three courses agree protection comes last. One gives it a vote._

Review: [ ]

### Range advantage sets how often you c-bet; nut advantage sets how big
`c-cash-6max-x-range-advantage-frequency-nut-advantage-size-001` · intermediate · flop · srp · ip · consensus 0.83 · sources: 2cc,cc,rio · **draft**

**Claim.** Two separate questions decide a flop c-bet. How much more equity does your whole range have than theirs? That sets frequency. Who holds more of the very strong hands (overpairs, sets, trips)? That sets size. Keep the dials apart: you can bet rarely and big, or everything and small.

**Why.** A weak opposing range has to fold more, which improves value bets, bluffs and equity denial at once, so a large equity edge means betting a big share of your range. Size is about the top of the two ranges. Hands near 85% equity want a fast-growing pot, so when your range is dense with them and theirs is not, bet big. When the caller can hold the nuts as easily as you (a paired rank they defend, three of a suit, an ace that beats your overpairs), a big bet mostly loads money against an uncapped range, so bet small even if you bet everything. An overpair on 982 is near the top of both ranges; on 654 or on a paired board the caller has caught up. The common turn spot, polarized bettor against condensed caller, is where the two dials happen to agree (rarely and big), which is why players confuse them.

**Common mistake.** Reasoning 'I only bet sometimes here, so I should bet big', or sizing up on a board where the opponent holds the nut region as often as you do.

**Numbers.** Small c-bet when the nut region is shared: about 25-33% pot

**Schools disagree.** Some coaches treat nut advantage as a driver of c-bet frequency as well as size, while others keep it strictly to size and let range equity alone set frequency. / What 'big' means differs: some coaches cap the large c-bet at about 75% pot, others use overbets of 115-150% on the same high-card textures.

**Hooks.** _You bet big because you bet rarely? That's backwards._ · _Two questions decide every c-bet. Most players only ask one._ · _Several top courses agree on how often to c-bet. They split on how big._

Review: [ ]

### On the river, check hands with showdown value and bluff everything below them
`c-cash-6max-x-showdown-value-decides-river-bluffs-001` · beginner · river · srp · ip · consensus 0.83 · sources: br79,cc,rio · **draft**

**Claim.** Find the weakest hand in your range that still wins at showdown often enough. Check it and everything above it that cannot bet for value. Bet everything below it. A pair is a showdown hand, not a bluff, even when the board gets scary; a hand that beats every fold and loses to every call has no reason to bet.

**Why.** A river bet does one of two things: gets called by worse or folds out better. A medium hand against a typical caller does neither, so betting it throws away the one thing it does well, which is winning at showdown for free. On the other side, a hand with no showdown value gains nothing by checking; a check and a fold are identical there, so any fold you collect is pure profit. Players tend to pick a few 'good-looking' bluffs and check the rest of their air, which leaves the betting frequency far too low. Whether ace-high is a check or a value bet depends on how much company it has: on low boards after two checks it is often near the top of your range and bets for value. And a profitable bluff can still be wrong if checking earns more, so compare bet to check for the hand you actually hold.

**Common mistake.** Betting middle pair on a brick river 'to represent the flush', folding out only ace-high and getting called by every pair.

**Schools disagree.** Some coaches tell micro-stakes players to skip river bluffs entirely because the pool does not fold, while others say missing the mandatory river bluff is the single biggest leak at those stakes.

**Hooks.** _Bottom pair is never a bluff. Not even on a four-straight._ · _The hand that beats everything that folds._ · _Bluff the river at NL5? One course says never. Two say you must._

Review: [ ]

### Second-barrel when the turn card hurts the hand they called with, not when it looks scary
`c-cash-6max-x-turn-barrel-by-caller-range-001` · intermediate · turn · srp · ip · consensus 0.83 · sources: 2cc,br79,cc · **draft**

**Claim.** After your c-bet is called, name the hands the caller most likely has and ask what the turn card does to them. A ten-to-king on a low board belongs to the raiser and gets barrelled often; a card that leaves their pair intact does not. Barrel selectively, around 40-60% on a blank, not your whole range: calling the flop made their range stronger.

**Why.** Betting the flop filters the caller: their air leaves, their pairs and draws stay, so on the turn they often hold the equity edge even though you keep the nut edge. That is why turn barrels are fewer and bigger than flop bets. The turn card is only one of five inputs, with preflop ranges, flop, flop action and position. High broadway turns on a low board favour you because the caller 3-bet many of those hands preflop and folded the rest to your flop bet. A card that gives their likely pair nothing, like a jack under their king, produces no folds. The ace is the contested card: it beats the pairs that called, but on a dry flop ace-high called the small c-bet too and now beats your overpairs. Against a specific player type, ask whether they are even capable of folding a pair before you fire.

**Common mistake.** Firing the turn on any 'new' card because the flop c-bet got called, without asking what the opponent holds and whether the card hurts it.

**Numbers.** Blank-turn barrel after a called c-bet: roughly 40-60% of your range in theory

**Schools disagree.** Some coaches call the ace the classic scare card to barrel because it beats the pairs that called, while others show the ace turn is often the worst overcard for the raiser on a dry flop, since ace-high called the small c-bet and now beats your overpairs. / Some coaches barrel scare cards against regulars but check them against recreational players who call any pair, while others say the population over-folds turns and you should bluff far above the solver's count.

**Hooks.** _The ace turn is a scare card for you, not for them._ · _They called your c-bet. Their range just got stronger._ · _Barrel the ace? One coach says yes, another calls it the worst card in the deck._

Review: [ ]

### Use one c-bet size per flop texture; it costs almost no EV
`c-cash-6max-x-one-cbet-size-per-texture-001` · intermediate · flop · srp · ip · consensus 0.75 · sources: 2cc,br79,cc,rio · **draft**

**Claim.** Pick a single c-bet size for each class of flop and use it with every hand you bet there. Decide only bet or check. A solver forced down to one size loses a negligible amount, and a strategy you can execute beats a multi-size tree you cannot.

**Why.** A raw solver output mixes four or five sizes plus a check, and each combo splits differently. Nobody plays that accurately, and execution errors cost far more than the simplification. When a solver is restricted to one size it compensates: it bets more often with a smaller size or less often with a bigger one, and it repairs the rest on the turn and river. On typical flops the EV matches the full mix to two decimal places. A single size also hides your hand, because bluffs and value look identical, and it makes later streets easier to study since each texture produces one pot size. Where two sizes both do real work on a texture, keep both and cut the check instead, but never carry more than two options into a flop.

**Common mistake.** Copying a multi-size solver output, applying it inconsistently, and bleeding more EV than the simplification would ever have cost.

**Numbers.** EV cost of one size per texture: hundredths of a big blind or within solver noise · Keep at most two options per flop texture: check plus one size, or two sizes with no check

**Schools disagree.** Some coaches say at micro stakes you should bet big with strong hands and small with weak ones because opponents there do not read sizing, while others say sizing that leaks hand strength is the most common small-stakes leak; the first is an exploit of inattentive recreational pools, the second a default against anyone who watches.

**Hooks.** _Solvers use four flop sizes. You need one._ · _We cut the solver to one bet size. The EV didn't move._ · _One course says bet big with your good hands at the micros. Three say never. Here's the fault line._

Review: [ ]

### Bluff more against players who fold the flop, not against players who call the river
`c-cash-6max-x-bluff-more-or-less-at-the-micros-001` · beginner · multi-street · srp · any · consensus 0.63 · sources: 2cc,br79,cc,rio · **draft**

**Claim.** The schools split on bluffing at low stakes. One side says under-bluffing is the biggest leak there, because the population over-folds when your range is ahead. The other says never bluff a player who does not fold. Both are right about different opponents: bluff more on flops and turns against unknowns and regulars, and stop bluffing rivers against proven stations.

**Why.** Fold equity is a reaction to your range and to the opponent. Solver-based coaches show that real players fold the flop more and call ace-high less than theory requires, so range-betting dry boards and barrelling your air prints against them, and checking down queen-high after three checks surrenders a pot your range owns. Micro-stakes exploitative coaches watch a different player: the loose passive caller who pays off with bottom pair and never folds a draw. Against that player a river bluff is donated money and the profit comes from value. The reconciliation is to tag the opponent first. Unknowns and typical regulars fold too much to early-street aggression; a tagged station does not fold at all, so redirect every bluff into a thinner value bet and call their small bets to see their hands.

**Common mistake.** Applying one bluffing policy to the whole table: barrelling a station off a pair, or checking down air against a regular who folds far above break-even.

**Schools disagree.** Some coaches say that at micro stakes the most frequent large blunder is failing to bluff and that when unsure you should bet, while others say at those same stakes you should make top pair, value bet and never bluff a river; the gap is the opponent model, thinking regulars versus loose passive callers. / On a scare-card turn some coaches barrel far above the solver's count because the population over-folds, while others check against recreational players who hold the scare card more often and call with any pair anyway.

**Hooks.** _Two courses, same stakes: 'bluff more' vs 'never bluff'. Both are right._ · _The leak that costs more than every bad call combined._ · _Stop bluffing this one player. Start bluffing everyone else._

Review: [ ]

### Ace-high flops in position: bet small, but how often is disputed
`c-cash-6max-x-ace-high-flop-cbet-001` · intermediate · flop · srp · ip · consensus 0.50 · sources: 2cc,cc,rio · **draft**

**Claim.** On an ace-high flop the raiser's c-bet is small, about a quarter to a third of the pot, because an ace on board lets any random ace beat your overpairs. Whether you fire that small bet with your whole range or check back a third of the time or more is where the schools split.

**Why.** Everyone agrees on why the size is small: the ace erases the nut advantage your overpairs gave you, and the caller holds plenty of weak aces that will not fold. The frequency argument runs two ways. One camp reads aggregate solver output as a near range-bet: the raiser has the clear range edge, the caller has few hands that can raise, and a quarter-pot bet taxes all the junk cheaply. The other camp points out that top pair and second pair on AQ2 need little protection, since a king or jack turn rarely lets a folded hand overtake you, and that two-tone ace-high flops give the caller many draws, so the solver lands near 33% c-bet on boards like AQ2 or A32 two-tone. Our read: rainbow ace-high with disconnected low cards is close to a range bet; add a flush draw or Broadway connectivity and the checks come back.

**Common mistake.** Auto-betting every ace-high flop 'because I have the ace in my range', or sizing up with top pair on A72 and splitting your range.

**Numbers.** Small c-bet on ace-high flops: ~25-33% pot

**Schools disagree.** Some coaches treat ace-high flops as a quarter-pot range bet at a very high frequency, while others show solver c-bet frequencies near 33% on ace-high two-tone flops and check back many top and second pairs. / Some coaches even overbet rainbow ace-high flops with two Broadway cards such as AK7 or AQ4, while others put every ace-high flop in the small-bet group.

**Hooks.** _Two solver-based courses, same flop, opposite answers._ · _Top pair on an ace-high flop doesn't need protection. So why bet?_ · _Everyone bets small on ace-high flops. Nobody agrees how often._

Review: [ ]

### Facing a flop check-raise: theory calls wide and almost never 3-bets; the micros disagree
`c-cash-6max-x-facing-flop-check-raise-001` · intermediate · flop · srp · ip · consensus 0.50 · sources: 2cc,br79,rio · **draft**

**Claim.** After c-betting in a single-raised pot and getting check-raised, theory continues with more than half of your hands, almost all by calling, and re-raises only a few percent. Defending enough with draws, backdoors and weak pairs matters far more than finding 3-bets. Against micro-stakes pools, where a raise is usually a real hand, coaches split on how much to fold.

**Why.** The check-raiser's range is wide and full of bluffs and semi-bluffs, so the in-position player must call with hands that feel uncomfortable: third pair, ace-high with a backdoor flush draw, suited backdoors. Re-raising adds little because the c-bettor's own range is tight; on a king-high flop the solver 3-bets under 1%, and even on a low paired board only about 4%. Then the opponent model takes over. Where the population check-raises with more draws than theory, 3-bet more and fold less; where it raises with stronger hands and less junk, fold most backdoors and keep only direct flush draws and the best backdoors. Micro-stakes coaches go further and treat a flop raise as a strong hand almost always, folding even top pair when barely invested.

**Common mistake.** Folding weak pairs and backdoor draws to a check-raise because they 'can't be good', or spending study time balancing a 3-bet range the solver barely uses.

**Schools disagree.** Some coaches say that facing a check-raise you should worry only about continuing enough, while others say at micro stakes a raise is almost always a real hand and folding top pair is routine; against regulars with wide check-raising ranges the first holds, against passive recreational pools the second. / Even the exploit direction splits by board: on a low paired two-tone flop the population raises more draws, so some coaches 3-bet about 22% and fold less; on a king-high flop the population raises stronger, so the same coaches fold most backdoor hands.

**Hooks.** _Check-raised with third pair? The solver calls. Here's why that scares people._ · _One raise, two schools: call it down or fold top pair._ · _The 3-bet you can delete from your game._

Review: [ ]


---

# PART 2. Single-source cards by topic


## fundamentals  (16)

### Before betting a one-pair hand, decide what you do if raised
`c-cash-6max-br1-think-ahead-before-betting-013` · beginner · flop · srp · ip · consensus 0.50 · sources: br79 · **draft**

**Claim.** With a hand like top pair weak kicker or a middle pair in position, ask what you will do if the opponent raises. If the honest answer is "fold", consider checking back instead, especially against an aggressive player who raises often.

**Why.** A bet that folds to a raise turns a hand with decent showdown value into a bluff you did not intend to make. Thinking one step ahead reveals this before the chips go in. Checking back keeps the pot small, keeps your hand's showdown value intact and denies the aggressive opponent the chance to blow you off it. Against a passive opponent the calculus changes, because the raise you fear rarely comes.

**Common mistake.** Betting on autopilot, getting raised, and only then realizing the hand cannot continue.

**Hooks.** _Ask one question before every bet. What if he raises?_ · _Top pair, bad kicker, aggressive villain. Check._ · _Most micro players bet first and think second._

Review: [ ]

### Decide early whether a hand is going all the way, then do not half-commit
`c-cash-6max-br4-plan-the-hand-009` · beginner · multi-street · any · consensus 0.50 · sources: br79 · **draft**

**Claim.** Before putting significant money in, have a general plan for the hand: either you are folding early or you are prepared to see a showdown. The worst outcome in poker is investing heavily and then folding before the river.

**Why.** Money put in and then abandoned has no chance of being recovered, so half-commitment combines the costs of both playing and folding. A simple plan formed at the start, based on opponent type, stack depth and your hand's playability, prevents that. Against a weak short stack with a strong one-pair hand the plan can be "we are stacking off"; with a marginal hand against an unknown it can be "fold at the first sign of trouble". The plan can bend with new information, but having one makes every later decision easier.

**Common mistake.** Calling a raise, calling a flop bet, calling a turn bet and then folding the river with the pot already huge.

**Hooks.** _The most expensive line in poker is call, call, call, fold._ · _Decide on the flop whether you are going to showdown._ · _A plan made early saves you a stack later._

Review: [ ]

### At NL10 play disciplined ABC poker; profit comes from avoiding mistakes, not fancy plays
`c-cash-6max-br7-play-abc-profit-from-avoiding-mistakes-001` · beginner · multi-street · any · consensus 0.50 · sources: br79 · **draft**

**Claim.** Each step from NL2 to NL5 to NL10 is a real jump in difficulty, but the winning approach stays the same: straightforward, disciplined poker. No light 4-bets, no river check-raise bluffs, no turning pocket threes into a bluff, no wide calls of 3-bets unless deep. The players who win big at these stakes are simply not making the spewy plays everyone else makes.

**Why.** Many players look for a magic trick to beat small stakes. There is none; the population loses by making unforced errors, and the winner is whoever makes the fewest. Big creative plays add variance and only work against opponents who think, which most of these opponents do not. Folding marginal hands, declining to bluff players who never fold, and waiting for weak players to hand over stacks looks boring on screen but it is where the win rate comes from. When unknowns play back at you early in a session, let them; do not shove money in for something to do.

**Common mistake.** Turning a medium hand into a bluff "because the board is scary", or 4-betting light against an unknown to feel in control of the table.

**Hooks.** _There is no trick to beating NL10. Here is what works instead._ · _The biggest winners at micro stakes make the fewest plays._ · _Stop turning pocket threes into a bluff._

Review: [ ]

### Classify every bet by how much equity the folded hands had
`c-cash-6max-cc03-equity-folded-spectrum-001` · beginner · multi-street · consensus 0.50 · sources: cc · **draft**

**Claim.** Judge what a bet is doing by the average equity of the hands your opponent folds, not by whether you "had the best hand". Near 0% folded equity means a value bet, 15-30% means value plus denial, around 50% is a bluff-denial hybrid, and 75-100% is a pure bluff.

**Why.** Whether you were technically ahead is a poor label because it makes 50% a magic number. What matters is how much of the pot the folded hands would have won at showdown. When a flush draw bets and makes ace-high fold on the flop, the opponent surrendered roughly half the pot, so there is a real bluffing component even though the draw may have been the favourite. Fold equity (how often he folds) and equity folded (what he gave up when he did) are different quantities, and the second one tells you why the bet made money.

**Common mistake.** Calling any bet with the current best hand a "value bet" and any bet with the worst hand a "bluff", ignoring how much the folded hands would have won.

**Numbers.** ~0% equity folded: value bet · ~15-30% equity folded: value/denial · ~50% equity folded: bluff-denial · 75-100% equity folded: pure bluff

**Hooks.** _Your 'value bet' might actually be a bluff._ · _Stop asking who had the best hand. Ask what folded._ · _Four kinds of bet, one scale. Here it is._

Review: [ ]

### A profitable bluff is still a blunder when checking makes more
`c-cash-6max-cc03-profitable-but-wrong-007` · beginner · river · srp · consensus 0.50 · sources: cc · **draft**

**Claim.** Never evaluate a bluff by whether it beats the break-even fold frequency. Weigh what a bet earns against what a check earns, because a check is not worth zero; a fold is. With real showdown value, a bet that makes money can still cost you a large chunk of the pot.

**Why.** Take a river where the pot has been checked down and you hold king-high with a strong range on an ace-high paired board. Betting 3/4 pot needs about 43% folds to break even and the opponent folds far more than that, so the bet is profitable. But checking wins the pot very often, so the check is worth even more. In one such solver spot, checking was worth about 47% of the pot while a small bet earned 42% and a 4x-pot overbet still showed +27% of the pot: profitable, and still a mistake. Choosing a thousand when you were offered two thousand is not a good decision just because you ended up richer.

**Common mistake.** Saying "he folds more than 43% so this bet is good" and never asking what the hand would have earned by checking.

**Numbers.** 75% pot bet breaks even at ~43% folds (3 into 7) · 33% pot bet breaks even at 25% folds (1 into 4) · example river: check ~47% pot EV vs bet ~42% (small) or ~27% (4x pot)

**Example.** positions: CO vs BB | hero: KhJd | board: Ac 4s 4d 8h 2c | action: CO opens, BB calls. Checks through on flop and turn. BB checks river. | decision: Bet 75% pot or check? | answer: Check. The bet is profitable against the fold frequency, but king-high wins at showdown so often that checking earns clearly more.

**Hooks.** _This bet makes money. It's still a huge mistake._ · _Which poker action is worth zero? Not checking._ · _'He folds more than 43%' is not a reason to bet._

Review: [ ]

### Having more sets or more nutted combos does not give you range advantage
`c-cash-6max-cc06-nut-advantage-is-not-range-advantage-004` · intermediate · flop · any · consensus 0.50 · sources: cc · **draft**

**Claim.** Nut advantage is a component of range advantage, not a substitute for it. A range can hold more of the very best hands and still have less total equity than the opponent's range.

**Why.** Think of two sets of numbers. One contains a 12, a 10 and an 8 and sums to 10 because the rest are tiny; the other has nothing above 8 but sums to 15. The second set is "stronger" even though the first has all the best individual pieces. Ranges behave identically. Humans remember the dramatic hands - the set that stacked someone, the flush that got there - so we overweight them when we size up a spot. The best hands matter, but they are only a few combos inside a range of two hundred. Assess the whole distribution first, then look separately at the top end when you decide how big to bet.

**Common mistake.** Saying "we have more sets here, so we have range advantage" and betting as if the whole range were ahead.

**Hooks.** _More sets than villain? Still doesn't mean you're ahead._ · _The nut advantage trap that fools most regs_ · _Your brain is magnetized to the nuts. Fix that._

Review: [ ]

### Nut advantage is about hands with roughly 85%+ equity, not the literal nuts
`c-cash-6max-cc06-nutted-means-85-percent-equity-010` · intermediate · flop · any · consensus 0.50 · sources: cc · **draft**

**Claim.** When assessing nut advantage, count every hand with very high equity - around 85% or more against the opponent's range - not only the single best possible holding. On low dry boards that is mostly overpairs, and overpairs are far more numerous than sets.

**Why.** The literal nuts are a tiny part of any range. A set is three combos; a flopped set on a board where pocket pairs are a small part of a range might be 3% of it. Overpairs that the opponent cannot hold can be 24 combos or more, sitting at 85-90% equity. Twenty-four combos at 90% beat three combos at 96% by a wide margin, just as eleven payments of 100 beat three payments of 150. So an overpair on a seven-three-deuce board is a real nut-advantage contributor, while the opponent's extra sets barely register. Treating "nuts" literally makes you give away edges on exactly the boards where your overpairs dominate.

**Common mistake.** Deciding the opponent has the nut advantage because they can hold small sets you cannot, while ignoring that your range holds dozens of unbeatable-in-practice overpairs.

**Numbers.** Nutted threshold used: roughly 85%+ equity vs the opponent's range · A set is 3 combos; in a ~200-combo defending range, 6 set combos is ~3% · Example raiser range: 24 combos of JJ+ out of ~224 is ~11% of the range at ~86-87% equity

**Hooks.** _'He can have a set' is 3% of his range._ · _The nuts is not what you think it is._ · _24 overpairs beat 3 sets. Every time._

Review: [ ]

### A range almost never has more than 60-70% equity, so 55% is already a big edge
`c-cash-6max-cc06-range-equity-rarely-exceeds-70-012` · beginner · flop · any · consensus 0.50 · sources: cc · **draft**

**Claim.** Because every range carries some hands that miss any given flop, range-vs-range equity on the flop tops out around 60-70% even in lopsided spots. Calibrate accordingly - 55% for a range is a healthy advantage, not a marginal one.

**Why.** A single hand can easily hold 80 or 90% equity. A range cannot, for the same reason that 25 random people cannot all be in the top tenth of anything. Even the preflop raiser on a favorable board holds small pairs that missed and suited aces that whiffed, and those drag the average down. So when you see a range sitting at 55% you should read it as "clearly ahead" and when you see 66% as "enormous". This matters because players who expect hand-like numbers from ranges either dismiss real advantages as small or imagine advantages that are not there.

**Common mistake.** Looking at a 55% range equity figure and concluding the ranges are roughly even.

**Numbers.** Flop range equity rarely exceeds ~60-70% even with a huge advantage · ~55% range equity in position on a middling board = a sizable edge

**Hooks.** _55% equity sounds small. For a range it's huge._ · _Why no range ever has 80% equity_ · _One number that recalibrates how you read range advantage_

Review: [ ]

### A small range advantage should be treated as no advantage at all
`c-cash-6max-cc06-small-range-advantage-is-no-advantage-002` · intermediate · flop · any · consensus 0.50 · sources: cc · **draft**

**Claim.** Only talk about having a range advantage when the gap in range-vs-range equity is sizable. If your range is a few points ahead, treat the spot as roughly even and build your strategy from there.

**Why.** The question is never "who is ahead" but "by how much". Two armies of a million and 999,999 are equal for planning purposes, and so are two ranges split 51/49. The strategic consequences of range advantage, such as betting your whole range, only follow when the edge is big enough to make the opponent fold a lot of weak hands. Labeling a tiny edge as an advantage tempts you into over-aggression that the actual equity does not support. On the flop a strong edge looks like 60-70% range equity; 55% is already meaningful, but anything close to half is just a coin flip between two teams of hands.

**Common mistake.** Announcing "I have range advantage" in nearly every spot as the preflop raiser and using it to justify betting everything.

**Numbers.** Range-vs-range equity of ~55% is a real edge; 60-70% on the flop is a very large one · Anything near 50/50 should be treated as no advantage

**Hooks.** _'I have range advantage' is the most abused phrase in poker._ · _51% is not an advantage. It is a coin flip._ · _How much range advantage you need before it changes anything_

Review: [ ]

### Range advantage comes from fewer trash hands as much as from more strong ones
`c-cash-6max-cc06-three-sources-of-range-advantage-003` · intermediate · flop · any · consensus 0.50 · sources: cc · **draft**

**Claim.** Range advantage is whole-range equity against whole-range equity. It is built from three things at once - a higher share of very strong hands, a higher share of decent hands, and a lower share of garbage. The missing garbage is the part almost everyone forgets.

**Why.** A team with one superstar and ten children loses. A team of eleven solid players is hard to beat. Ranges work the same way. The preflop raiser on a dry middling board does not lead mainly because of their overpairs; they lead because the big blind is stuffed with low suited junk that whiffed, while the raiser's worst hands are still two overcards. Every weak combo your opponent carries drags their range equity down, and every one you do not carry pulls yours up. So when you assess a flop, ask what both ranges are weighted toward and away from, across the full distribution, not just who holds the monsters.

**Common mistake.** Judging range strength only by the top end ("I can have AA and KK, they can't") and ignoring how much junk each range carries.

**Hooks.** _The reason you have range advantage is not your overpairs._ · _Be grateful for the trash hands you don't have._ · _Range advantage: it's about the bottom, not the top_

Review: [ ]

### Betting a polarized flop range raises your nut share, not your equity
`c-cash-6max-cc07-polarized-betting-concentrates-nuts-005` · intermediate · flop · srp · ip · consensus 0.50 · sources: cc · **draft**

**Claim.** When you bet the flop with your strongest hands and your bluffs while checking the middle, your betting range's equity barely rises but its share of nutted hands jumps. Ranges work by concentration and dilution, not just by combo counts.

**Why.** Think of a bucket of mixed balls: remove the mediocre ones and the chance of drawing a premium one goes up, even though you added nothing. Checking back medium pairs and weak ace-highs removes the filler from your betting range; the sets and overpairs that were always betting now make up a larger fraction. Because you also bet plenty of air, overall equity moves only slightly. This is why a c-bettor who bets 40% of the time can still arrive on the turn with a large nut advantage while trailing in equity. The caller, by contrast, checks every hand first, so nothing about their range changes until they call and shed their junk.

**Common mistake.** Measuring your range only by how many strong combos you hold, and not by how concentrated they are after your line removes the medium hands.

**Hooks.** _Betting less often can make your range scarier._ · _Your nut advantage comes from what you check, not what you bet._ · _Ranges are concentrations, not combo counts._

Review: [ ]

### Range advantage is about equity; favorability is about EV
`c-cash-6max-cc07-range-advantage-vs-favorability-003` · intermediate · turn · srp · any · consensus 0.50 · sources: cc · **draft**

**Claim.** Having a range advantage means your range has more equity than theirs. A favorable world means your range has more EV, counting position, nut share and future streets. On most turn barrel spots the flop caller holds the equity edge while the bettor holds the EV edge.

**Why.** Equity only measures who wins at showdown if all money went in now. EV also captures who gets paid, who gets folds and who controls the pot. After a flop bet and call, the caller has discarded their junk, so their average hand is stronger and their equity is often above 50%. The bettor, however, kept almost all the nutted hands and far more bluffs, so their range is polarized. Polarized ranges earn more than their equity suggests because the nuts are entitled to well over 100% of the current pot once future bets count, and the bluffs still collect fold equity. So a condensed range can hold 55% equity and still be the one with 42% of the pot in EV. To be in an unfavorable world while holding the range advantage, you must be the condensed range facing a polarized one.

**Common mistake.** Saying "this turn is bad for me, they have the equity now" and shutting down, when your nut advantage and position still make the spot profitable to barrel.

**Numbers.** A nutted overpair on a favorable turn is worth roughly 150-200% of the current pot in EV · Typical blank-turn barrel spot: bettor ~57-58% pot EV while caller has the equity edge

**Hooks.** _They have more equity. You have more money. Both are true._ · _'Range advantage' and 'good spot' are not the same thing._ · _How can 55% equity be a losing spot?_

Review: [ ]

### On more connected low flops, gutshots push weak overcards and small pairs out
`c-cash-6max-gp30-gutshots-replace-overcards-008` · advanced · flop · srp · oop · consensus 0.50 · sources: rio · **draft**

**Claim.** Move the cards of a low flop closer together so that single-card gutshots exist and, facing the same 75% pot c-bet, more gutshots continue while weak pairs and single-overcard hands fold more. The overcard hands that remain need extra qualities, such as a second overcard plus a backdoor flush draw to the nuts.

**Why.** This is not about swapping hand classes to hit a defense frequency. The caller's range on a more connected board contains many more front-door draws, and the raiser's range does too, so an overcard hand that was comfortably ahead of air on a disconnected board now has less equity and worse realization. Gutshots, especially those drawing to the nuts or carrying backdoor equity, simply have more equity than the overcards they displace. The folding threshold moves because the hands' equities moved, and that is the mindset to carry into any texture you have not studied.

**Common mistake.** Keeping the same "any two overcards continue" rule on 865 that worked on 843 and calling with hands that are now clearly behind.

**Numbers.** vs 75% pot on connected low flops: gutshot-plus continues; weak pairs and single overcards fold more

**Hooks.** _843 or 865: only one lets you call ace-high._ · _Why your overcards lost value when the board got connected._ · _It is not about MDF. Your hand just got worse._

Review: [ ]

### Wanting protection does not make a hand strong enough to bet for protection
`c-cash-6max-gp35-protection-needs-strength-012` · beginner · flop · 3bet-pot · ip · consensus 0.50 · sources: rio · **draft**

**Claim.** A small pocket pair on a flop with overcards is vulnerable, but vulnerability alone is not a reason to bet. A protection bet needs a hand that is actually ahead often enough that denying equity is worth the risk; weak pairs usually just check and sometimes fold.

**Why.** Protection bets work when you are ahead of most of the range and the opponent has live cards to fold out. A low pocket pair under two or three overcards is often behind already, so a bet does not protect a lead; it builds a pot you are losing and exposes you to raises. The feeling that a hand "needs protection" is a signal of weakness, not a licence to bet. Check it, take your showdown value, and let the hand go when the action gets heavy.

**Common mistake.** Betting pocket deuces on a Q-9-6 flop "so they don't see a free card".

**Hooks.** _'I'm betting for protection' is costing you money._ · _Your small pair doesn't need protection. It needs a check._ · _Protection bets need a lead. Do you have one?_

Review: [ ]

### An overpair is worth more on 982 than on 654
`c-cash-6max-tc13-overpair-value-depends-on-board-002` · intermediate · flop · srp · btn · consensus 0.50 · sources: 2cc · **draft**

**Claim.** The same overpair is a much stronger betting hand on a high-ish disconnected flop than on a low connected one, so size it up on boards like 982 and keep it smaller on boards like 654.

**Why.** Hand strength is relative to what the opponent's range can hold. On 982 the big blind has plenty of nines, eights and pairs below jacks that an overpair beats, and few hands that beat it, so pocket jacks can extract with a very large bet. On 654 the big blind's calling range is full of sevens, eights, small pairs and suited connectors that already have sets, two pair or big draws, so jacks are ahead of less and get raised more. The card ranks that connect with the board decide how much your overpair is worth, not the overpair itself.

**Common mistake.** Treating every overpair as the same hand and betting it the same size regardless of the flop.

**Numbers.** JJ on 982: solver's preferred single size is an overbet (~169% pot in the full solve) · JJ on 654: far less value, small size preferred

**Hooks.** _Pocket jacks on 982 and on 654 are not the same hand._ · _Your overpair just lost half its value. Here's the board._ · _Checking back jacks here makes you more money._

Review: [ ]

### Protection only counts hands that would fold and still have real equity
`c-cash-6max-tc15-protection-definition-006` · intermediate · flop · srp · btn · consensus 0.50 · sources: 2cc · **draft**

**Claim.** When weighing whether to bet for protection, count only the opponent's hands that hold meaningful equity against you and would fold to the bet. Draws that call anyway are not a protection argument.

**Why.** Protection means ending the hand before a free card lets a worse hand overtake you. With pocket sevens on KK6, a bet makes the big blind fold T9, which had two overcards and about a quarter of the equity; that fold is pure gain. But a nine-out flush draw or an eight-out straight draw is not going anywhere when you bet, so betting does not deny them anything on this street. Confusing the two leads players to 'protect' against hands that never fold, which is just betting into a calling range. Ask which hands with equity will actually release?

**Common mistake.** Saying 'I bet to protect against the flush draw' - the flush draw calls, so nothing was protected.

**Example.** positions: BTN vs BB | hero: 7h7c | board: KsKd6c | action: BTN opens, BB calls. BB checks the flop. | decision: Bet or check back? | answer: Bet. The big blind folds overcard hands like T9 and Q8 that would outdraw sevens on many turns, and those folds are the whole point of the bet.

**Hooks.** _'Betting to protect against the flush draw' makes no sense._ · _Protection is about hands that fold. Not hands that call._ · _Pocket sevens on KK6. Why the bet is mandatory._

Review: [ ]


## preflop-ranges  (23)

### Heads-up against a weak player, raise roughly 80-85% of buttons
`c-cash-6max-br1-headsup-button-range-003` · beginner · preflop · btn · consensus 0.50 · sources: br79 · **draft**

**Claim.** When a table is down to two players and your opponent is recreational, open about 80-85% of hands from the button and fold only the pure trash such as 9-3 offsuit or T-2 offsuit. Out of position, call sparingly and 3-bet occasionally rather than flatting a lot.

**Why.** Two-handed, the blinds come around every other hand, so folding costs far more than it does 6-max. The button has position on every postflop street and a weak opponent will fold too often preflop and play badly when they do defend. That makes raising almost anything profitable. The reverse also holds: without position you should stay disciplined, because the same positional edge is now working against you.

**Common mistake.** Playing a standard 6-max button range heads-up and bleeding blinds, or calling wide from the big blind and getting out-positioned every hand.

**Numbers.** Heads-up button open frequency: ~80-85% · Fold only the bottom ~15%, e.g. 9-3o, T-2o

**Hooks.** _Heads-up, folding the button is a leak. Here is the range._ · _Ten-deuce offsuit: the one hand you fold heads-up._ · _You should raise four out of five buttons here._

Review: [ ]

### Raise limpers with a wide range, especially when they limp your blind
`c-cash-6max-br1-isolate-limpers-006` · beginner · preflop · ip · consensus 0.50 · sources: br79 · **draft**

**Claim.** When a weak player open-limps, isolate with a wide range rather than limping behind or folding marginal hands. Keep doing it even after they call a few times; you will not win every pot, so let a missed flop go and attack again next time.

**Why.** Open-limping is close to a confession: strong players almost never do it, so the limper is usually a weak player with a weak range. Raising gives you the initiative, builds a pot against the person you want to play with, and frequently wins a c-bet on the flop when they miss, which is most of the time. If they call and the flop is bad for you, one give-up costs little compared with the pots you take down and the stacks you win when you both connect.

**Common mistake.** Letting players limp into your blinds for free, or quitting the isolation plan after one failed c-bet.

**Hooks.** _Someone limps into your blind. Raise. Every time._ · _A limp tells you more than fifty hands of stats._ · _Limpers are inviting you to take the pot. Accept._

Review: [ ]

### Against someone shoving every hand, call with an average hand or better
`c-cash-6max-br2-call-open-shover-003` · beginner · preflop · any · consensus 0.50 · sources: br79 · **draft**

**Claim.** When a short-stacked player open-shoves hand after hand, stop stealing their blinds and simply wait to call. Heads-up, roughly Q7 offsuit and better is above average against a random hand and is a profitable call. Do not open hands you would not be happy calling an all-in with.

**Why.** A player who jams every hand has a random range. Against a random hand, a holding like Q7 or better wins more than half the time, and the pot already contains their blind, so the call shows a clear profit. Trying to steal becomes pointless because they will shove regardless, and opening weak hands just forces you to fold to the jam. Variance is high, but getting a stack in preflop with 55-60% equity repeatedly is about as good as poker gets.

**Common mistake.** Folding everything but premiums to a maniac and letting someone else at the table collect the stack.

**Numbers.** Heads-up vs random hand: call Q7o or better

**Hooks.** _He shoves every hand. Here is exactly what to call with._ · _Queen-seven is a snap call here. Really._ · _Stop stealing. Start calling. He is giving it away._

Review: [ ]

### Do not 3-bet weak players light; flat and use your postflop edge
`c-cash-6max-br2-flat-dont-3bet-fish-006` · beginner · preflop · ip · consensus 0.50 · sources: br79 · **draft**

**Claim.** Against a recreational opener, 3-bet for value with strong hands but do not re-raise speculative hands or push for 100 big blinds preflop. Calling in position and letting them make mistakes after the flop keeps your edge intact and your variance low.

**Why.** Your advantage over a weak player is largest postflop, where they call with nothing, bet odd amounts and give off information every street. A light 3-bet or a preflop stack-off turns a hand you would dominate over three streets into a near coin flip decided before any of those mistakes happen. Flatting keeps the stack-to-pot ratio high so that their later errors are expensive for them. Save the 3-bets for hands that want to build the pot on their own merit.

**Common mistake.** Re-raising every fish open "to isolate" and then being forced to play a bloated pot with a hand like K9.

**Hooks.** _Stop 3-betting the fish. You are throwing away your edge._ · _The fish makes mistakes after the flop. Let him get there._ · _A preflop flip is the worst way to play a fish._

Review: [ ]

### Raise instead of limping; your own database will show roughly double the win rate
`c-cash-6max-br3-raise-dont-limp-010` · beginner · preflop · ip · consensus 0.50 · sources: br79 · **needs-review** · review note: _Conclusion fine, but the 2x win-rate evidence is selection-biased. Rewrite why before publishing._

**Claim.** Enter pots with a raise, not a limp, including when isolating a limper in position. If you doubt it, filter your tracker for hands where you raised preflop versus hands where you limped: the raised hands typically earn about twice as much, often more.

**Why.** Raising gives you the initiative, which lets you take down pots with a c-bet when everyone misses, builds a bigger pot for the times you connect and earns some respect so your later bets are credited. Limping does none of those things and invites more players into the pot behind you. When isolating a weak limper deep-stacked, a larger raise such as 8 big blinds is fine, since they call anyway and the extra money goes in while you have position and the better hand.

**Common mistake.** Limping behind a fish with a speculative hand "to see a cheap flop" and playing a multiway pot with no initiative.

**Numbers.** Win rate when raising preflop ~2x or more vs limping (coach's own tracker) · Iso-raise up to ~8bb vs a deep-stacked fish

**Hooks.** _One filter in your tracker ends the limping debate._ · _Raise or limp? Your database already answered._ · _Limping cuts your win rate in half. Literally._

Review: [ ]

### Choose light 3-bets from hands just below your calling range, not from it
`c-cash-6max-br4-light-3bet-below-calling-range-011` · beginner · preflop · btn · consensus 0.50 · sources: br79 · **draft**

**Claim.** On the button facing a weak-looking open, the hands to occasionally 3-bet light are ones you would not call with, such as a suited connector a notch too weak or an ace-rag with a blocker. Hands you are happy to flat should keep flatting.

**Why.** Re-raising a hand you would otherwise call does not add anything: you lose a profitable call and replace it with a higher-variance bluff. Re-raising a hand that would otherwise be folded turns zero into positive expectation if the opener folds often enough. Ace-rag works because the blocker makes it slightly less likely the opener holds a premium ace, and because the hand plays badly as a call anyway. Keep the frequency low at micro stakes, where most opponents call 3-bets too much.

**Common mistake.** 3-betting medium-strength hands like K-J for "balance" and folding to the 4-bet, when a call would have been clearly profitable.

**Hooks.** _Which hands to 3-bet light? The ones you were folding._ · _Stop 3-betting your calling hands. It costs you twice._ · _A light 3-bet should come from the trash, not the middle._

Review: [ ]

### Do not squeeze out of position when the opener is very tight
`c-cash-6max-br4-no-squeeze-oop-vs-nit-010` · beginner · preflop · multiway · oop · consensus 0.50 · sources: br79 · **draft**

**Claim.** When a tight player opens and several weak players call, resist the squeeze from the blinds with a speculative hand. In position you would call and play against the fish; out of position against a strong opening range, fold.

**Why.** A squeeze works when the opener's range is wide enough to fold and the callers are weak enough to give up. A player who has entered one pot in ten hands has a range that is not folding, so the squeeze turns into a re-raise into strength. Calling out of position is also poor because every postflop street starts with you acting blind. In position the multiway pot with several weak callers is attractive and a call is correct; the blinds are not that spot.

**Common mistake.** Squeezing from the small blind with a suited connector because "there is a lot of dead money" while ignoring who opened.

**Hooks.** _Dead money is a trap when the opener is a nit._ · _Squeezing a tight opener is just a re-raise into aces._ · _The squeeze spot that is really a fold._

Review: [ ]

### Pocket tens facing an open is mostly a 3-bet, not a call
`c-cash-6max-br4-tens-3bet-007` · beginner · preflop · ip · consensus 0.50 · sources: br79 · **draft**

**Claim.** Against a normal open, re-raise pocket tens for value most of the time. Flat only against a very tight opener whose range is dominated by bigger pairs and strong broadways.

**Why.** Tens are far ahead of a typical open-raising range and benefit from building the pot while they are still the best hand. Calling invites multiway action, where a medium pair plays poorly on the many flops with overcards. The hand's one weakness is that a 4-bet is awkward, but at micro stakes 4-bets are rare and usually mean exactly what they look like, so you can fold without much regret. Against a nit whose opens are mostly premiums the value disappears, and a set-mining call is the better line.

**Common mistake.** Flatting tens by default to "see a flop" and then being lost on a K-high board multiway.

**Hooks.** _Pocket tens is a 3-bet. Here is the one exception._ · _Stop set-mining with tens against a normal open._ · _Medium pairs hate multiway pots. Re-raise to avoid them._

Review: [ ]

### Call rather than 3-bet light against weak players; keep them in the pot
`c-cash-6max-br5-call-dont-3bet-light-vs-fish-010` · beginner · preflop · ip · consensus 0.50 · sources: br79 · **draft**

**Claim.** Against a typical loose passive player, do not 3-bet marginal hands like queen-jack suited in position; call. Your edge after the flop is huge, especially in position, and a 3-bet often folds out the very player you wanted to play against. The exception is a loose player who raises 30% of hands: 3-bet medium pairs such as eights and nines and good broadways for pure value.

**Why.** A light 3-bet works by winning the pot preflop or by playing a bloated pot with initiative. Against a weak player neither matters much: you would rather see a flop with them cheaply and let them make postflop mistakes across three streets, which they will. Folding them out with queen-jack is throwing away the most profitable situation in the game. Against a player who raises very wide, though, your medium hands are far ahead of their range, so 3-betting becomes a value play rather than a bluff and you want the call.

**Common mistake.** Treating every weak-player open as a 3-bet-for-isolation spot and watching them fold hands that would have paid you off postflop.

**Numbers.** vs a player raising ~30% of hands, 3-bet 88 and 99 for value

**Schools disagree.** Many modern coaches recommend 3-betting weak players wide for value and isolation; this coach prefers flatting to keep the weak player in, reserving 3-bets for clear value.

**Hooks.** _Stop 3-betting the fish. Seriously._ · _Queen-jack suited versus the table fish: call, do not raise._ · _We studied how coaches treat weak players preflop. They disagree._

Review: [ ]

### Cold-call more preflop when deep, in position, with a weak player in the blinds
`c-cash-6max-br5-flat-more-deep-ip-with-fish-behind-006` · beginner · preflop · srp · ip · consensus 0.50 · sources: br79 · **draft**

**Claim.** The default versus an open is 3-bet or fold, with pocket pairs as the main calling hands. Widen that calling range considerably when three things line up: stacks are deep, you have position on the raiser, and a weak player sits in the blinds who will come along. In that spot 3-betting with suited broadways mostly folds out the player you want in the pot.

**Why.** Cold-calling is weak in general because you play a capped range without initiative. But deep stacks raise the value of implied odds, position lets you realize equity with hands like ten-nine suited, and a loose player behind you adds dead money and a target for every street. Those factors swing marginal hands from fold to call. A 3-bet would get called by the raiser's pairs and draws while blowing the weak player out, which is the opposite of what you want.

**Common mistake.** Mechanically 3-betting or folding every hand without noticing the 100% VPIP player sitting in the big blind with 150bb.

**Hooks.** _3-bet or fold? Not when the fish is in the blinds._ · _Three conditions that turn a fold into a call preflop._ · _Why we stopped 3-betting here and started calling._

Review: [ ]

### Set-mine only when the raiser has enough stack to pay you off
`c-cash-6max-br5-set-mine-needs-stack-depth-008` · beginner · preflop · srp · any · consensus 0.50 · sources: br79 · **draft**

**Claim.** Calling a raise with a small pocket pair is a bet on flopping a set, so the raiser needs a deep enough stack to make the rare hit worth it. A 100bb raiser is plenty. Around 60-65bb it is marginal; continue only if a weak player is also in the pot or you have position. Against a min-raise the call is easy regardless.

**Why.** Small pairs rarely improve, so almost all their value comes from winning a big pot when they do. If the raiser has a short stack there is no big pot to win, and the call is just a slow leak. Extra factors can rescue a borderline spot: a loose player already in the hand adds implied odds from a second source, and position helps you extract when you hit. Check stack sizes before every set-mining call, not after.

**Common mistake.** Auto-calling raises with pocket deuces against a 40bb stack and wondering why set-mining never seems to pay.

**Numbers.** 100bb starting stack is plenty for set-mining · ~60-65bb is marginal; needs a weak player in the pot or position to continue

**Hooks.** _Pocket deuces are a fold here. Check his stack._ · _Set-mining only works if there is a stack to win._ · _The number you must check before calling with a small pair._

Review: [ ]

### Stats from short-handed play run loose; a normal 6-max game should be tighter than 30/28
`c-cash-6max-br6-do-not-copy-loose-video-stats-013` · beginner · preflop · any · consensus 0.50 · sources: br79 · **needs-review** · review note: _Coach commenting on own on-camera stats; near-duplicate of br8-014._

**Claim.** Numbers like 30/28 or 27/24 come from sessions with a lot of heads-up and three-handed play, which inflates VPIP, PFR, steal and 3-bet percentages. In a normal six-handed game play tighter, and keep your 3-bet around 4% rather than 5% or more.

**Why.** Short-handed hands force you into the blinds and the button far more often, so the same strategy produces much looser aggregate stats. Copying those numbers at a full 6-max table would mean opening and 3-betting hands that lose money against five opponents. Compare your stats with the game type you actually played, and when in doubt err towards tight: the micro-stakes edge comes from value and discipline, not from frequency.

**Common mistake.** Seeing a coach or winning player at 30/28 and forcing those numbers at a six-handed table full of regulars.

**Numbers.** normal 6-max 3-bet frequency ~4%; 5% shown was inflated by short-handed play · 30/28 and 27/24 session stats were skewed by heads-up and 3-handed hands

**Hooks.** _Do not copy a coach's video stats. Here is why._ · _30/28 looked great in the video. It will lose you money._ · _Short-handed hands are inflating your VPIP._

Review: [ ]

### Short-handed against weak players, raise 80-90% of button hands and fold only junk
`c-cash-6max-br6-heads-up-button-range-vs-weak-players-001` · beginner · preflop · btn · consensus 0.50 · sources: br79 · **needs-review** · review note: _Duplicate of br1-headsup-button-range-003. Keep one._

**Claim.** When a 6-max table is down to two or three players and the opponent is weak, open roughly 80-90% of hands from the button. The 10-15% you fold are the true junk hands: ten-three, nine-three, eight-two, seven-deuce offsuit and the like. Against a limp-in from them, raise with the same wide range.

**Why.** Heads-up, any hand with a face card or a connection is ahead of a random hand, and weak players fold the blinds too often and play badly after the flop. Raising wide buys the initiative cheaply and lets you win most pots with a c-bet or by simply making top pair. The few hands you fold have no playability and no showdown value, so even against a bad player they lose money. If the opponent turns out to be competent, do not stay; short-handed tables fill up quickly anyway.

**Common mistake.** Playing a full-ring range when the table is three-handed, folding the button with jack-six and letting a weak player collect blinds for free.

**Numbers.** raise 80-90% of button hands heads-up vs a weak player · fold the bottom 10-15%: T3o, 93o, 82o, 72o type hands

**Hooks.** _Heads-up on the button? Raise almost everything._ · _The only hands we fold heads-up against a weak player._ · _Short-handed tables scare you? Here is the whole plan._

Review: [ ]

### Against players who never give you credit, 3-bet big for value and skip light 3-bets
`c-cash-6max-br7-3bet-big-for-value-vs-players-who-give-no-credit-012` · beginner · preflop · 3bet-pot · any · consensus 0.50 · sources: br79 · **draft**

**Claim.** Many micro players call 3-bets with any two after you have shown aggression once, because they do not believe you. Against them, a light 3-bet is a bad bluff, so fold the marginal hands instead. When you do have a big hand, 3-bet, and 3-bet larger than normal; they will call anyway.

**Why.** A 3-bet bluff needs folds; a 3-bet for value needs calls. The fickle, stubborn opponent gives you the second and not the first, so your 3-betting range against them should be nearly all value, sized to extract. Bluffing them preflop just builds a pot out of position with a weak hand against someone who will not fold on later streets either. The adjustment is simple and highly profitable: polarize towards value, size up, and let their disbelief pay you.

**Common mistake.** 3-betting queen-jack as a bluff against a player who has just called two 3-bets with junk, then giving up on the flop.

**Hooks.** _He will not fold to your 3-bet. Good. Make it bigger._ · _Light 3-bets are wasted on this player type._ · _When disbelief becomes your profit source._

Review: [ ]

### Isolate limpers very wide in position, but keep real standards out of position
`c-cash-6max-br7-isolate-wide-in-position-keep-standards-oop-009` · beginner · preflop · limped · oop · consensus 0.50 · sources: br79 · **draft**

**Claim.** Raising limpers is one of the best plays at micro stakes, but tighten up when the limper will have position on you. In position almost any suited ace or two broadway cards is a raise; from the blinds a hand like ace-three offsuit is the bottom of the range or a fold, and king-eight is a check. Pots are simply harder to win when you act first on every street.

**Why.** Isolating a limper works because you win the pot preflop or with one c-bet most of the time, and position makes both easier: you see whether they continue before you commit more. Out of position you have to bet blind into their range on every street and cannot take free cards, so marginal hands turn into expensive guesses. Having higher standards out of position keeps your isolation plays profitable instead of just frequent.

**Common mistake.** Raising every limper with any ace from the small blind, then facing three streets of decisions out of position with a hand that only makes weak pairs.

**Hooks.** _Isolate every limper? Not from the blinds._ · _Ace-three offsuit: raise in position, check out of position._ · _Position decides how wide you can punish limpers._

Review: [ ]

### Raise nearly any two in position against a player who posts in or limps into your blind
`c-cash-6max-br7-punish-posters-and-blind-limpers-002` · beginner · preflop · limped · any · consensus 0.50 · sources: br79 · **draft**

**Claim.** A player who posts a blind out of position to play immediately, or who open-limps into your blind, has announced weakness. Raise them with almost any two cards when you have position, and raise about 4x with nearly your whole range when they limp your blind. Expect a fold preflop or on the flop a large share of the time.

**Why.** Posting in and open-limping are both plays that losing players make and winning players do not, so the raise is targeted at exactly the opponents who fold too much to aggression and play badly when they continue. With position you also get to see them act first on every street. The hand you hold is nearly irrelevant: the profit comes from the initiative and from how often they give up, so do not wait for a real hand to apply pressure.

**Common mistake.** Checking your option or folding playable hands against a limper in your blind, letting the weakest players at the table see cheap flops.

**Numbers.** raise ~4x with nearly the whole range when someone limps into your blind

**Hooks.** _He posted in. That is your cue to raise any two._ · _A limp into your blind is an invitation. Accept it._ · _The weakest preflop play in poker, and how to punish it._

Review: [ ]

### Micro regs rarely 3-bet, so steal wide from the cutoff and button; back off when one does
`c-cash-6max-br7-regs-are-tame-steal-wide-but-respect-the-3bettor-010` · beginner · preflop · btn · consensus 0.50 · sources: br79 · **draft**

**Claim.** Most regulars at NL10 are tame: they 3-bet far below 8% and seldom play back. Against tight blinds open very wide from the cutoff and especially the button, including any two suited cards. When you spot one of the rare players with real 3-bet numbers on your left, drop the marginal steals like jack-eight offsuit against them.

**Why.** Stealing profits from blinds that fold, and the typical micro regular folds the blinds far more often than theory would allow. Super-tight players, at 8% VPIP for example, fold so much that nearly any two cards show a profit from the button. The exception is the uncommon competent regular with 20/18-type stats and a healthy 3-bet percentage: against them a marginal steal faces a 3-bet often enough that the hand becomes a fold. Adjust by seat, not by a fixed range.

**Common mistake.** Opening a tight textbook button range against blinds that fold everything, or stubbornly opening jack-eight into the one player who 3-bets properly.

**Numbers.** few micro regs 3-bet as much as ~8% · lay off marginal steals vs a 21/18 player with an ~8% 3-bet on your left · an 8% VPIP player at 6-max should be stolen from with almost any two

**Hooks.** _Your button range is too tight for NL10._ · _Any two suited from the button? Against these blinds, yes._ · _One player type that should shrink your steal range._

Review: [ ]

### Set-mine only against a raiser with at least half a stack, unless a weak player is also in
`c-cash-6max-br7-set-mine-needs-half-a-stack-006` · beginner · preflop · srp · any · consensus 0.50 · sources: br79 · **needs-review** · review note: _Duplicate of br5-set-mine-needs-stack-depth-008 with a different threshold; merge or drop._

**Claim.** Before calling a raise with a small pair, check the raiser's stack. You generally want the raiser to hold at least half a buy-in; below that the payoff when you hit is too small. A weak player already in the pot can rescue a borderline spot because they supply the implied odds instead.

**Why.** A set wins big only when there is money left to win. Against a 40bb stack you flop a set rarely and collect a modest pot when you do, which does not cover all the times you miss and fold. Adding a second, loose opponent changes the math because their calling range will pay you even when the original raiser does not. Make the stack check part of the routine on every small-pair call.

**Common mistake.** Calling a half-stack's raise with pocket twos out of habit, then winning a tiny pot when the set finally comes.

**Numbers.** set-mine when the raiser has at least half a stack

**Hooks.** _Half a stack. That is the minimum to set-mine._ · _Small pair, short raiser: the fold most players never make._ · _One stack check that fixes a common small-pair leak._

Review: [ ]

### Call small pairs against early-position opens and 3-bet them against button opens
`c-cash-6max-br7-set-mine-vs-early-opens-3bet-small-pairs-vs-late-005` · beginner · preflop · srp · any · consensus 0.50 · sources: br79 · **draft**

**Claim.** With a small pocket pair facing a raise, let the raiser's position decide. Against an under-the-gun open, just call and set-mine: their range is tight and strong, so your implied odds when you hit are excellent. Against a button open, lean towards 3-betting: a late-position range is far wider, so you are often ahead and they will rarely pay off a set.

**Why.** Implied odds depend on the raiser holding a hand strong enough to pay you three streets when you flop a set. Early-position ranges are full of big pairs and big aces, which is exactly what you want to run into. A button range can be twice as wide or more, so it misses most flops and folds to your flop bet, which kills the set-mining plan but makes a 3-bet profitable. Always note where the raise came from before deciding how to play a pair.

**Common mistake.** Playing fives the same way against every open, 3-betting a tight early-position raiser or flatting a wide button and getting no action when the set arrives.

**Numbers.** a button range can be about twice as wide as an under-the-gun range · the coach opens up to four times more hands in late position than from UTG

**Hooks.** _Pocket fives: call or 3-bet? Look at where the raise came from._ · _Set-mining only pays against one kind of raiser._ · _The question to ask before every small-pair decision._

Review: [ ]

### Open tight from early position, and loosen only when a weak player sits in the blinds
`c-cash-6max-br7-tight-early-unless-a-fish-is-in-the-blinds-013` · beginner · preflop · utg · consensus 0.50 · sources: br79 · **draft**

**Claim.** Hands like six-seven suited or ten-three suited are folds from under the gun in a normal 6-max game. They become opens when a loose passive player is in the blinds and likely to call, because the hand is now a vehicle for playing a pot against them in position. Playing fewer tables also justifies a few more opens, since you can give each spot more attention.

**Why.** Early-position opens face the most players behind, so the base range must be tight. The value of a speculative hand comes almost entirely from who calls it; against regulars who 3-bet or fold, ten-three suited has nothing going for it, but against a weak player who will call and pay off two pair, the same hand is a profitable open. Fewer tables means more focus and more ability to extract from those spots, which shifts the marginal hands from fold to raise.

**Common mistake.** Opening speculative hands from under the gun regardless of who is in the blinds, or folding them when the loosest player at the table is about to call.

**Hooks.** _Six-seven suited under the gun: fold, unless this one thing is true._ · _Your opening range should change with who is in the blinds._ · _The fish in the big blind just made your junk hand playable._

Review: [ ]

### When players limp into your blinds, raise about half your hands; they fold early
`c-cash-6max-br8-raise-half-your-range-vs-blind-limpers-002` · beginner · preflop · limped · blinds · consensus 0.50 · sources: br79 · **draft**

**Claim.** Against one or two open-limpers when you are in the blinds, raise roughly 50% of your hands. Limpers at micro stakes fold to the raise or give up on the flop a large share of the time. Even so, keep a bit of a standard: hands like king-eight are a check out of position, while the same hand is an isolation raise in position.

**Why.** Open-limping is a passive, weak play, and the players who do it rarely defend properly against a raise. That makes the raise profitable with a wide range even though you are out of position, because so many pots end before the turn. The limit is the hands that make only weak pairs and have no suit or connection; out of position those turn into guessing games on later streets. Raise a lot, but not everything.

**Common mistake.** Completing or checking behind limpers with every playable hand, letting the most passive players at the table see flops at a discount.

**Numbers.** raise ~50% of hands against limpers when in the blinds

**Hooks.** _Two limpers, you are in the big blind. Raise half your hands._ · _Limpers fold more than you think. Make them pay to find out._ · _King-eight: raise in position, check from the blinds._

Review: [ ]

### Get queens in preflop against a near-maniac, especially right after you 3-bet them
`c-cash-6max-br8-stack-off-queens-vs-near-maniac-with-history-013` · beginner · preflop · 4bet-pot · any · consensus 0.50 · sources: br79 · **draft**

**Claim.** Against a player with stats close to 47/37 who 4-bets you, shove queens. Their range is wide and aggressive, and if you 3-bet them an orbit or two earlier they are even more likely to be playing back light. Do not let a full-ring habit of slowing down with queens cost you a stack against this player type.

**Why.** Queens are a borderline hand against a tight 4-bettor, but the decision is entirely opponent-dependent. A loose-aggressive player 4-bets with far more than aces and kings, and recent history makes them more stubborn still. Against that range queens are a big favourite and the third-best starting hand, so the stack-off is clear. If they happen to have one of the two hands that beat you, that is variance, not a mistake.

**Common mistake.** Flat-calling or folding queens to a 4-bet from a 47/37 because "queens are tricky", applying a full-ring rule to a maniac.

**Numbers.** vs a ~47/37 player, queens are a trivial preflop stack-off

**Hooks.** _Queens versus a 4-bet: the answer depends on one HUD number._ · _You 3-bet him last orbit. Now he 4-bets. Shove queens._ · _Stop treating queens like a trap hand against maniacs._

Review: [ ]

### A beginner at 6-max should aim near 21/18 with a 4-5% 3-bet, tighter than the coach
`c-cash-6max-br8-target-stats-for-beginners-at-6max-014` · beginner · preflop · any · consensus 0.50 · sources: br79 · **needs-review** · review note: _Coach commenting on own on-camera stats; context-bound._

**Claim.** Stats like 28/23 with an 8% 3-bet come from an experienced player on only four tables who can spot extra spots. A beginner or novice should play tighter, around 21/18, with a 3-bet around 4-5%, and loosen up only as marginal spots become comfortable. Playing fewer tables justifies a few more hands because you can give each decision more attention.

**Why.** Loose stats are only profitable when every extra hand is played well postflop, and that takes experience. A tighter range keeps a newer player out of the marginal situations where most money is lost, while still capturing the core edge of isolating weak players and value betting. The number of tables matters because attention is the resource that converts a marginal hand into a profitable one; on many tables the same hand is a leak.

**Common mistake.** Copying a coach's loose session stats hand for hand while playing eight tables and without the postflop experience to back it up.

**Numbers.** beginner target ~21/18 at 6-max · 3-bet around 4-5% rather than ~8% · coach's 28/23 with ~8% 3-bet came from four tables and video play

**Hooks.** _The stats a beginner should actually aim for at 6-max._ · _28/23 works for the coach. It will not work for you yet._ · _Fewer tables, more hands: the trade-off explained._

Review: [ ]


## cbet-strategy  (30)

### Versus a station, c-bet with hands that can improve and give up with the rest
`c-cash-6max-br2-cbet-hands-that-can-improve-007` · beginner · flop · srp · ip · consensus 0.50 · sources: br79 · **draft**

**Claim.** Against a player who calls almost every flop bet, do not c-bet simply because you raised. Bet when your hand has ways to improve, such as overcards or a draw, and check back hands like a small pocket pair on a high board that are drawing nearly dead if called.

**Why.** A c-bet against a non-folder rarely wins the pot outright, so its value has to come from what happens when called. A hand with six or more outs can turn into the best hand and collect more bets from a player who does not fold. A hand with two outs just puts money in behind and then has to fold to any aggression. Checking those hands keeps the pot small and sometimes wins at showdown unimproved, which is a better result than a wasted bet.

**Common mistake.** Firing a c-bet with pocket fives on a K-J-8 board against a station and then folding the turn.

**Hooks.** _Which hands should you c-bet into a station? Only these._ · _Pocket fives on a king-high flop. Check, do not bet._ · _A c-bet that cannot improve is a donation at micro stakes._

Review: [ ]

### With just two overcards on a middling, coordinated flop, do not c-bet
`c-cash-6max-br3-skip-cbet-two-overs-wet-013` · beginner · flop · srp · any · consensus 0.50 · sources: br79 · **draft**

**Claim.** When you hold a hand like A-Q on a flop such as 9-8-6 with draws everywhere, give up without putting a chip in. The opponent connects with too many hands and you have only two overcards with no backup.

**Why.** Boards full of middle cards hit the calling ranges of micro players hard: pairs, straight draws, two pairs and combination draws are all common. Your two overcards have about six outs and little fold equity, since this type of opponent calls with any piece. A c-bet here builds a pot you are usually losing and sets up awkward turn decisions. Skipping the bet entirely keeps the loss to the preflop raise.

**Common mistake.** C-betting every flop as the preflop raiser and then facing a raise on a board you can never continue on.

**Hooks.** _Ace-queen on nine-eight-six. Do not bet a penny._ · _The flop every c-bet rule forgets about._ · _Two overcards, wet board, no bet. Here is why._

Review: [ ]

### C-bet the large majority of flops heads-up in position; micro players give up easily
`c-cash-6max-br5-cbet-most-flops-ip-heads-up-009` · beginner · flop · srp · ip · consensus 0.50 · sources: br79 · **draft**

**Claim.** Heads-up and in position after raising preflop, continuation bet most flops no matter what you hold, around 80% or more, with a stab of roughly 60% pot. When a player checks to you, bet. The strength of your own hand matters much less than the fact that the population plays very straightforwardly and folds too much.

**Why.** Players at these stakes mostly continue only when they connect, and they rarely float or check-raise light. That means a single bet wins the pot often enough that hand strength becomes almost secondary when you are in position against one opponent. The betting lead you bought preflop is only worth something if you use it. Reserve the checks for the small set of flops where you have no equity and expect few folds (see the card on middling two-tone boards), and against players who have shown they never fold.

**Common mistake.** Only c-betting when you hit, which lets straightforward opponents play perfectly against you and wastes the initiative you paid for preflop.

**Numbers.** c-bet roughly 80%+ heads-up in position · standard stab ~60% pot

**Schools disagree.** Solver-based c-bet frequencies vary heavily by texture and are often well below 80%; the coach argues the micro population over-folds enough to justify a near-always c-bet in position.

**Hooks.** _Checked to you in position? Bet. Here is the number._ · _Your hand barely matters on this flop._ · _Most NL5 players c-bet far too little heads-up._

Review: [ ]

### C-bet about 80% of flops, 90% when checked to in position; skip middling two-tone boards
`c-cash-6max-br7-cbet-frequency-and-the-flops-to-skip-004` · beginner · flop · srp · any · consensus 0.50 · sources: br79 · **draft**

**Claim.** As the preflop raiser, continuation bet roughly 80% of flops overall, closer to 90% when you are in position and the opponent checks. The flops to skip are the coordinated middling boards, something like six-seven-eight or seven-eight-nine with two of a suit, when you hold nothing: you have no equity and expect few folds. Two broadways plus a low card, or a dry board, is a good flop to stab.

**Why.** Most micro-stakes opponents fold to a single bet unless they connect, which makes a high c-bet frequency correct. But middling connected two-tone boards hit a calling range hard: they contain pairs, straight draws and flush draws for the caller and nothing for an overcard-heavy raising range. Betting there with no outs just loses a bet. High-card boards do the opposite; they favour the raiser and miss the caller, so a stab there wins often even without a hand.

**Common mistake.** C-betting every flop on autopilot, including the eight-seven-six two-tone board where the caller continues most of the time and you have no way to improve.

**Numbers.** c-bet ~80% of flops overall · ~90% when in position and checked to · skip flops like 6-7-8 or 7-8-9 with two of a suit when you hold no equity

**Schools disagree.** Solver output c-bets far less than 80% on many textures; the coach's frequency relies on a micro population that folds too much to one bet.

**Hooks.** _We c-bet 80% of flops. These are the 20% we skip._ · _The one flop type where a c-bet is just burning money._ · _Two broadways and a brick: always stab._

Review: [ ]

### The flops you skip c-betting should mostly be the ones where you are out of position
`c-cash-6max-br8-cbet-less-often-out-of-position-016` · beginner · flop · srp · oop · consensus 0.50 · sources: br79 · **draft**

**Claim.** Against a player who rarely folds, a middling flop with a gutshot is a check out of position, but the same flop is a c-bet in position. Most of the time you decline to c-bet, it should be because you are out of position; in position, keep betting at a very high frequency.

**Why.** Out of position a c-bet that gets called leaves you first to act on the turn with no information and no free card, so a bluff on a bad texture compounds across streets. In position the same bet is cheaper: if called, you can check the turn, see a free river, or decide with their action in front of you. Position changes the cost of being wrong, so it should change how often you fire on marginal flops.

**Common mistake.** Using the same c-bet frequency in and out of position, which means bluffing too much from the blinds and too little from the button.

**Hooks.** _Same flop, same hand. Bet in position, check out of position._ · _Where you sit should change how often you c-bet._ · _Most of your flop checks belong out of position._

Review: [ ]

### With a massive flop range advantage, bet your air now instead of hoping he bets
`c-cash-6max-cc03-flop-range-bet-dont-trap-019` · intermediate · flop · 3bet-pot · oop · consensus 0.50 · sources: cc · **draft**

**Claim.** On flops that overwhelmingly favour you, such as a paired king-high board as the 3-bettor from the blinds against the button, bluff immediately with your whole range. Checking to trap fails because the player with the weak range almost always checks back, and delaying lets him realise equity you could have denied.

**Why.** You hold all the kings and the big pairs; he mostly missed. If you check, a competent opponent, and even a weak one who senses the board is bad for him, will rarely bet into you, so the check-raise you were planning never happens. Meanwhile his jack-ten gets a free card and will not fold once a jack arrives. In one solver example the button folded about 53% to a third-pot bet, roughly double the 25% that pot odds alone would suggest, because he understands how badly his range is doing. Checking here is only a small error since you can bluff later, but it is still an error, and the betting should be done by the player with the strong range.

**Common mistake.** Checking a dry king-high paired flop in a 3-bet pot to "induce", then watching the opponent check back and catch up.

**Numbers.** example: button folds ~53% to a 33% pot c-bet on K-K-x vs the blinds' 3-bet range (neutral baseline 25%) · checking instead loses ~1% of the pot in equilibrium

**Hooks.** _Trapping on K-K-5 only traps yourself._ · _He folds 53% to a third pot. Bet everything._ · _When your range is the bear, you throw the first swipe._

Review: [ ]

### Ask how much the big blind has caught up, not whether they are ahead
`c-cash-6max-cc06-equalization-sets-cbet-frequency-021` · intermediate · flop · srp · btn · consensus 0.50 · sources: cc · **draft**

**Claim.** The big blind almost never has a range advantage against the button, so the useful question is how much its range has equalized on this flop. The more it has caught up, the lower your c-bet frequency should be, even if you still hold a nut advantage.

**Why.** The button's range is dense with two high cards - ace-jack, king-ten and the like. On a low connected flop those hands drop sharply in equity while the big blind's small suited connectors and one-gappers turn into pairs, two pairs and draws. The button may still sit at 50% range equity and still own the overpair region, but the frequency edge is gone. That produces the conventional pattern of betting rarely but big. On a high dry board the equalization is minimal and the button bets very often. Frame every flop as "how far has the defender closed the gap" and your c-bet frequency will follow.

**Common mistake.** C-betting the button at the same high frequency on every flop because the button "always has range advantage".

**Numbers.** Example: BTN vs BB on a low connected board, button ~50% range equity, keeps overpair nut edge - low frequency, big size

**Hooks.** _The big blind is never ahead. That's the wrong question._ · _How much did they catch up? That sets your c-bet rate._ · _Why you c-bet less on low connected flops_

Review: [ ]

### On low paired boards the raiser can range-bet large, not small
`c-cash-6max-cc06-range-bet-big-on-low-paired-boards-018` · advanced · flop · srp · ip · consensus 0.50 · sources: cc · **draft**

**Claim.** On a board like jack-deuce-deuce, an early-position raiser against the big blind holds both a huge range advantage and a huge nut advantage, so betting the entire range for around 75% pot is the theory-preferred strategy. A small range bet is acceptable but gives up a little EV.

**Why.** Nobody has many deuces, so the real nut region is still overpairs, which sit above 90% equity against a range full of missed hands. The big blind cannot catch up at the top because the paired card is one they rarely hold. That is the profile for big sizing. Contrast a jack-ten-ten board, where the big blind holds a ten far too often - trips are now easy for them, your overpairs are negated, and a small size is mandatory. The difference is not "paired board" versus "unpaired", it is whether the paired rank is one the defender actually has. Most players assume range bets are always small, and the coach estimates that most regulars would size small here, which makes the big bet unfamiliar to face as well as theoretically better.

**Common mistake.** Equating "range bet" with "small bet" and never considering a large size when betting everything.

**Numbers.** Range-bet ~75% pot on low paired, hard-to-hit boards where overpairs keep ~90% equity · Coach's estimate: 70-80% of regs would bet small on such a board

**Hooks.** _Yes, you can range-bet 75% pot. Here's where._ · _Range bet does not mean small bet._ · _J22 and JTT look similar. The sizing is opposite._

Review: [ ]

### Range advantage raises c-bet frequency because every reason to bet gets better
`c-cash-6max-cc06-why-range-advantage-means-more-cbets-013` · intermediate · flop · srp · any · consensus 0.50 · sources: cc · **draft**

**Claim.** With a large range advantage on the flop, bet a much larger share of your range - sometimes all of it. The reason is mechanical, not mystical - a weak opposing range has to fold more, which improves value bets, bluffs and equity denial at the same time.

**Why.** A range is just a collection of hands, so anything that is good for the range is good for many of the hands in it. When the opponent's range is weak, they fold more often than a break-even defender would, so bluffs win more. Fewer of their hands beat a given holding, so thinner hands become value bets. And because their weak hands still have live outs, denying those outs with a bet is safer - you rarely run into the hand that punishes you. All three motives improve together, which is why solvers range-bet flops where one side is far ahead. This is a flop phenomenon. On the turn and river you are close to showdown, denial matters less and betting polarizes again.

**Common mistake.** Treating "bet your range when ahead" as a memorized rule while still applying it to turns and rivers where the same logic no longer holds.

**Hooks.** _Why range advantage means bet more - the real mechanism_ · _Three reasons to bet, and all three improve at once_ · _Range-bet the flop. Never range-bet the river._

Review: [ ]

### On terrible flops in position, range check rather than c-betting 20% of the time
`c-cash-6max-cc07-range-check-horrible-flops-ip-020` · intermediate · flop · srp · ip · consensus 0.50 · sources: cc · **draft**

**Claim.** When a flop is so bad for the preflop raiser that the equilibrium c-bet frequency drops to about 20% at a small size, simplify to checking your entire range in position. The caller will lead the turn often, so your strong hands still get paid.

**Why.** A 20% c-bet strategy is nearly impossible to execute: you would need a randomizer for every hand class and gain almost nothing for the effort. On flops like low connected monotone boards, even your overpairs hold only around 62-65% equity against the caller's range, behind more often and less far ahead when in front, so they do not want to build a big pot yet. If the flop is that bad for you it is correspondingly good for the caller, who in theory wants to lead the turn at a high frequency, so your sets and straights make money by letting them bet. Remember that initiative is not a reason to bet: betting with a range disadvantage is the same whether you raised preflop or not. What matters is which ranges arrived at the flop.

**Common mistake.** Feeling obliged to c-bet "something" because you were the raiser, and firing a tiny fraction of the time with a strategy you cannot actually apply.

**Numbers.** Overpair on a very bad flop texture: ~62-65% equity vs the caller's range · If the equilibrium c-bet frequency is ~20%, simplify to a range check in position

**Hooks.** _Some flops you should never c-bet, even in position._ · _'I raised, so I bet' is a myth._ · _Why checking your whole range here makes more money._

Review: [ ]

### Straight-heavy middling flops and monotone boards are where the raiser checks most
`c-cash-6max-gp23-high-check-textures-003` · intermediate · flop · srp · ip · consensus 0.50 · sources: rio · **draft**

**Claim.** In position after a check, the flops with the highest check-back frequency are middling connected boards with several possible straights and monotone boards. When you do bet on the connected middling boards, the typical size is around 75% pot rather than a small bet.

**Why.** The caller defends preflop with suited and connected medium cards, so textures like T98 or 875 hit their range harder than yours and your high-card overpairs are vulnerable. Checking more protects your medium-strength hands and avoids bloating pots where you are often behind. When you do bet, a medium size with a tighter, more polarized range makes sense because the caller has many strong hands and draws that will not fold to a quarter pot anyway. Note that a high check frequency can mean two different things: little money going in because the caller is favored, or a polarized big-bet strategy. Look at the bet size column before concluding which.

**Common mistake.** Auto c-betting small on 987 two-tone because "I am the raiser", then facing raises and turn barrels with a range that cannot stand them.

**Numbers.** when betting middling connected flops IP, ~75% pot is the typical size

**Hooks.** _Checking this flop makes you more money than betting._ · _The one flop type where the raiser is the underdog._ · _Raiser checks here 60%+ of the time. Do you?_

Review: [ ]

### Paired and ace-high flops are the home of the quarter-pot c-bet in position
`c-cash-6max-gp23-small-bet-paired-ace-high-002` · intermediate · flop · srp · ip · consensus 0.50 · sources: rio · **draft**

**Claim.** As the in-position raiser in a single raised pot, paired boards and most ace-high boards call for a small c-bet (around 25% pot) at a very high frequency. Whether the board is rainbow or two-tone barely changes this choice.

**Why.** On these textures the preflop raiser holds the clear range advantage and the caller has few hands that can comfortably raise. A small bet taxes the caller's many weak holdings, keeps your own weak hands in the pot cheaply, and makes future streets simpler. Solver reports show the boards with the highest small-bet frequency are dominated by paired flops, and once those are removed the remainder is mostly ace-high. Monotone and heavily connected boards are notably absent from this group, while suit distribution between rainbow and two-tone shows up on both sides, which tells you flush-draw count is not the driver of size here.

**Common mistake.** Sizing up to 2/3 pot with strong hands on A72 or 884 rainbow and checking the rest, which splits the range and makes both parts easier to play against.

**Numbers.** c-bet ~25% pot on paired and ace-high flops IP in SRP

**Example.** positions: CO vs BB | hero: KdQs | board: As7h2c | action: CO opens, BB calls. BB checks. | decision: Check, bet 25% or bet 66%? | answer: Bet 25%. This texture is a small-bet board for the whole range, including king-high air.

**Hooks.** _Most NL10 players size this flop wrong._ · _Paired board? Bet a quarter pot. Every time._ · _'Two-tone means bet bigger' is costing you money._

Review: [ ]

### Limit every flop category to two options: check plus one size, or two sizes with no check
`c-cash-6max-gp23-two-options-rule-006` · advanced · flop · srp · ip · consensus 0.50 · sources: rio · **draft**

**Claim.** When simplifying a flop c-bet strategy, cap each texture at two actions. Usually that is check or one size. On some textures, such as two-Broadway boards, the better pair is a quarter-pot bet and an overbet with checking removed entirely.

**Why.** A solver's three-or-four-way mix on a flop is not something a human can reproduce accurately, and errors in frequency cost more than the simplification does. The trick is to drop the option that is closest in value to another one. Where a paired or ace-high board shows a low but nonzero check frequency, folding the checks into the small bet is almost free. Where the small bet and the overbet both do real work and the checks are the weak option, remove the checks instead. The decision is about which two options carry the EV, not about always keeping a check.

**Common mistake.** Assuming simplification always means "check or bet one size", and never considering that the check itself may be the option worth cutting.

**Numbers.** two-Broadway flops: 25% pot and 150% pot, no checks

**Hooks.** _Two options per flop. Never three._ · _Sometimes the move to cut from your strategy is the check._ · _Counterintuitive: never checking this flop is the simple play._

Review: [ ]

### Range-bet high paired flops; keep the solver's checks on low paired flops
`c-cash-6max-gp30-paired-high-vs-low-002` · advanced · flop · srp · ip · consensus 0.50 · sources: rio · **draft**

**Claim.** In position in a single raised pot, high paired boards such as QQx or KKx can be simplified to a quarter-pot range bet. On lower paired boards (around TTx and below) the c-bet frequency drops, the caller check-raises more, and the correct defense is easy to see, so keep the mixed strategy with checks.

**Why.** The higher the pair, the more of the caller's range is pure air with little to raise with, and the hands that should continue or raise are awkward ones many players miss. Dropping the pair rank even two notches noticeably increases the solver's checking and the caller's raise frequency. On a low paired board the caller's defending hands are intuitive: pairs, straight draws, overcards with a flush-suit card. Opponents will find those, so betting your whole range into them is less attractive. One side note: the caller's preferred raise size also shifts with pair rank, small on high paired boards and large on lower ones.

**Common mistake.** Treating all paired boards as identical range-bet spots and getting check-raised off equity on 776 and 554 textures.

**Numbers.** vs 25% c-bet on high paired flops the caller raises ~20% and folds little

**Example.** positions: BTN vs BB | hero: 9c8c | board: KhKd4s | action: BTN opens, BB calls. BB checks. | decision: Bet or check with a weak unpaired hand? | answer: Bet 25%. On a high paired board the simplified plan is to bet the entire range at a small size.

**Hooks.** _KK4 and 664 are not the same flop._ · _Range bet the high pair, respect the low pair._ · _Two ranks lower and the whole plan changes._

Review: [ ]

### Decide whether to range-bet a flop by checking how hard the correct defense is to find
`c-cash-6max-gp30-range-bet-test-001` · advanced · flop · srp · ip · consensus 0.50 · sources: rio · **draft**

**Claim.** When a solver c-bets a texture almost always but not quite, look at the caller's response to the small bet before simplifying to a 100% range bet. If the correct defense relies on hands most opponents will not find, such as weak queen-high or jack-high with only a backdoor straight draw, the range bet is safe. If the defending hands are obvious, follow the solver's checking frequency.

**Why.** A range bet gives up a little EV versus a perfect opponent but gains a lot in simplicity, and it gains even more against opponents who under-defend. The way to measure that is to study the counter-strategy: how often the caller is supposed to raise, how little they are supposed to fold, and what the marginal continuing hands look like. When those hands are strange and the raise frequency is high, real players will fold too much and raise too little, so betting everything prints. When the defense is intuitive, your air gets punished and the solver's checks are worth keeping.

**Common mistake.** Range-betting every "dry" flop by reflex, without checking whether the caller's correct response is easy or hard for real players to execute.

**Hooks.** _Range bet only when the defense is hard to find._ · _The one check that tells you to bet 100%._ · _Your range bet works because opponents miss these hands._

Review: [ ]

### Range-betting a texture deletes the whole facing-a-float branch for you
`c-cash-6max-gp34-range-bet-removes-float-branch-002` · intermediate · flop · 3bet-pot · oop · consensus 0.50 · sources: rio · **draft**

**Claim.** As the out-of-position 3-bettor, every flop texture you decide to range-bet is a texture where you will never face an in-position stab after checking. Only study the check-then-face-a-bet node on textures where your plan actually includes checks.

**Why.** A simplified flop plan sorts boards into range-bet, range-check and a few mixed textures. If you never check a board class, the in-position player never gets to bet into your check there, so planning your response on that class is wasted effort. The reverse is also true. Range-check textures (high-low-low and monotone) and the mixed middle textures are exactly where you will face the most bets after checking, so those are the high-priority spots for building a check-call and check-raise plan. Simplifying the first decision point is what makes the later streets manageable.

**Common mistake.** Spending study time on how to defend a check on boards where your own game plan says you always bet.

**Hooks.** _Half the flop spots you study will never happen to you._ · _Range-bet here and one awkward spot disappears forever._ · _Where does checking as the 3-bettor actually get tested?_

Review: [ ]

### On a high-frequency betting board, a hand that looks like a check still bets often
`c-cash-6max-gp35-check-looking-hand-still-bets-010` · intermediate · flop · 3bet-pot · ip · consensus 0.50 · sources: rio · **draft**

**Claim.** When the baseline betting frequency on a texture is high, a hand that seems weaker than average does not become a pure check. It becomes a lower-frequency bet, for example 40% instead of 60%.

**Why.** Your betting frequency on a board is a property of the whole range, not of each hand. If the range bets most of the time, then even the below-average hands need to bet some of the time or the frequency collapses and your checks become too weak. Players who judge hand by hand tend to bet only the obvious candidates and end up far below the frequency the board calls for. Anchor on the baseline first, then move individual hands up or down from there.

**Common mistake.** Checking every hand that is not an obvious bet, which drops a 60% board to a 30% board without noticing.

**Hooks.** _'This hand is a check' is usually wrong. It's a 40% bet._ · _You bet hands. Solvers bet ranges._ · _Why your c-bet frequency is quietly too low._

Review: [ ]

### A low betting frequency is not just missing bluffs; all hand classes bet small
`c-cash-6max-gp35-many-hand-classes-bet-small-011` · intermediate · flop · 3bet-pot · ip · consensus 0.50 · sources: rio · **draft**

**Claim.** If your in-position betting frequency after a check is too low, do not assume you only lack bluffs. Solvers mix small bets into middle pairs, strong hands and various draws at frequencies most players never use. The gap is spread across all hand classes.

**Why.** It is tempting to diagnose a frequency leak as "I need more bluffs", because bluffs feel like the hands you are afraid to bet. But a small bet works for a medium pair that denies equity, for a strong hand that builds the pot, and for a draw that wants a free card less than it wants fold equity. When all of these bet some of the time, the total frequency rises without any single class betting always. Fixing the leak means loosening across the board, not adding one bluff type.

**Common mistake.** Adding a few extra bluffs and declaring the frequency fixed while middle pairs still check 100%.

**Hooks.** _Your frequency problem isn't bluffs. It's everything._ · _Middle pair bets small here. Yes, really._ · _The hands you never bet that solvers bet all the time._

Review: [ ]

### Range-check jack-to-king-high dry flops as the 3-bettor in wide-range pots
`c-cash-6max-gp36-high-low-low-range-check-010` · advanced · flop · 3bet-pot · oop · consensus 0.50 · sources: rio · **needs-review** · review note: _Source framed for heads-up 100-120bb; say so in why or re-tag format._

**Claim.** On flops headed by a jack, queen or king with two low disconnected cards (not ace high), the out-of-position 3-bettor can check the entire range. Removing checks is the most expensive mistake on these boards and a small range bet gets almost no folds.

**Why.** The 3-bettor's range is full of broadway cards that miss a board like Q-7-3 or J-6-2, while the caller's suited connectors, small pairs and low suited hands connect or hold backdoors. A quarter-pot stab makes the caller fold only around 13%, so it buys nothing. Checking the whole range costs almost no EV against a correct opponent, whose checking frequency rises only about 3% in response, and it funnels the pot into check-raise and delayed lines where the 3-bettor's value hands do better. This texture category excludes ace-high boards and boards where the middle card makes high-end straight draws.

**Common mistake.** Auto c-betting Q-7-3 as the 3-bettor because "I have the range advantage", then facing a raise or a call with no plan.

**Numbers.** Caller folds ~13% to a 25% pot c-bet on high-low-low flops · In-position checking frequency rises only ~3% when the 3-bettor range-checks

**Hooks.** _3-bet, flop Q-7-3, and the right play is check. Always._ · _A c-bet that gets 13% folds is not a c-bet._ · _The dry flop where the 3-bettor should stop betting._

Review: [ ]

### Wide 3-bet ranges mean the 3-bettor checks far more often out of position
`c-cash-6max-gp36-wide-3bet-ranges-check-more-001` · advanced · flop · 3bet-pot · oop · consensus 0.50 · sources: rio · **needs-review** · review note: _Source framed for heads-up 100-120bb; say so in why or re-tag format._

**Claim.** In 3-bet pots where both ranges are wide, the out-of-position 3-bettor should check the flop much more than in tighter-range formats, and when betting, lean toward polarized large bets rather than frequent small ones.

**Why.** The small range bet works when the aggressor's range is clearly stronger on most flops. A wide 3-bet range against a wide calling range loses that edge, and many textures quietly favour the in-position caller. With less range advantage, betting the whole range small bleeds value, so the solution is to check often and bet big with a polarized range on the textures where betting is still good. A player can still build a profitable plan with more c-betting than theory, but they should know they are paying for it in EV.

**Common mistake.** Carrying the six-handed habit of range-betting small as the 3-bettor into wide-range blind-vs-blind or button-vs-blind 3-bet pots.

**Hooks.** _The 3-bettor checks here. Most players can't believe it._ · _Range betting small in 3-bet pots has a hidden cost._ · _Checking makes you more money in these 3-bet pots._

Review: [ ]

### C-bet most often on rainbow, paired and high-card flops as the button
`c-cash-6max-tc14-high-frequency-flop-types-001` · intermediate · flop · srp · btn · consensus 0.50 · sources: 2cc · **draft**

**Claim.** Button against big blind in a single-raised pot, the flops with the highest c-bet frequency share three features - they are rainbow, they are paired, or they are headed by a high card (ten or above). The more of these a flop has, the closer you get to betting your whole range.

**Why.** When you sort every flop by how often the solver checks, the near-range-bet flops are dominated by boards like AAx, KKx, QQx rainbow, and unpaired king- and queen-high rainbow boards. Rainbow textures mean fewer flush draws for the caller to continue with, pairing removes most of the two-pair and set combos from the big blind's range, and high cards hit the button's range far harder than the big blind's. Almost no eight-high or lower flop appears in the high-frequency group unless it has trips on board.

**Common mistake.** C-betting a fixed percentage on every flop, so you under-bet the boards where the whole range profits and over-bet the ones where it does not.

**Numbers.** Highest c-bet frequency flops: AAx, KKx, QQx paired boards and rainbow high-card boards · Trips boards like 333, 332, 334 are the only low flops in the high-frequency group · Almost no 8-high or lower unpaired flop reaches the high-frequency group

**Hooks.** _Three flop features tell you to bet your whole range._ · _Most NL25 players check too much on KK6 rainbow._ · _Paired, rainbow, high. Bet it all._

Review: [ ]

### C-bet least on monotone and ace-high two-tone flops as the button
`c-cash-6max-tc14-low-frequency-flop-types-002` · intermediate · flop · srp · btn · consensus 0.50 · sources: 2cc · **draft**

**Claim.** The flops where the button checks most are monotone boards, especially ace-high monotone ones, followed by ace-high two-tone flops such as AQ2, A32 or AQ5. Rainbow flops almost never appear among the low-frequency boards.

**Why.** Monotone and two-tone textures give the big blind many flush draws and made flushes to continue with, and an ace on top means the button's many top-pair hands do not need to bet for protection. Together those two features cut the incentive to bet dramatically. The first rainbow flop only shows up once c-bet frequency has climbed back to around a third, and even that one is ace-king high. Below that line almost everything is suited in some way.

**Common mistake.** Auto-c-betting ace-high flops because 'I have the ace in my range', even when the board is suited and the big blind can continue with lots of draws.

**Numbers.** Lowest c-bet frequency flops are all monotone, mostly ace-high · Ace-high two-tone flops like AQ2, A32, AQ5 sit around 33% c-bet frequency · First rainbow flop in the low-frequency region (AK2) appears at ~33% bet frequency

**Hooks.** _'Always c-bet ace-high flops' is costing you money._ · _Checking AQ2 two-tone makes you more money. Here's why._ · _The flops a solver barely ever c-bets._

Review: [ ]

### Check back more on ace-high flops because your pairs need little protection
`c-cash-6max-tc15-ace-high-flops-less-protection-007` · intermediate · flop · srp · btn · consensus 0.50 · sources: 2cc · **draft**

**Claim.** On ace-high flops like AQ2 the button's many top-pair and second-pair hands gain little from betting for protection, so the c-bet frequency should be lower than on a flop like J88 where the caller holds many overcards.

**Why.** Top pair with an ace cannot be out-pipped by a higher pair on the turn; the caller needs two pair or better to pass you, and those hands mostly were not folding anyway. Second pair like KQ on AQ2 is a similar story. A king turn gives you two pair, a jack turn gives folded Jx a lower pair than yours, so the folds you would get are from hands that rarely overtake you. Betting there mostly gets called by better and folds out worse that was not a threat. Contrast J88 with pocket fours, where the caller is full of Qx, Kx and Ax that beat you on many turns and would have folded - there, protection is a strong reason to bet.

**Common mistake.** Betting every ace-high flop with second pair 'for protection', then being unable to explain which hands with equity actually folded.

**Numbers.** Ace-high two-tone flops like AQ2 land near ~33% c-bet frequency in the report

**Hooks.** _Checking AQ2 with top pair makes you more money._ · _Why KQ on AQ2 should not bet._ · _'Protect your hand' is a myth on ace-high flops._

Review: [ ]

### High flops miss the big blind's range, so bets go through more often
`c-cash-6max-tc15-high-flops-miss-bb-range-004` · intermediate · flop · srp · btn · consensus 0.50 · sources: 2cc · **draft**

**Claim.** C-bet more on flops like K82, KK6 or QTT because the big blind's calling range is built from low and medium cards and folds a lot there. C-bet less on low connected flops like 65x where that same range hits pairs and draws.

**Why.** The big blind three-bets its best high-card hands preflop, so the range that reaches the flop by calling is weighted toward small cards and suited junk. The button's range is the opposite, dominated by broadways and big aces. On a high flop the caller has little to continue with and folds often, which rewards frequent betting. On a low connected flop the caller has every small pair, hands like 53s and 52s that the button never opens, and gutshots and open-enders around the board, and even offsuit connectors like 87o that the button folds preflop. Fold equity collapses, so the button checks more.

**Common mistake.** Firing on 654 or 763 'because I'm the raiser' when the big blind's range connects with the board better than yours does.

**Hooks.** _The big blind folds K82 and calls 653. Plan around it._ · _Most players c-bet 654 too often against the big blind._ · _Why 'I'm the raiser' is not a reason to bet._

Review: [ ]

### C-bet near your whole range on AAx and KKx flops as the button
`c-cash-6max-tc15-paired-high-boards-trips-advantage-002` · intermediate · flop · srp · btn · consensus 0.50 · sources: 2cc · **draft**

**Claim.** On paired ace-high and king-high flops the button should c-bet at a very high frequency, because the button holds far more trips than the big blind does.

**Why.** The big blind three-bets most of its strong Ax and Kx - AK, AQ, KQ, AA, KK - before the flop, so those hands leave the range the moment they just call. The button still opens all of them. On AAx or KKx that means the nut-like holdings are concentrated on the button's side and the big blind is left with weak Ax and Kx at best. When one player owns the trips and the other mostly has air and small pairs, betting almost everything is correct.

**Common mistake.** Slowing down on paired high boards because 'nobody has anything', and checking back a range that would print money betting.

**Numbers.** AAx and KKx paired flops sit in the highest c-bet frequency group of the report

**Hooks.** _KK6 rainbow. Bet every hand. Here's why._ · _The big blind can't have trips here. Make them pay._ · _Who has more kings on KK4? Not who you think._

Review: [ ]

### Suited flops give the caller more hands to continue with than rainbow flops
`c-cash-6max-tc15-suited-flops-more-continues-005` · beginner · flop · srp · btn · consensus 0.50 · sources: 2cc · **draft**

**Claim.** All else equal, c-bet less often on two-tone and monotone flops than on rainbow flops, because every flush draw the big blind holds becomes a continuing hand against your bet.

**Why.** The big blind's calling range contains a lot of suited hands, so whenever two or three cards of one suit appear, a big chunk of that range picks up a draw and will not fold to a c-bet. A rainbow flop removes this entirely - the caller continues only with pairs, straight draws and the occasional float. Fewer continues means more folds, and more folds means a higher betting frequency is justified. This is why rainbow boards dominate the high-frequency end of any flop report.

**Common mistake.** Ignoring suits when deciding whether to c-bet and betting K72 two-tone as often as K72 rainbow.

**Hooks.** _Same flop, two suits, different c-bet. Here's why._ · _Flush draws don't fold. Count them before you bet._ · _One glance at the suits changes your flop plan._

Review: [ ]

### Three factors decide how often to c-bet the flop in position
`c-cash-6max-tc15-three-factors-cbet-frequency-001` · intermediate · flop · srp · btn · consensus 0.50 · sources: 2cc · **draft**

**Claim.** Judge a flop by three questions - who has more nut hands, how many hands can the caller continue with, and how many of your hands benefit from protection. The more of these favour the button, the higher your c-bet frequency should be.

**Why.** Each factor is a separate reason to bet. A nut advantage lets you bet big and often without fear of the top of their range. A caller who misses the flop folds a lot, so bets win the pot outright. Protection matters when your medium hands are ahead but vulnerable to free cards. High-card, paired, rainbow flops tick all three boxes and get near range bets; low, connected, suited flops fail all three and get checked much more. Scoring a flop on these three gives you a usable c-bet frequency without a solver at the table.

**Common mistake.** Picking a c-bet frequency from one feature only, such as 'I have range advantage', and ignoring that the caller can continue widely or that your hands do not need protection.

**Hooks.** _Three questions replace your solver on the flop._ · _Most NL10 players c-bet on one reason. You need three._ · _How often should you c-bet? Ask this._

Review: [ ]

### C-bet only about 57% on 774 two-tone as the button
`c-cash-6max-tc17-cbet-57-on-774-001` · intermediate · flop · srp · btn · consensus 0.50 · sources: 2cc · **draft**

**Claim.** In a single-raised pot, button versus big blind, a 774 two-tone flop is not a range-bet board. Theory c-bets around 57%, checks a share of trips as a balance, mixes checks with overpairs, underpairs, second and third pairs, and checks many ace-high and king-high hands.

**Why.** The paired low board favours the caller more than it looks. The big blind holds more 7x, including offsuit combos you never open, plus 74s and 44 for full houses, so they have more trips and more boats than you. Quads via 77 are shared. With the nut region tilted toward the defender, you cannot bet everything without being check-raised off too much equity, so part of the range checks and some trips check to protect the checking range.

**Common mistake.** Treating every paired low flop as an automatic small range bet in position.

**Numbers.** GTO c-bet ~57% on 774 two-tone BTN vs BB

**Hooks.** _Paired low board, in position. Not a range bet._ · _Why 774 belongs to the big blind._ · _'Always c-bet paired boards' is costing you money._

Review: [ ]

### Ace-high and king-high prefer to check on 774
`c-cash-6max-tc17-high-cards-check-774-002` · intermediate · flop · srp · btn · consensus 0.50 · sources: 2cc · **draft**

**Claim.** Unpaired high cards such as KJs or AT are the biggest checking category for the button on 774. Check them, take a turn card, and keep your six outs instead of betting.

**Why.** A bet with king-jack on 774 gets called by almost everything that beats it and folds out very little that it loses to. The big blind's weak hands that fold were already behind you. Meanwhile a check-raise would push you off a hand with live overcards and backdoor equity. Checking realises that equity for free, keeps your checking range from being too weak, and leaves the turn bet available if you improve or a scare card comes.

**Common mistake.** Betting high-card hands because the board is low, then folding six live outs to a check-raise.

**Hooks.** _King-jack on 774: the bet that only gets called by better._ · _Checking here makes you more money than betting._ · _Six outs you throw away every time you c-bet._

Review: [ ]

### C-bet about 80% on K72 two-tone as the button, checking some showdown hands
`c-cash-6max-tc32-cbet-80-on-k72-001` · intermediate · flop · srp · btn · consensus 0.50 · sources: 2cc · **draft**

**Claim.** In a single-raised pot, button versus big blind, K72 two-tone is a high-frequency c-bet board. Theory bets about 80%, and betting the whole range would be at most a tiny error. The checks are lower top pairs, underpairs, second and third pairs, and a lot of ace-high and queen-high hands.

**Why.** A king-high dry board gives the raiser a large range and nut advantage, so most hands profit from betting. The hands that check share one trait, good showdown value against a range that rarely has them beaten and will not fold many better hands to a bet. Ace-high and queen-high hands beat most of the big blind's misses and lose little by checking, so they take a free card and keep the checking range from being pure air.

**Numbers.** GTO c-bet ~80% on K72 two-tone BTN vs BB

**Hooks.** _K72 in position: bet almost everything, but not quite._ · _Which hands check back a king-high board? Showdown value._ · _Range-betting K72 is barely a mistake. Here is the exception._

Review: [ ]


## turn-play  (21)

### Barrel scare cards against regulars, check them against recreational players
`c-cash-6max-br1-barrel-regs-not-fish-014` · beginner · turn · srp · ip · consensus 0.50 · sources: br79 · **draft**

**Claim.** A turn overcard that is a fine double-barrel against a regular is often a check against a weak player. The regular reads the card and folds marginal pairs; the weak player calls with pairs anyway and actually holds the scare card more often because their range is wide.

**Why.** A barrel works through two mechanisms: the opponent folding hands you beat, and the card being less likely in their range than in yours. Against a tight regular both hold. Against a player who plays half their hands, the ace or king on the turn is in their range all the time, and when it is not they still call with second pair. Both legs of the bluff collapse, so checking and realizing your own equity is better.

**Common mistake.** Applying "always barrel the ace" as a rule regardless of who is in the hand.

**Hooks.** _Same turn card, two opponents, two different plays._ · _The scare card does not scare a player who never folds._ · _'Always barrel the ace' is costing you money._

Review: [ ]

### Unsure what to do if shoved on? Checking two pair on the turn is fine
`c-cash-6max-br3-check-two-pair-turn-001` · beginner · turn · srp · ip · consensus 0.50 · sources: br79 · **draft**

**Claim.** When you hold two pair or a similar strong-but-not-nut hand on a turn that completes a flush with deep stacks behind, and you do not know how you would respond to a check-raise all-in, checking is acceptable. You can usually collect a bet on the river anyway.

**Why.** Against most micro opponents you were never getting two more full bets from their calling hands; they call once with a pair and fold to the second bet, or they hold the flush and raise. Betting the turn therefore mostly exposes you to a raise you cannot handle while adding little value. Checking and betting the river gets the same single bet from the hands that would have called, keeps the pot controlled against the hands that beat you, and lets you see what they do with a free card. It is not the sin that "always bet two pair" thinking makes it out to be.

**Common mistake.** Betting the turn out of obligation, facing a shove, and making a guess for stacks.

**Hooks.** _Checking two pair here makes you more money. Here is why._ · _'You have to bet two pair' is costing you stacks._ · _You will not get two bets anyway. So take one safely._

Review: [ ]

### Barrel the turn only with a clear reason; otherwise let the small pot go
`c-cash-6max-br3-no-barrel-without-reason-002` · beginner · turn · srp · ip · consensus 0.50 · sources: br79 · **draft**

**Claim.** Do not fire a second barrel without a made hand unless you have a specific reason, such as stats showing the opponent is a thinking regular who floats flops and folds turns. With no information, or against a recreational player, check back and let them win the small pot.

**Why.** A turn bluff needs folds, and the players who fold turns are regulars who read boards. Weak players call with any pair and any draw, so barrelling them without a hand is money lost most of the time. Giving up a small pot costs little; the profit comes from the big pots you win when you connect against those same players. Barrelling "because you are supposed to" is a habit that bleeds chips and invites tilt when it fails.

**Common mistake.** Double-barrelling an unknown three hands into the session because the flop c-bet got called.

**Hooks.** _'Bet, bet, bet' is advice for a different opponent._ · _Why the second barrel is a leak at NL5._ · _Lose the small pots on purpose. Win the big ones._

Review: [ ]

### Do not auto-barrel the turn with strong non-nut hands when a bet only folds out worse
`c-cash-6max-br5-check-turn-with-strong-non-nut-hand-012` · intermediate · turn · srp · any · consensus 0.50 · sources: br79 · **draft**

**Claim.** When your hand is well ahead of an opponent's medium holdings, such as trips versus a top-pair type, but a turn barrel would fold out everything you beat and get called only by hands that beat you, check. You keep the weaker hands in for a river bet or call, and you avoid bet-folding a strong hand.

**Why.** Micro-stakes players call one bet with a mediocre hand far more readily than two. If you bet the turn, ace-high or a weak pair folds and you win a small pot; if you check, that same hand often bets the river or calls your river bet. The check also adds deception, and when the opponent does hold the nuts, their river bet is often sized so small that you can call profitably with outs to improve. Checking is not giving up: with trips you still call any turn bet, and you let them put in dead money.

**Common mistake.** Barrelling every turn out of habit, then folding trips to a raise or winning only the small pot that a bet-fold line allows.

**Schools disagree.** Solver-informed play barrels strong hands on most turns for value and protection; the coach argues the micro population over-folds medium hands to a second barrel, so checking earns more.

**Hooks.** _Checking the turn here makes you more money. Here is why._ · _Trips on the turn. Most players bet. We check._ · _Bet-folding a strong hand is a leak. Fix it._

Review: [ ]

### After winning a pot off an active player, consider a delayed c-bet instead of firing again
`c-cash-6max-br7-delayed-cbet-vs-players-who-play-back-014` · beginner · flop · srp · ip · consensus 0.50 · sources: br79 · **draft**

**Claim.** When an aggressive or stubborn micro player has just lost a pot to you, expect them to play back at your next c-bet regardless of their hand. Against that player checking the flop in position and betting the turn, or letting them bluff into you, often beats the automatic c-bet.

**Why.** Players at these limits are fickle; losing a pot makes them want to punish you on the next one, often with a raise or a float they would not normally make. A flop c-bet into that mood invites a raise you cannot continue against. Checking back removes the trigger, lets them take the lead with air, and gives you a cheaper look at the turn where your bet is more credible. It is a timing adjustment, not a change of strategy.

**Common mistake.** C-betting into a player who just lost a pot to you and then folding to the inevitable raise, repeating the pattern every orbit.

**Hooks.** _Just won a pot off him? Skip the next c-bet._ · _The delayed c-bet is built for stubborn opponents._ · _Fickle players tell you when they will play back._

Review: [ ]

### A scare-card turn is a barrel against regulars, but a check against weak players
`c-cash-6max-br7-do-not-barrel-fish-on-scare-cards-003` · beginner · turn · srp · ip · consensus 0.50 · sources: br79 · **draft**

**Claim.** When the turn brings a high card that beats your opponent's likely pairs, such as a king over a jack-high flop, fire a second barrel against a regular almost every time. Against a loose passive player, check instead: they call far too wide for the card to do its job, so take your free card or show down cheaply.

**Why.** A second barrel on a scare card works because a thinking player recognizes that your range contains the card and folds their medium pairs. Weak players do not run that logic; they look at their own hand, see a pair, and call. Barrelling them with air just builds a pot you are losing, and barrelling them with a draw costs you the chance to see the river cheaply. Save the aggression for value against this type and the scare-card bluffs for regulars.

**Common mistake.** Firing a second barrel on the king because "it is a great card for my range", without checking whether the opponent is capable of folding a pair.

**Hooks.** _Great barrel card. Wrong opponent._ · _The king turn: bet against regs, check against fish._ · _Scare cards only scare players who are paying attention._

Review: [ ]

### Second-barrel only when the turn card actually worries the hand they are likely holding
`c-cash-6max-br8-barrel-only-cards-that-scare-their-hand-010` · beginner · turn · srp · ip · consensus 0.50 · sources: br79 · **draft**

**Claim.** Before firing a second barrel, name the hand your opponent most likely called the flop with and ask whether the turn card changes anything for it. A jack does not scare a player holding a king; a seven does not scare pocket nines. An ace often does. If the card does not threaten their hand, check and try to improve rather than bluff.

**Why.** Micro-stakes players decide with their own hand in mind, so a barrel works only when the new card makes that specific hand feel beaten. A broadway card below their pair, or a low card on a high board, leaves their confidence intact and they call. An overcard to their pair, especially an ace, is the card that produces folds. Barrelling selectively keeps your bluffs cheap and your second barrels believable when you do fire.

**Common mistake.** Firing the turn on any "new" card because the flop c-bet got called, without asking what the opponent is holding and whether the card hurts it.

**Hooks.** _That turn card does not scare him. Do not barrel._ · _Name his hand first. Then decide whether to fire._ · _Why the jack is a bad barrel card. The ace is good._

Review: [ ]

### Medium pair on an ace-high board: bet once and stop, you are way ahead or way behind
`c-cash-6max-br8-way-ahead-way-behind-one-and-done-011` · beginner · turn · srp · any · consensus 0.50 · sources: br79 · **draft**

**Claim.** Holding something like pocket nines on an ace-high flop, make one continuation bet and then check the turn and river unless something changes. If they have the ace you are far behind and a second barrel will not move them; if they have a lower pair you are far ahead and a second bet only folds them out. There is no hand to protect against and nothing to bluff.

**Why.** Way-ahead-way-behind spots are defined by the absence of draws that can change the order of hands. When the opponent's range splits into hands far ahead of you and hands far behind, betting again gains nothing from either part: the better hands call or raise, the worse hands fold. Checking keeps the pot small when behind and often earns a river call or bluff from the worse hands when ahead. One bet to take it down, then pot control.

**Common mistake.** Barrelling nines on an ace-king-x board to "find out", folding out the pairs you beat and paying off every ace.

**Hooks.** _One bet, then stop. The way-ahead-way-behind rule._ · _Pocket nines on an ace-high board: never barrel._ · _Betting again here can only hurt you._

Review: [ ]

### After checking back the flop, bluff the turn or the river, but never show down air
`c-cash-6max-cc03-delayed-cbet-never-check-down-016` · intermediate · turn · srp · ip · consensus 0.50 · sources: cc · **draft**

**Claim.** A delayed c-bet is more bluff-friendly than a double barrel because the opponent never had to call a bet and his range is still full of air. Betting the turn with air or waiting to bet the river when checked to are close in EV. What is a serious mistake is checking all the way down with a hand that cannot win at showdown while your range retains the advantage.

**Why.** The out-of-position caller folds well above the pot-odds baseline here: against a 33% bet, symmetric ranges would fold about a quarter, but the actual fold rate in a solver example was around 42%, and on the river he folds even more. That is why both timings work: betting now harvests fold equity while he still has junk; waiting lets him realise a little equity but saves money against his strong hands and sets up a bigger river fold rate. A small size suits the turn because your checked-back range has fewer monsters. The pure error is doing neither and losing the pot with queen-high on a board where he is folding more than enough to make almost any bet profitable.

**Common mistake.** Checking the flop, checking the turn, then checking the river with queen-high "because I never showed strength".

**Numbers.** neutral break-even vs a 33% pot bet: 25% folds · example delayed c-bet spot: opponent folds ~42% to 33% pot

**Hooks.** _Checked back the flop? You can still bluff. You must._ · _Queen-high, check, check, check. The quietest way to lose._ · _He folds 42% to a third pot. Why are you checking?_

Review: [ ]

### Probe the turn with air only when you have a draw to a nutted hand
`c-cash-6max-cc03-turn-probe-unfavorable-010` · intermediate · turn · srp · oop · consensus 0.50 · sources: cc · **draft**

**Claim.** After the in-position raiser checks back the flop, the out-of-position caller is usually in an unfavourable range situation on the turn. Bluff-probing with pure air is then worse than folding would be. Lead only with hands that can make a very strong hand by the river, such as flush draws and gutshots, or with real value.

**Why.** The raiser's checking range stays stronger than the caller's range, and he has position, so he defends a little more than the pot odds require. Pure air cannot recover when called: even hitting a pair on the river rarely wins and never earns another bet. A draw changes the maths because the times you get called and then hit, you win not just the current pot but an extra river bet, and those implied odds can lift the lead from losing to acceptable. In a solver example, nine-high overbetting the turn here was worth about -3% of the pot while checking kept +3.6%. The exception is low, connected turns that smash the caller's range, where leading becomes close to a range bet.

**Common mistake.** Leading the turn with nothing after a check-back because "he showed weakness", then paying off when he calls.

**Numbers.** example: nine-high overbet probe ~-3% pot EV vs check ~+3.6%

**Hooks.** _He checked back. That doesn't mean he's weak._ · _Betting here is worse than open-folding your hand._ · _Probe the turn with a draw or don't probe at all._

Review: [ ]

### After a flop bet gets called, the caller often holds the turn equity lead
`c-cash-6max-cc06-flop-action-changes-turn-range-advantage-007` · intermediate · turn · srp · ip · consensus 0.50 · sources: cc · **draft**

**Claim.** Range advantage on the turn depends on the flop action, not just the turn card. When the in-position raiser c-bets big and the big blind calls, the big blind's condensed range frequently has more equity on the turn than the bettor's polarized range, especially when the turn pairs the middle of the board.

**Why.** Two things move range equity between streets - the new card and what each player did. Players remember the card and forget the action. The caller has folded their junk and kept middle pairs, top pairs and draws; the bettor has kept value and bluffs, and the bluffs are now the weak part of their range. On a jack-ten-four flop, a ten on the turn turns a huge chunk of the caller's middling range into trips. A solver shows the bettor sitting around 43% range equity there. That is why turn barrels become selective - the aggressor still bets, but only with real value, equity-driven bluffs, or hands with good blockers. A smaller flop bet condenses the caller less and dissipates the bettor's edge more slowly, but the direction is the same.

**Common mistake.** Looking at a turn card, deciding "nothing changed, same texture" and assuming the preflop raiser still has the advantage they held before the flop action.

**Numbers.** Example: aggressor ~43% vs caller ~57% range equity on JT4 with a T turn after a 75% c-bet and call

**Hooks.** _The turn card didn't change anything. The flop call did._ · _Why your turn barrels fail after they call a big c-bet_ · _Who really has the equity lead on the turn?_

Review: [ ]

### Range advantage raises your betting frequency, it does not license betting every hand
`c-cash-6max-cc06-range-advantage-does-not-make-every-hand-bet-006` · beginner · turn · srp · ip · consensus 0.50 · sources: cc · **draft**

**Claim.** A big range advantage means more of your hands want to bet. It never overrides what your specific hand wants. A medium-strength hand with showdown value still checks even when your range is far ahead.

**Why.** The reasons for betting have not changed - value, bluffing, and a little equity denial. Range advantage makes those reasons apply to more hands, but a hand that is too weak to be called by worse and too strong to turn into a bluff gains nothing from betting. Betting it might even be profitable in isolation, yet checking is worth more, and the goal is the best line, not a line that happens to be above zero. Your opponent still defends sensibly, continuing with the better part of their range and folding the worst, so a bet with a middling hand buys nothing it did not already have.

**Common mistake.** Checking back a middle pair on the flop, then firing a large turn bet with it after a blank because "I have the range advantage here".

**Example.** positions: CO vs BB | hero: 8c8d | board: Th6s2c Qd | action: CO opens, BB calls. Flop checks through. Turn Q: BB checks, CO bets 75% pot. | decision: Is a 75% turn bet with 88 correct given CO's range advantage on this runout? | answer: No. 88 has showdown value and beats most of what folds while losing to most of what calls. Check and often win at showdown. Range advantage guides range strategy, not this hand's choice.

**Hooks.** _Your range is ahead. Your hand still should not bet._ · _The turn bet that is +EV and still a blunder_ · _Range advantage is not a free pass to bet anything_

Review: [ ]

### A range disadvantage makes you selective, not passive
`c-cash-6max-cc06-range-disadvantage-still-bet-strong-hands-008` · intermediate · turn · srp · ip · consensus 0.50 · sources: cc · **draft**

**Claim.** When your range is behind on the turn you still bet your strong hands. The disadvantage shows up as a more polarized betting range - fewer thin value bets and bluffs chosen for blockers or equity - not as checking everything.

**Why.** If nine out of ten cookies are ruined, the tenth is not inedible; it is the only one worth eating. A set when your range is weak is exactly that cookie. The opponent's range is strong, they will invest, and your hand is happy to build a pot. What changes is the margin. Second pair that would be a fine value bet against a weak range becomes a never-bet, because the caller's range is now dense with hands that beat it. Random no-equity bluffs become too expensive, so bluffs need a flush blocker, a draw, or a card that removes the opponent's continues. Range disadvantage trims the edges of your betting range; it does not remove the middle of it.

**Common mistake.** Learning about range disadvantage and then checking a set or betting second pair for thin value in the same spot, in both cases ignoring the specific hand.

**Example.** positions: CO vs BB | hero: 4h4d | board: Jc Th 4s Td | action: CO c-bets 75% on the flop, BB calls. Turn T: BB checks. | decision: CO's range is behind now that the ten paired. Bet or check with the set? | answer: Bet. The set wants a big pot and villain's range is strong enough to pay. J9 in the same spot never bets - too thin against a range full of Tx and Jx.

**Hooks.** _Range behind? Bet your set anyway. Here's what changes._ · _Range disadvantage means fewer bets, not zero bets._ · _The one hand you must never barrel on this turn_

Review: [ ]

### Turn barrels are usually big and infrequent - nut edge without range edge
`c-cash-6max-cc06-turn-barrel-nut-edge-without-range-edge-017` · intermediate · turn · srp · ip · consensus 0.50 · sources: cc · **draft**

**Claim.** The typical turn after a c-bet and call is a spot where the bettor has a nut advantage but no longer a range advantage. The right response is to bet a small share of your range and to bet it large.

**Why.** The flop call condensed the opponent toward medium hands and raised their range equity, often past yours. Your range, however, still holds the hands they rarely have - sets, overpairs, the strong value you bet the flop with - and those hands sit at the top of the equity distribution. So the range as a whole does not want to bet often, but the hands that do bet want a big pot. This is why the standard turn barreling range is polarized and sized up - it is the natural outcome of two separate inputs, one saying "rarely" and the other saying "big". Recognizing the pattern stops you from either barreling too wide or betting your strong hands too small.

**Common mistake.** Barreling the turn with the same wide range and small size that worked on the flop, after the opponent's call has already caught their range up.

**Hooks.** _Why turn barrels are big and rare - it's not style_ · _They called the flop. Now bet less often, but bigger._ · _The most common post-flop pattern, explained_

Review: [ ]

### Judge the turn world, not the turn card
`c-cash-6max-cc07-favorability-is-the-whole-world-007` · beginner · turn · srp · any · consensus 0.50 · sources: cc · **draft**

**Claim.** How favourable a turn spot is depends on five things together: the preflop ranges, the flop, the flop action, position, and the turn card. The fourth card is just one of five inputs and only a quarter of the board.

**Why.** Players often say "the queen is good for him" and then act as though the first three cards disappeared. They did not. The same queen on the same flop can be a strong barrel card after a small bet and call in position, and a mediocre one out of position after a large bet. Position alone shifts EV by several percent of the pot in every spot, so a card that creates a neutral world for the in-position bettor can create an unfavourable one for an out-of-position bettor with identical ranges. Sorting spots into favourable, neutral and unfavourable is the skill to practise, and it is impossible if you only look at the fourth card.

**Common mistake.** Deciding whether to barrel based purely on whether the turn card "looks good" for the preflop raiser.

**Hooks.** _One card out of four. Stop treating it like the whole board._ · _Same card, same flop, opposite decision. Why?_ · _Most players evaluate turns wrong in the first second._

Review: [ ]

### Favourability sets how strict your turn value and bluff thresholds are
`c-cash-6max-cc07-favorability-sets-your-thresholds-011` · intermediate · turn · srp · any · consensus 0.50 · sources: cc · **draft**

**Claim.** Classify the turn world first, then set your standards. Favourable: bet 60%+ of the time, value bet thin and bluff almost any hand. Neutral: bet around 35-40%, raise the value bar and pick bluffs by blockers and draws. Unfavourable: bet around 20%, only strong value and premium draws, and protect your checking range.

**Why.** Your opponent's folding frequency is a reaction to your betting range. In a favourable world their range is weak enough that even trash gets enough folds to be indifferent with checking, and marginal hands like second pair become value bets because the top of their range is missing. In a neutral world they fold a little less than the bet size requires, so an air bluff is already a loser and only hands with equity or good blockers may bet. In an unfavourable world they are condensed around hands that connect, they will raise more, and your medium-strong hands drop below the value line entirely. The same hand can be a mandatory bet in one world and a mandatory check in another; the hand did not change, the world did.

**Common mistake.** Using one fixed turn barrel frequency regardless of how the card, position and action sequence changed each range.

**Numbers.** Favourable world: barrel ~60%+; neutral: ~35-40%; unfavourable: ~20% · Neutral-world example: BB folds ~40.6% vs ~42.7% needed for a 75% pot bluff to break even

**Hooks.** _Three turn worlds, three different rules. Which one are you in?_ · _The same hand is a must-bet here and a must-check there._ · _Your bluff standards should move. Most players' don't._

Review: [ ]

### Calling the flop strengthens their range, so turn barrels are rarely range bets
`c-cash-6max-cc07-flop-call-condenses-turn-barrels-selective-004` · intermediate · turn · srp · ip · consensus 0.50 · sources: cc · **draft**

**Claim.** When the flop caller folds their weakest hands, their remaining range gets stronger on average, and on the turn they usually hold the equity edge. So after a flop c-bet is called, barrel the turn selectively, around 40-60% of the time on a blank, rather than betting your whole range.

**Why.** Betting the flop filters your opponent for you: their air leaves, their pairs and draws stay. A range built only from hands that passed a strength test is condensed, and condensed is not weak, it is simply short on nutted hands. Their equity jumps, yours stays flat or drops slightly even though your nut share remains high. Range-betting a turn into that stronger range hands them profitable calls and raises. The exceptions are rare cases where the turn card hugely favours you, like a king arriving on a low board in a 3-bet pot where overpairs dominate. Otherwise expect to bet roughly half the time, more in favourable worlds and sometimes as little as 20-30% when the turn is bad for you.

**Common mistake.** Treating "they called my c-bet" as weakness and firing the turn with everything, which pays off a range that just removed all its trash.

**Numbers.** Blank-turn barrel frequency after flop bet-call: ~40-60% on average · In bad turn worlds the frequency can fall to ~20-30%

**Hooks.** _They called your flop bet. Their range just got stronger._ · _Range-betting the turn is almost never right. Here's the one exception._ · _The 50% rule for turn barrels._

Review: [ ]

### Out of position on a bad turn, check most of your range, including the nuts
`c-cash-6max-cc07-oop-unfavorable-check-heavy-015` · intermediate · turn · srp · oop · consensus 0.50 · sources: cc · **draft**

**Claim.** When you c-bet out of position and the turn connects with the caller's range, bet only around 20% of the time. There are no mandatory value bets: even your strongest hands can check at some frequency, because the in-position player will bet often when checked to.

**Why.** Being out of position is a constant tax on your EV, and a turn that favours the condensed caller pushes the world into unfavourable territory. Their range will raise more and fold less, so medium-strong hands like top pair with a weak kicker fall below the value line and air can never bet. Checking a monster here costs little: there is a whole river left, the opponent bets frequently into a check, and you can check-raise. The occasional missed bet when they check behind is recovered by the raises you get in and the bluffs you induce. A low flush with about 75-80% equity is a genuine mix between betting and checking, not a forced bet. Only strong exploitative reads, such as an opponent who never bets when checked to, should swing you back toward betting.

**Common mistake.** Betting every flush and every strong hand out of position because it feels like missing value otherwise, leaving a checking range that stronger regulars attack.

**Numbers.** Unfavourable OOP turn world: bet ~20%, EV around 47% of pot · Weak flush OOP (~75-80% equity): roughly indifferent between bet and check

**Hooks.** _Checking the nuts out of position is not a slow-play. It's correct._ · _You don't have to bet your flush. Here's the proof._ · _Out of position on a bad turn? Bet 20%, not 60%._

Review: [ ]

### Positional slow-play rule - IP check strong-not-nutted hands, OOP check anything
`c-cash-6max-cc07-positional-slow-play-rule-016` · intermediate · turn · srp · any · consensus 0.50 · sources: cc · **draft**

**Claim.** In position on the turn, your checking range should contain some strong but not nutted hands (a good top pair, a weak flush) while the true nuts almost always bet. Out of position, keep the checking range fully uncapped: every hand, including the nuts, checks at some frequency.

**Why.** The driver is urgency, meaning how much money a hand still needs to get in before the river and how much time it has. In position the nuts own too much of the pot to let a street go by, so they must bet; a strong-ish hand gains from checking because it loses less when behind, lets weaker hands bluff the river and keeps hands in that would have folded. Out of position the opponent still has the option to bet when you check, so checking a monster does not lose a street; it often gains one via a check-raise. The one discipline is that when you do check a big hand OOP and they bet small, raise rather than call, because calling and checking again lets time run out. None of this is exploitative guesswork: the equilibrium strategy checks these hands too.

**Common mistake.** Assuming "I'm in position, I always bet my strong hands" and "I'm out of position, I must bet before they check behind", which produces face-up checking ranges in both seats.

**Hooks.** _In position, check your good hands. Out of position, check anything._ · _The nuts don't always need to bet the turn._ · _One rule for slow-playing that depends only on your seat._

Review: [ ]

### Build more flop checks into your plan to reach profitable delayed lines
`c-cash-6max-gp36-checking-opens-delayed-lines-012` · advanced · multi-street · 3bet-pot · oop · consensus 0.50 · sources: rio · **draft**

**Claim.** A strategy that checks the flop more often as the 3-bettor reaches delayed c-bet and check-check-check lines more often, and those lines hold extra EV against most opponents. Choose flop simplifications partly for how often they get you there.

**Why.** Players defend flop c-bets reasonably well because they face them constantly, but turn probes, delayed bets after a flop check-through and river decisions after two checks are studied far less and played worse. The only way to get to those nodes is to check the flop. If the flop check costs almost nothing in theory on a texture, the practical upside of the later streets makes range-checking there a clear choice rather than a toss-up.

**Common mistake.** Judging a flop check only by the flop EV and ignoring the easier turn and river spots it leads into.

**Hooks.** _The best spots in 3-bet pots start with a flop check._ · _Check now, collect on the turn. The delayed-line edge._ · _Why checking the flop is an investment, not a surrender._

Review: [ ]

### Ace turns on 774 shut off the medium-strength barrel
`c-cash-6max-tc16-ace-turn-medium-hands-check-004` · intermediate · turn · srp · btn · consensus 0.50 · sources: 2cc · **draft**

**Claim.** When an ace lands on the turn of 774 after the big blind calls your c-bet, barrel your value and your bluffs but check pocket kings through jacks, underpairs, weaker top pairs and third pairs. This holds in theory and against real opponents alike.

**Why.** On an ace turn the hands that will check-call another bet are mostly Ax that just improved. Weaker holdings such as 4x and pocket eights through tens exist in the big blind's range but at low frequency, and most of those either fold or already lose to you. So a pocket-kings barrel folds out what you beat and gets called by what beats you. A hand with no showdown value does not share that problem, which is why bluffs keep betting while medium hands check and realise their equity.

**Common mistake.** Firing overpairs on the ace for protection when the only hands that continue are the aces that already have you beaten.

**Hooks.** _Pocket kings on an ace turn: stop betting._ · _Why bluffs barrel the ace but overpairs check._ · _The turn card that flips who bets on 774._

Review: [ ]


## river-play  (10)

### With showdown value on the river, check rather than bluff
`c-cash-6max-br2-showdown-value-no-bluff-008` · beginner · river · srp · ip · consensus 0.50 · sources: br79 · **draft**

**Claim.** If your hand can win at showdown against some of the opponent's missed draws and weak pairs, check the river instead of betting. A bet only gets called by better and folds out the hands you already beat.

**Why.** A river bet does one of two things: it wins extra money from worse hands that call, or it makes better hands fold. A medium-strength hand achieves neither against a typical micro opponent: their worse hands fold or were never betting anyway, and their better hands call. Checking lets you realize the equity you already have. Turning a hand with showdown value into a bluff throws away the one thing it does well.

**Common mistake.** Betting ace-high or a weak pair on the river "because they might fold" and being called by second pair.

**Hooks.** _You have showdown value. Why are you bluffing?_ · _The river check that wins more than a bet._ · _Ace-high on the river is a check, not a bet._

Review: [ ]

### On a scary river against a fish, check-call to let them bluff with nothing
`c-cash-6max-br3-check-river-induce-bluff-009` · beginner · river · srp · oop · consensus 0.50 · sources: br79 · **draft**

**Claim.** When a flush or straight completes on the river and you hold a decent but non-nut hand against a weak player, check and call rather than bet. Their nonsense hands that would fold to a bet will often bet themselves, and you collect from hands that had zero intention of calling.

**Why.** A river bet into a completed draw gets called by the draws and folded by everything else. A check gives the weak player room to make a mistake: they frequently fire with air on a scary board because the card "looks like" a bluffing opportunity. You lose nothing against the hands that got there, since they would have raised your bet anyway, and you gain a bet from the air. Keep the sizing of your call sensible and accept that sometimes they have the hand.

**Common mistake.** Blocking-betting the river and folding out every hand that would have bluffed.

**Hooks.** _Checking the river here makes you more money than betting._ · _Scary river, weak opponent. Let them do the betting._ · _The bet they make with nothing is yours if you check._

Review: [ ]

### At micro stakes a river raise is almost always the nuts, so value bet without fear
`c-cash-6max-br5-river-raises-are-the-nuts-005` · beginner · river · srp · any · consensus 0.50 · sources: br79 · **draft**

**Claim.** Players at NL2-NL10 almost never raise the river light. That cuts both ways: when you bet for thin value and get raised, fold easily; and stop skipping thin river value bets because you are afraid of being raised. Bet around half pot against a player who will call with any pair.

**Why.** Fear of a river raise is the most common reason weaker players leave value on the table. But the population at these stakes raises rivers with strong hands only, so the raise carries very little risk: you simply fold and lose nothing more than the bet. Meanwhile loose players call river bets with second pair, third pair and middling pocket pairs all day. The combination of easy folds versus raises and frequent calls from worse hands makes the thin river bet clearly profitable.

**Common mistake.** Checking back a medium-strength hand on the river to avoid being raised, then paying off a raise when it does come.

**Numbers.** ~half pot for thin river value against a sticky player

**Hooks.** _Scared to bet the river? That fear costs you money._ · _A river raise at NL5 means one thing._ · _The simplest river rule for micro stakes._

Review: [ ]

### On the river, if worse hands will not call but ace-high might bluff, check and call
`c-cash-6max-br6-check-river-to-let-ace-high-bluff-014` · beginner · river · srp · oop · consensus 0.50 · sources: br79 · **draft**

**Claim.** Holding a medium-strength hand on the river out of position, ask what calls a bet. If the answer is almost nothing you beat, but the opponent is the type to bet ace-high or a missed draw when checked to, check with the intention of calling. You win the same pot plus their bluff.

**Why.** A river bet with a medium hand only profits when worse hands call. Against many micro players, worse hands fold and better hands call, so betting is zero or negative value. Checking turns their aggression into your profit: they bluff with the hands that would have folded, and you call. If they check back, you lose nothing compared to the bet that would not have been called anyway. The key is a read that this player does fire at checked rivers.

**Common mistake.** Betting the river with second pair "for value", getting called only by better, and never giving the opponent the chance to bluff.

**Hooks.** _Checking this river wins more than betting it._ · _Give him the rope: a river line most NL5 players never use._ · _Nothing worse calls. So why are you betting?_

Review: [ ]

### Do not bluff when your hand already beats every hand that would fold
`c-cash-6max-br8-do-not-bluff-when-you-beat-everything-that-folds-009` · beginner · river · srp · ip · consensus 0.50 · sources: br79 · **draft**

**Claim.** In position on the river against a weak player, if your medium hand beats all the missed draws and loses to all the pairs, check. A bet only folds out hands you were already beating and gets called by hands that beat you. The same applies on the turn when a flush draw misses: if they have the draw, you are effectively holding the nuts against it and there is nothing to bluff.

**Why.** A bluff makes money by folding out better hands. When every hand that folds is worse than yours, the bluff has no target, and when every hand that calls is better, the bet has no value either. Against a player who calls with any pair, that describes most medium hands on the river. Checking takes the free showdown and wins exactly the same pots a bet would have won, without ever paying off a better hand.

**Common mistake.** Betting middle pair on a brick river "to represent the flush", folding out only ace-high and getting called by every pair.

**Hooks.** _You cannot bluff a hand you already beat._ · _Middle pair on the river vs a fish: check, every time._ · _The bluff that folds out only worse hands._

Review: [ ]

### Before calling a river bet from a passive player, ask whether they are capable of bluffing
`c-cash-6max-br8-river-call-vs-passive-player-check-aggression-015` · beginner · river · srp · any · consensus 0.50 · sources: br79 · **draft**

**Claim.** Facing a river bet with a medium hand, first ask whether this opponent ever bluffs. Against a passive player with a very low aggression factor, lean towards folding: they have a real hand almost every time they bet. Against a player who has shown aggression, the call is fine. A weak-looking line of your own invites the odd stab and pushes a close spot back towards a call.

**Why.** Bluff-catching only profits when the opponent's betting range contains bluffs. Passive players bet when they have it and check when they do not, so their river bets are value-heavy and your medium hand is usually beaten. A low aggression factor is the stat that captures this, though it needs a large sample to trust. Your own line is the other input: a passive line from you invites the occasional bluff, which pushes a borderline spot back towards a call.

**Common mistake.** Calling every river bet with second pair "because he could have anything", against a player who has never been seen to bluff.

**Hooks.** _Can this player bluff? Answer before you call._ · _A low aggression factor should make you fold more rivers._ · _The one question that decides most river calls._

Review: [ ]

### Called the flop, he checked back the turn, you missed: bet the river almost always
`c-cash-6max-cc03-river-busted-draw-after-checkback-018` · intermediate · river · srp · oop · consensus 0.50 · sources: cc · **draft**

**Claim.** When you call a flop c-bet out of position, the in-position player checks the turn, and you reach the river with a busted draw, bluff. Your flop call purged the air from your range while his turn check often means he is giving up with his flop bluffs, so your fold equity is far above the break-even point and checking is worth nothing.

**Why.** Calling a bet condenses a range: the junk folds and what remains is stronger on average. The flop bettor, by contrast, often bets a wide or polarised range and then checks the turn with its weak part. On the river that leaves you with the range advantage and him with plenty of hands that fold to one bet. Blocker details barely matter in this spot; a missed gutshot and a missed flush draw should both bet. Because a no-showdown-value check and a fold are identical on the river, every fold you collect is pure profit over checking.

**Common mistake.** Checking a missed flush draw to the in-position player "in case he bets", when he will mostly check back and win with ace-high or a weak pair.

**Example.** positions: BTN vs BB | hero: 9h8h | board: Kh 6h 2c 3s Qd | action: BTN opens, BB calls. BB checks, BTN bets 33%, BB calls. Turn: check, check. River: BB to act. | decision: Check or bet with the missed flush draw? | answer: Bet. BB's flop call removed his air, BTN's turn check is often a give-up, and checking wins nothing.

**Hooks.** _He checked back the turn. That's your green light._ · _Missed your flush? Good. Now bet the river._ · _Blockers don't matter here. Betting does._

Review: [ ]

### When the hand checks through to the river and you kept the range advantage, bluff your air
`c-cash-6max-cc03-river-must-bluff-checked-down-017` · intermediate · river · srp · ip · consensus 0.50 · sources: cc · **draft**

**Claim.** If you raised preflop against a blind caller and both players checked every street, your range is still stronger than his on the river. With a hand that cannot win at showdown you must bet, because there is no later street to delay to and checking with nothing equals folding. "I can't represent anything after checking twice" is a myth.

**Why.** In equilibrium the raiser's checking ranges are protected with plenty of showdown value, so checking does not turn his range into junk; both ranges weaken a little and the gap carries through. The opponent therefore has to fold a lot to a river bet, and real opponents with similar ranges tend to fold even more than the maths requires. A solver example with queen-high after three checks showed a pure bet to a 3/4-pot size, with the opponent folding far above the 43% break-even. Since a no-showdown-value check is worth zero, any bet that gets those folds beats it by the entire profit of the bet.

**Common mistake.** Checking down eight-high after check-check-check and calling it "the honest line", when it is simply surrendering a pot your range owns.

**Numbers.** 75% pot river bluff breaks even at ~43% folds; favourable checked-down rivers fold well above this

**Hooks.** _'I checked twice, I can't rep anything.' Wrong._ · _Check, check, check, show down eight-high. Never again._ · _On the river, checking air is just folding._

Review: [ ]

### After checking flop and turn in position, your river range is mostly unpaired high cards
`c-cash-6max-gp32-checked-down-range-is-high-cards-001` · intermediate · river · srp · ip · consensus 0.50 · sources: rio · **draft**

**Claim.** When the hand checks through to the river in a single-raised pot, the in-position player holds very few pairs and a lot of king-high and ace-high hands. Build your river strategy around that fact rather than around the strong hands you would have bet earlier.

**Why.** Pairs and better bet the flop or turn most of the time, so they rarely reach a checked-down river. What arrives is the hands that had nothing to bet with: unpaired Broadway cards, some weak pairs that checked once, and air. On low boards that means your value comes from a king or ace that is now the best hand far more often than it looks, and your bluffs come from the weakest unpaired hands. Thinking about which hands actually survive the line is what makes the river thresholds make sense.

**Common mistake.** Checking king-high on a low river out of habit, when it is near the top of the range that takes this line.

**Hooks.** _King-high on the river is often your value hand._ · _You checked twice. Now what's actually in your range?_ · _Why ace-high bets rivers more than you think._

Review: [ ]

### Ace-high checks back only when you have many hands of similar strength
`c-cash-6max-gp32-showdown-value-needs-company-006` · intermediate · river · srp · ip · consensus 0.50 · sources: rio · **draft**

**Claim.** Whether an unpaired high card checks or bets on a checked-down river depends on how many similar hands share your range. Ace-high checks on textures where you hold a lot of comparable showdown-value hands; on textures where it is near the top of your range, it bets for value.

**Why.** A hand checks back when betting would mostly fold out worse and get called by better. For that to be true of ace-high you need a dense band of hands at roughly its strength, so that checking is the natural plan for a whole class and the opponent cannot exploit the checks. On low boards where the in-position range is thin on pairs, ace-high and king-high may be the best hands you can hold and betting half pot for value becomes correct.

**Common mistake.** Treating ace-high as an automatic check on every river regardless of what the rest of the range looks like.

**Hooks.** _Ace-high: check or value bet? Depends on your range._ · _Checking here makes you more money than betting. Here's why._ · _The showdown-value rule that isn't about your hand._

Review: [ ]


## bluffing  (17)

### When a passive player checks to you twice, take a stab at the pot
`c-cash-6max-br1-two-checks-means-weakness-015` · beginner · turn · srp · ip · consensus 0.50 · sources: br79 · **draft**

**Claim.** If a weak player checks the flop and then checks the turn again, a bet in position usually wins the pot even without a hand. Two checks from someone who bets their good hands means they very rarely have anything.

**Why.** Recreational players are inconsistent in many ways but consistent in one: when they hold something they like, they bet. Two consecutive checks are therefore an honest signal of a missed hand or a draw. A small to medium bet gets through often enough to be profitable, and when they do call with a draw you still have the river to see what develops. This is one of the few cheap bluff spots that works against non-folders, precisely because they have nothing to call with.

**Common mistake.** Checking behind on the turn with air after two checks because "they never fold", when there is nothing in their hand to fold.

**Hooks.** _The one spot where bluffing a station actually works._ · _Two checks from a fish is a flashing green light._ · _Check, check. Now bet. They have nothing._

Review: [ ]

### Raise your draws when a fold is likely: two ways to win beat one
`c-cash-6max-br5-raise-draws-two-ways-to-win-011` · beginner · flop · srp · any · consensus 0.50 · sources: br79 · **draft**

**Claim.** Facing a bet with a flush draw and nothing else, on a board where the bettor often gives up, raise instead of calling. You can win right now when they fold, and you still have the draw as a backup if they continue. The same logic is why you raise rather than limp preflop.

**Why.** Calling with a draw has exactly one way to win: hitting. Raising adds fold equity on top of that, and at micro stakes opponents give up a lot after a single raise. When the raise fails you are not dead; you still have outs, and sometimes a free river card after your show of strength. Giving yourself the maximum number of paths to the pot is the core reason aggression wins in this game, before and after the flop.

**Common mistake.** Calling every draw passively and only winning the pots where the card arrives.

**Hooks.** _Calling a flush draw wins one way. Raising wins two._ · _Seven-high, flush draw, facing a bet. Raise._ · _The real reason aggression wins at micro stakes._

Review: [ ]

### Heads-up against micro players: make top pair, value bet, skip the river bluffs
`c-cash-6max-br6-keep-heads-up-simple-no-river-bluffs-002` · beginner · river · any · consensus 0.50 · sources: br79 · **draft**

**Claim.** Short-handed against weak opponents, keep the game extremely simple. Raise wide, c-bet, and when you make top pair, bet it for value on every street. Do not try to bluff rivers, even when it would probably work; the player types you meet here call too much for bluffs to be a reliable profit source.

**Why.** Weak players' defining leak is calling too wide and too long, which makes value betting hugely profitable and bluffing marginal. A river bluff that works once is offset by the many times a station calls with bottom pair. By sticking to value with top pair or better and checking back the rest, you remove variance and let their calling habit pay you. You do not need a heads-up specialist's game to beat these spots; you need discipline and position.

**Common mistake.** Treating heads-up as a licence to bluff every river, against the one player type that never folds.

**Hooks.** _The bluff would have worked. We still did not make it._ · _Heads-up at NL5 is simpler than you think._ · _Top pair and discipline beat fancy heads-up plays here._

Review: [ ]

### Bluff-raise weak donk bets on dry paired boards, but never bluff with zero outs
`c-cash-6max-br7-bluff-raise-donk-bets-but-always-with-outs-011` · beginner · flop · srp · ip · consensus 0.50 · sources: br79 · **draft**

**Claim.** When a wide-range player leads into you on a dry paired flop such as eight-four-four, raise rather than call or fold: it is very hard for them to have anything, and players who donk often fold to a raise even if they ignore 3-bets preflop. Do it with at least a gutshot, though. A bluff with no way to improve has only one way to win, and that is not enough.

**Why.** Donk bets from loose players are usually weak pairs, draws or probes, and a dry paired board gives them almost no strong holdings. A raise makes them fold most of that range immediately. Insisting on some outs is cheap insurance: when the bluff gets called you still have a chance to win, which turns a pure gamble into a semi-bluff. Players who 3-bet-proof their preflop game often still fold to flop raises because the stakes feel bigger, so this is a reliable spot against them.

**Common mistake.** Calling a small donk bet with nothing to "see what happens", or bluff-raising with a hand that cannot improve on any turn card.

**Numbers.** a donk-bet stat of ~33% over 6 opportunities already flags a frequent leader

**Hooks.** _He leads into you on a paired board. Raise._ · _The one rule we never break when bluffing._ · _Why a gutshot is the minimum for any bluff._

Review: [ ]

### A better hand is not a better bluff: compare bet vs check for the hand you hold
`c-cash-6max-cc03-compare-actions-not-hands-014` · intermediate · turn · srp · consensus 0.50 · sources: cc · **draft**

**Claim.** Whether to bluff is the difference between the EV of betting and the EV of checking with your actual hand. A flush draw is worth more than queen-high, but if both have bet EV equal to check EV, both are equally optional bluffs. "I'd rather bluff with a draw" compares hands, not actions, and is irrelevant.

**Why.** In a double-barrel spot the solver may bet a flush draw and an unpaired queen-high at similar frequencies. The draw is entitled to roughly 30% of the pot whatever it does; the queen-high to about 5% whatever it does. Neither gains anything by betting over checking, which is exactly what makes them optional. Players bet the draw far more often than the air because bluffing with equity feels less troubling, but a feeling about the hand is not evidence about the action. You are choosing between the two options available with these cards, not wishing for different cards.

**Common mistake.** Checking the turn with air because "we have better bluffs in our range", which is a statement about which hands you would prefer, not about which action is higher EV.

**Numbers.** example: flush draw ~31% pot EV, queen-high ~5% pot EV, both indifferent between bet and check

**Hooks.** _You'd rather have a flush draw. You don't. Now decide._ · _'We have better bluffs' is an emotion, not an argument._ · _Both hands bluff the same amount. One just feels nicer._

Review: [ ]

### You do not need a draw to barrel the turn when your range is doing fine
`c-cash-6max-cc03-no-comfort-blanket-013` · intermediate · turn · srp · ip · consensus 0.50 · sources: cc · **draft**

**Claim.** In position with a normal range on a dry runout, betting the turn with pure air after your c-bet is called is fine and often optional in theory, and better than fine against opponents who fold too much. Requiring a draw, backdoor or overcard as a "get-out clause" before bluffing means your betting range is far too strong.

**Why.** Your value hands sit at the top of your range and your semi-bluffs just below them. If you only barrel those, you bet an unbalanced, top-heavy range and give up the pot with everything else. A hand like queen-high on K-7-3-8 is entitled to only a few percent of the pot whichever way it is played, so betting it costs nothing relative to checking while adding the bluffs your range needs. Fold equity comes from the range-versus-range situation, not from your own card quality. The exception is a runout that hammers your range; then even air with no outs must check, unless it has nut potential.

**Common mistake.** Checking back pure air on the turn with "nothing to rep" and only barrelling when holding some equity, making bluffs easy to spot and too rare.

**Example.** positions: BTN vs BB | hero: QhJc | board: Kd 7s 3c 8h | action: BTN opens, BB calls. BB checks, BTN c-bets, BB calls. Turn: BB checks. | decision: Barrel with queen-high and no draw? | answer: Yes, at some frequency. Range is in a fine spot, fold equity is normal, and checking is worth almost nothing with this hand.

**Hooks.** _Bluffing with nothing on the turn is normal. Here's why._ · _Only bluff with draws? Your range is far too strong._ · _Queen-high, no draw, dry turn. Bet it._

Review: [ ]

### Most bluffs are optional; in a neutral spot, bet or check and never regret the result
`c-cash-6max-cc03-optional-bluffs-dont-agonize-015` · intermediate · multi-street · srp · consensus 0.50 · sources: cc · **draft**

**Claim.** C-betting the turn after a called flop bet, delayed c-bets, flop bets with a slight range edge and most triple barrels are optional bluffs: betting and checking are close in EV. Pick one, and if you bet and get called, do not conclude the bet was wrong.

**Why.** Once the opponent has called a flop bet his range has condensed, so neither side holds a large range edge on the turn; that near-neutrality is exactly what makes bluffs optional. If betting air were clearly winning or clearly losing, someone would be playing badly and it would not be equilibrium. In these spots a bad hand is entitled to a small share of the pot by either route; bluffing earns that share through fold equity rather than by improving. Without a specific read that the opponent over- or under-folds, the choice barely matters, so there is nothing to agonise over and nothing to learn from one call.

**Common mistake.** Barrelling, getting called, and deciding "he obviously had it, I should never bluff there" after a single outcome.

**Hooks.** _Most bluffs don't matter. Stop agonising over them._ · _He called your bluff. That proves nothing._ · _Bet or check: when both are fine, just pick one._

Review: [ ]

### Every bluff spot is forbidden, optional or mandatory; two factors decide which
`c-cash-6max-cc03-three-bluffing-worlds-008` · intermediate · multi-street · consensus 0.50 · sources: cc · **draft**

**Claim.** Sort bluffing decisions into three buckets: cannot bluff (checking is better), optional (bet and check are about equal), and must bluff (checking loses a lot). Two inputs decide the bucket: how much showdown value your hand has, and how favourable the range-versus-range situation is for you.

**Why.** High showdown value raises the value of checking, so bluffing has a higher bar to clear. A favourable range situation raises your real fold equity above what the pot odds alone suggest, so bluffing clears the bar more easily. Most spots in the middle of the hand are optional because the aggressor has a modest range edge that is roughly offset by the caller's filtered range. Must-bluff spots cluster on the river when you still hold the range advantage and there is no later street to bluff. Cannot-bluff spots require either too much showdown value or a badly unfavourable world, and there are fewer of them than beginners think. When quizzed, "optional" is the safe guess.

**Common mistake.** Treating bluffing as a binary "is this a bluff spot" instead of asking how big the gap between betting and checking is.

**Hooks.** _Can't bluff, can bluff, must bluff. Which one is this?_ · _Two questions decide every bluff. Most players ask neither._ · _Most bluffs don't matter. A few are mandatory._

Review: [ ]

### At the micros, missing a required bluff costs more than any calling error
`c-cash-6max-cc03-underbluffing-biggest-leak-004` · beginner · multi-street · consensus 0.50 · sources: cc · **draft**

**Claim.** Facing a bet limits your options, so calling mistakes tend to be small. When you have the free choice to bet or check, the errors are far bigger, and the most frequent large blunder at low stakes is failing to bluff in spots that demand it. If you genuinely cannot work out a spot, lean towards betting.

**Why.** Most low-stakes players have learned not to stack off with weak hands, but they have not learned to win the pots their range is entitled to. When your range is much stronger than your opponent's and the hand reaches the river, the opponent has to fold more often than the break-even point, and checking throws away a pot that was yours to take. Bluffing in bad spots does happen, but it is the rarer and usually smaller error. That asymmetry is why the default when unsure should be aggression, not caution.

**Common mistake.** Checking down queen-high or eight-high after a check-check-check sequence and feeling virtuous for "not spewing".

**Hooks.** _The most expensive mistake at NL10 is a bet you never made._ · _Calling errors are small. Betting errors are huge._ · _Not sure whether to bluff? That's usually a bluff._

Review: [ ]

### A pure bluff flips "usually losing" into "always winning"; denial only adds a sliver
`c-cash-6max-cc03-why-bluffs-beat-denial-002` · beginner · multi-street · consensus 0.50 · sources: cc · **draft**

**Claim.** Bluffing, like value, can justify a bet by itself. Denial cannot. When you bluff, each fold turns a hand that would lose most of the time into a won pot; when you bet for protection, most of the pot was already yours and a fold only adds a small extra share.

**Why.** A denial bet asks a hand with 15-20% equity to fold, so the gain is at most that slice. A pure bluff asks a hand with 90%+ equity to fold, so the gain is close to the whole pot. That is why the downside of bluffing (you lose nearly every time you are called) is worth accepting: the upside is enormous when your range lets you make the opponent fold more often than the break-even frequency. Semi-bluffs feel nicer because they sometimes win when called, but that does not make pure bluffs wrong; you should still bluff with no equity at some frequency on the flop and turn.

**Common mistake.** Treating protection as the main reason to bet while never putting in a bet whose only purpose is to make better hands fold.

**Hooks.** _Protection bets gain crumbs. Bluffs gain the whole pot._ · _Usually losing, always winning. That gap is why you bluff._ · _Semi-bluffs feel safer. They are not more correct._

Review: [ ]

### Rank the world first, then your draw - five tiers of unmade hands on the turn
`c-cash-6max-cc07-draw-ladder-world-first-018` · beginner · turn · srp · any · consensus 0.50 · sources: cc · **draft**

**Claim.** Sort your unmade turn hands into premium draws, decent draws, marginal draws, semi-trash and utter trash. Premium draws may bet in any world; each weaker tier needs a more favourable world before it is allowed to bluff. Judge the world before you judge the hand.

**Why.** A flush draw or open-ended straight draw has enough equity to bail itself out, so it can barrel even when your range is suffering. A decent draw, such as a good gutshot or two live overcards, bets almost always but may sit out in a horrible world. A marginal draw, like a weak gutshot or one overcard with a backdoor, needs at least a neutral world. Semi-trash, a lone overcard or a flush blocker, needs a favourable one, and complete air with no outs and poor blockers can bet only in the very best worlds. The important habit is the order: players who start from "my hand is weak, I won't bluff" under-bluff favourable turns badly, where even air should bet sometimes. This ladder is about what can bet, not what must bet, and applies to the turn specifically.

**Common mistake.** Starting from the hand ("only a gutshot, not good enough") instead of the world, so you never bluff enough when the turn is great for your range.

**Hooks.** _Is your draw good enough? Wrong question._ · _Five kinds of draws, one question: can this one bet?_ · _Most players judge their hand first. That's backwards._

Review: [ ]

### Their fold frequency is a reaction to what you bet, so trash bluffs lose in neutral spots
`c-cash-6max-cc07-fold-equity-reacts-to-your-betting-range-013` · intermediate · turn · srp · any · consensus 0.50 · sources: cc · **draft**

**Claim.** A 75% pot bet needs roughly 43% folds to break even as a pure bluff. In neutral or unfavourable turn worlds the caller folds less than that against a well-built range, so bluffing with no draw and no blockers loses money compared with checking.

**Why.** Fold equity is not a property of the spot; it is a response to your betting range. The caller folds a given amount because your bets are selective. If you start firing random junk, the solver, or an observant opponent, calls more and your fold equity drops further. So the 40% fold rate you see in a neutral world is the best case for a disciplined range, and already below the breakeven for air. Hands with a flush draw or overcards still have equity to fall back on, so they can bet; a hand with nothing cannot. In practice humans fold even less on connecting turns than theory suggests, which makes the restraint more valuable, not less.

**Common mistake.** Reading a 40% fold stat and thinking "they fold a lot", then bluffing every air hand into it until the stat stops being true.

**Numbers.** 75% pot bluff breakeven: ~43% folds (42.7%) · Neutral turn world after bet-call: caller folds ~40%; unfavourable: lower still

**Hooks.** _One number decides whether your turn bluff works: 43%._ · _They don't fold 'a lot'. They fold to a disciplined range._ · _Why your bluffing stat lies to you._

Review: [ ]

### On a checked-down river, every hand below the showdown line bluffs
`c-cash-6max-gp32-bluff-everything-below-threshold-004` · intermediate · river · srp · ip · consensus 0.50 · sources: rio · **draft**

**Claim.** Once you have identified which hand class is your weakest showdown-value hand on a given river, everything weaker should bet. If king-high is the bottom of your checking range, then queen-high and below bluff close to always.

**Why.** Checked-down pots are small and the opponent's range is weak, so bluffs need to fold out very little to profit. The in-position range holds many unpaired hands, and the ones that cannot win at showdown have no reason to check. Players tend to pick a few "good-looking" bluffs and check the rest, which leaves their betting frequency far too low. Find the threshold hand, then be systematic below it.

**Common mistake.** Bluffing only with hands that have a blocker or a story and checking the rest of the air.

**Hooks.** _Queen-high on the river? That's a bet, every time._ · _You pick bluffs. The solver bluffs a whole class._ · _The river bluff rule nobody follows._

Review: [ ]

### A pair is a showdown hand, not a bluff, even when the board gets scary
`c-cash-6max-gp32-dont-bluff-a-pair-005` · beginner · river · srp · ip · consensus 0.50 · sources: rio · **draft**

**Claim.** When a four-straight or four-flush arrives on the river and you hold a pair that is now unlikely to be best, check it back. Turning a pair into a bluff is almost never right in a checked-down pot because the hand still beats the opponent's air.

**Why.** In a hand where both players checked flop and turn, the opponent's range is full of unpaired hands and weak draws that missed. A pair beats all of that at showdown for free. Bluffing with it risks a bet to fold out hands you already beat and only gets called by hands that beat you. The right bluffs are the hands with no showdown value at all, which you have plenty of after checking twice.

**Common mistake.** Bluffing bottom pair when the straight completes because "I can't win at showdown anyway".

**Hooks.** _Four to a straight on the river. Don't bluff your pair._ · _A pair beats air. Stop betting it as a bluff._ · _Scary board? Your pair still shows down._

Review: [ ]

### The max exploit on 774 turns barrels bluffs and slow-plays value
`c-cash-6max-tc16-max-exploit-bluff-heavy-barrel-005` · advanced · turn · srp · btn · consensus 0.50 · sources: 2cc · **needs-review** · review note: _Max-exploit line; publish only framed as theoretical ceiling (see tc17-007)._

**Claim.** If the big blind will never adapt, the maximum exploit on 774 keeps the turn barrel frequency near the solver's but changes what bets. On blank turns only king-high, queen-high and worse hands bet, while trips and better check and slow-play.

**Why.** The real big blind check-raised more flush draws and A7 on the flop, so their calling range reaches the turn with fewer strong hands and fewer draws. A range that cannot continue often enough is best attacked with air, because each extra bluff shows an immediate profit. Value hands earn more by checking and letting a weaker range catch up or bluff. Lower overpairs plus second and third pairs still bet some 6x-type turns for protection, and on high flush turns value bets return because the population does keep a few low flushes in its calling range.

**Common mistake.** Copying only the frequency of an exploit and not its composition; betting the same share of hands with the solver's value-heavy mix leaves most of the gain unused.

**Numbers.** max-exploit barrel frequency close to GTO ~54% · blank-turn composition almost all bluffs

**Hooks.** _Same bet frequency, totally different hands. That is the exploit._ · _Why trips check the turn against most players._ · _The solver bets only air here. Seriously._

Review: [ ]

### 3-bet your best flush draws and suited-card blockers on 774
`c-cash-6max-tc18-3bet-flush-draws-and-blockers-005` · advanced · flop · srp · btn · consensus 0.50 · sources: 2cc · **draft**

**Claim.** Against a big blind who check-raises 774 with extra flush draws, re-raise high flush draws such as ace-x suited far more, about 21% versus under 5%, and add offsuit ace-high or king-high hands that hold a single card of the flush suit as bluffs.

**Why.** When the raiser has more flush draws, your higher flush draws dominate theirs, so getting money in with ace-high or king-high suited draws is close to a value play rather than a pure semi-bluff. The offsuit hand with one suited card works differently. It blocks the draws that would call your 3-bet, and the big blind's backdoor-flush check-raises cannot continue against the re-raise. A few suited broadways like QJ, JT and T9 also re-raise to fold out air, but that slice of the range is small.

**Numbers.** flush draws 3-bet ~21% vs <5% GTO · high-card region 3-bet ~18.5% vs ~3% GTO

**Hooks.** _Your flush draw dominates theirs. Raise it._ · _One spade in an offsuit hand turns it into a 3-bet._ · _The semi-bluff that is secretly a value raise._

Review: [ ]

### Overbluff low turns on K72 against a big blind who does not adjust
`c-cash-6max-tc31-overbluff-low-turns-003` · advanced · turn · srp · btn · consensus 0.50 · sources: 2cc · **draft**

**Claim.** On low turns such as a four, the maximum exploit against a typical big blind barrels its value plus a huge bluff share, nearly every queen-high or worse hand and A8 and lower, close to half of all ace-high hands and far above the solver's bluff count.

**Why.** The population check-raises sets, more two pair and more good top pairs on the flop, including top pair with a flush draw. Those are exactly the hands that would check-call a turn barrel, so once they have moved into the check-raising range the remaining caller folds the turn too often. The solver's answer is to flood the barrel with bluffs. Against an opponent who would readjust this edge disappears, but real opponents take a long time to notice, so the aggressive line often works in practice.

**Numbers.** max exploit on a 4x turn: Q-high and worse barrel · A8 and lower barrel, roughly half of ace-highs

**Hooks.** _A four hits the turn. Bluff with half your ace-highs._ · _Their best callers already raised the flop. So bluff._ · _Why the solver over-bluffs low turns against real players._

Review: [ ]


## value-betting  (15)

### Do not check big hands hoping a passive player will bet for you
`c-cash-6max-br1-put-the-money-in-yourself-009` · beginner · multi-street · any · consensus 0.50 · sources: br79 · **draft**

**Claim.** With a strong hand against a passive micro-stakes player, bet yourself on every street. Checking to induce only works against aggressive opponents; the typical weak player will check behind and you lose a whole street of value.

**Why.** Trapping relies on the opponent putting chips in on their own. Players at these stakes are passive by nature: they call a lot but bet rarely. Every time you check a set or two pair to them, the most likely outcome is a free card and a smaller pot. Since they call bets with a very wide range anyway, there is nothing to gain from disguise and a lot to lose from silence. Be the one who puts the bets in.

**Common mistake.** Checking top set on the flop "to let them catch up" and watching the hand check through two streets.

**Hooks.** _Checking your set to a station is the costliest move at NL5._ · _They will not bet for you. Ever. Bet yourself._ · _'Let them catch up' costs you a street every time._

Review: [ ]

### To win a stack from a sticky player, bet big on every street
`c-cash-6max-br2-build-pot-with-big-bets-014` · beginner · multi-street · any · consensus 0.50 · sources: br79 · **draft**

**Claim.** When you flop a strong hand against a player who has been calling everything, bet close to pot on each street. Big pots are only built with big bets, and this type of opponent is the one who will pay them.

**Why.** Stack-to-pot ratio decides whether you can get all the money in by the river. Three bets of a third pot leave most of the stacks behind; three pot-sized bets get everything in. The normal objection, that large bets make them fold, does not apply to a player who has shown they call light. When they also like to shove over bets with weak hands, a big bet both builds the pot and invites the mistake.

**Common mistake.** Betting small with a big hand against a station "to keep them in" and winning a third of the stack you could have had.

**Numbers.** Pot-sized bets on each street vs sticky players

**Hooks.** _Want their stack? Three pot bets gets you there._ · _Small bets build small pots. Even against a station._ · _The pot button is your friend when they never fold._

Review: [ ]

### With the nuts on a wet board, bet near pot now before scare cards arrive
`c-cash-6max-br3-bet-big-before-scare-cards-015` · beginner · flop · srp · any · consensus 0.50 · sources: br79 · **draft**

**Claim.** When you flop a very strong hand on a board with flush and straight draws, bet close to the full pot and keep betting. Slow-playing risks a turn or river card that kills your action, and against players who do not give you credit anyway there is nothing to disguise.

**Why.** Every draw-completing card either makes the opponent's hand or scares them off, and both outcomes reduce what you win. Getting the money in while your hand is clearly best and their draws still look alive maximizes the pot you play for. Micro-stakes players also call big bets with pairs and draws, so there is no benefit in betting small to keep them in. The rare exception for slow-playing is a hand like flopped quads where nothing can beat you and no card changes that.

**Common mistake.** Betting a third of the pot with the nut straight on a two-flush board and watching the flush complete.

**Numbers.** Bet roughly pot-sized with the nuts on wet boards

**Hooks.** _Slow-playing the nuts on a wet board costs you the stack._ · _Bet pot now. The next card might not let you._ · _The one hand you are allowed to slow-play. Quads._

Review: [ ]

### Stack off for value against a fish even if a regular behind might have you beat
`c-cash-6max-br3-ship-for-value-vs-fish-despite-reg-005` · beginner · flop · multiway · any · consensus 0.50 · sources: br79 · **draft**

**Claim.** In a multiway pot where an active weak player is betting with a wide range, get your strong one-pair hand like top pair top kicker all-in against them. The possibility that a tighter player still in the hand holds better does not outweigh how often you win a big pot from the fish.

**Why.** Decisions are made against the whole range of hands in play, weighted by how much money each opponent puts in. The weak player is shoving worse hands often enough that your hand is a clear favourite against their range. The regular may occasionally show up with a monster, but they are in the pot less often with a strong hand than the fish is with a weak one, and when the regular folds you win a large side pot from the fish anyway. Folding out of fear of the regular surrenders the main source of profit in the hand.

**Common mistake.** Folding a strong hand in a multiway pot because "the tight player could have a set" while the fish is shoving with ace-rag.

**Hooks.** _The reg might have it. Ship anyway. Here is the math._ · _Play the player who is shoving, not the scary one._ · _Side pots are where the fish pays you._

Review: [ ]

### Against weak players: big hand, big pot; medium hand, small pot
`c-cash-6max-br6-big-hand-big-pot-vs-fish-015` · beginner · multi-street · srp · any · consensus 0.50 · sources: br79 · **draft**

**Claim.** Versus a loose passive opponent the plan is simple. With top pair and a strong kicker, two pair or better, bet big on every street and aim to get stacks in. With medium hands, keep the pot small, check back the awkward turns and take the cheap showdown. Do not get fancy in either direction.

**Why.** Weak players pay off big hands because they call with a wide range of worse pairs and draws, so slow-playing or small-betting a strong hand against them leaves money on the table. The flip side is that they are unpredictable with medium hands and will sometimes show up with the one holding that beats you, so bloating a pot with a marginal hand buys variance without extra value. Match pot size to hand strength and let their calling habit do the rest.

**Common mistake.** Betting small with a monster to keep the fish in, or betting big with a medium hand to "find out where you are".

**Hooks.** _Four words that beat weak players: big hand, big pot._ · _Stop slow-playing against the one player who always calls._ · _Match your pot size to your hand. That is the whole plan._

Review: [ ]

### With a monster against a weak player, bet close to pot on all three streets
`c-cash-6max-br8-bet-near-pot-every-street-with-a-monster-vs-fish-017` · beginner · multi-street · srp · any · consensus 0.50 · sources: br79 · **draft**

**Claim.** When you hold a full house or similar lock against a loose passive player, the default line is to bet near pot on the flop, turn and river. Against a very bad player you can size even larger. They call with any piece, so small bets only leave money behind.

**Why.** Weak players do not fold a king on a paired board or a flush draw on the turn, and they rarely raise, so there is no reason to disguise your hand or keep the pot small. Three near-pot bets get the most money in by the river against a range that calls each one. The temptation to bet small to keep them in is misplaced: they are staying in anyway, and the only question is how much they pay.

**Common mistake.** Betting a third of the pot with a full house to avoid scaring off a player who would have called pot.

**Numbers.** bet close to pot on every street with a monster vs a weak player

**Hooks.** _Full house versus a fish: bet pot, pot, pot._ · _Small bets with monsters are the most expensive habit at NL10._ · _They are calling anyway. Charge them._

Review: [ ]

### Occasionally betting the river into a better hand means your value frequency is right
`c-cash-6max-br8-occasional-value-town-means-right-frequency-006` · beginner · river · srp · ip · consensus 0.50 · sources: br79 · **draft**

**Claim.** When you bet the river for value and get called by a better hand, do not treat it as a mistake to eliminate. If it happens from time to time, you are betting thin enough. If it never happens, you are checking back too many rivers that worse hands would have called.

**Why.** Micro-stakes players call rivers with surprisingly weak hands, so the profitable value-betting range is wider than it feels. The only way to be in that range is to occasionally run into the top of the opponent's calling range. A player who never gets "value-towned" has set their threshold too high and is leaving a steady stream of thin river bets unmade. Judge the frequency, not the single outcome, and keep betting when worse can call.

**Common mistake.** After one river bet gets called by a better hand, tightening up and checking back every medium-strength river for the rest of the session.

**Hooks.** _Got called by a better hand on the river? Good sign._ · _If you never value-town yourself, you are leaving money behind._ · _The river mistake that proves you are doing it right._

Review: [ ]

### Judge value bets by equity after the call; flop action moves that number
`c-cash-6max-cc03-finishing-equity-threshold-006` · intermediate · turn · srp · consensus 0.50 · sources: cc · **draft**

**Claim.** Judge a value bet by your equity against the hands that continue, not against the whole range before you bet. You want about 50-55% after the call. A pair plus a draw on a wet board after a big flop bet often lands near 40% and should check; a small pair on a dry board after the flop checked through can bet a third pot and still be comfortably ahead.

**Why.** A big flop bet filters your opponent's range hard, so by the turn he holds mostly hands that beat middle pair plus a gutshot; another big bet is too thin. When the flop was checked through on a texture he rarely connects with, his range is full of unpaired hands, so a small turn bet with a low pair gets called by worse and denies equity to all the live overcards. Two small sources of equity (a pair and a draw) added together do not automatically reach the value threshold. Checking is also entitled to a big share of the pot, so "I beat some hands" is not enough.

**Common mistake.** Seeing that you are a favourite before betting and concluding it is a value bet, without asking what you are up against once he calls.

**Numbers.** target finishing equity for a value bet: ~50-55% · middle pair + gutshot after a 75% flop c-bet is called: ~39-40% finishing equity, check

**Hooks.** _You were the favourite. You bet. Now you're the underdog._ · _Pair plus draw on the turn: value bet or spew?_ · _One number decides your thin value bet: equity after the call._

Review: [ ]

### Treat protection as a tiebreaker, never as the reason you bet
`c-cash-6max-cc03-protection-is-a-modifier-003` · intermediate · turn · srp · consensus 0.50 · sources: cc · **draft**

**Claim.** Decide first whether a bet is value or a bluff. Only after that should denial nudge a close decision. "This pair needs protection" should never on its own produce a bet, because a hand that truly needed protection would show a clear EV gap between betting and checking.

**Why.** On a dry turn with a range of medium pairs, the solver often mixes jacks, nines and sevens at similar frequencies. The lower pairs gain more from denial because more of the opponent's hands are live against them, but they also get called by more better hands, so their finishing equity is lower. The two effects cancel, which is why all of them are optional bets. The bigger pairs still bet a little more often, because value is a far stronger reason than protection. If denial is the only thing driving you, you are solving the problem in the wrong order.

**Common mistake.** Betting a vulnerable low pair "because it needs protection" while checking a stronger pair that would be the better value bet.

**Hooks.** _'My pair needs protection' is not a reason to bet._ · _Jacks, nines, sevens: same bet frequency. Here's why._ · _Protection is a tiebreaker. Value is the reason._

Review: [ ]

### 'He could have the nuts' is not a reason to check
`c-cash-6max-cc06-do-not-fear-the-nuts-011` · beginner · multi-street · any · consensus 0.50 · sources: cc · **draft**

**Claim.** Whether to value bet or bluff comes from estimating your equity and your opponent's folding range, not from whether a hand that beats you is possible. Sometimes you bluff into the nuts and get snapped, and that is correct.

**Why.** The opponent can nearly always hold something that beats you. The question is what share of their range it is. If flushes are 5% of their continuing range and the rest is worse than your hand, you value bet and accept the occasional cooler. If you only bluff when the nuts are impossible you never bluff, because they are rarely impossible. Fear of the worst case is wired into us - our instincts rank threats above opportunities - and running badly makes it louder, which is when players stop thin value betting and stop bluffing entirely. Replace the fear with a frequency - how often is that hand actually there?

**Common mistake.** Checking a strong hand or abandoning a bluff because "there are sets in his range", without asking how big that part of the range is.

**Hooks.** _Refuse to bluff into the nuts? Then you never bluff._ · _'He might have a flush' is costing you money._ · _The fear that stops you betting for value_

Review: [ ]

### "I bet for value" is an incomplete thought; a weak flush on the turn is often a check
`c-cash-6max-cc07-i-bet-for-value-is-a-bad-thought-017` · intermediate · turn · srp · ip · consensus 0.50 · sources: cc · **draft**

**Claim.** Deciding to bet because a hand is "a flush" or "strong" skips the real question: is checking also viable? On a flush-completing turn in position, a low flush is frequently a pure check, while only the near-nut flushes must bet.

**Why.** Three things argue for checking a low flush. First, blockers: holding two of the suit removes many of the drawing hands that would call your bet, so you are betting into a range that continues less. Second, relative strength: several higher flushes beat you, and checking gets you closer to showdown while losing less against them. Third, you unblock their air; hands that called the flop with overcards will often bluff the river after you check, paying you money that a turn bet would have folded out. A king-high or nut flush is different because it cannot be behind and owns too large a share of the pot to wait. Thinking "strong hand, bet" ignores all of this and makes your range easy to read for anyone paying attention.

**Common mistake.** Betting every flush on the turn because it feels like a strong hand, then wondering why the river never produces bluffs when you check.

**Example.** positions: BTN vs BB | hero: 8c7c | board: Qc9c4d 2c | action: BTN opens, BB calls. Flop: BTN bets 33%, BB calls. Turn: a third club, BB checks. | decision: Bet the flush or check back? | answer: Checking is at least as good and often better. Your two clubs block the draws that would call, you lose to every bigger flush, and checking lets BB bluff the river with the overcards they floated with. Only the top flushes here have to bet.

**Hooks.** _You made a flush. Checking it might be the only correct play._ · _'I bet for value' is costing you money._ · _Why the small flush should sometimes stay quiet on the turn._

Review: [ ]

### In a favourable turn world, second pair is a value bet and value drives the bluffs
`c-cash-6max-cc07-thin-value-when-they-cannot-have-the-card-012` · intermediate · turn · srp · ip · consensus 0.50 · sources: cc · **draft**

**Claim.** When the turn card is one the caller almost never holds, your value range widens dramatically: a hand that is now second pair can still bet for value, and because you are value betting so often, your draws and even your air may bet alongside.

**Why.** Value betting is about being ahead of the hands that call, not about absolute strength. If the turn king is nearly absent from the caller's range, your jack-high top pair from the flop is still ahead of most continuing hands, so it bets. A wide value range needs bluffs to balance it, which is why hands like Q-T with a draw bet very often, and why even low offsuit junk can bet: the fold equity is high enough that betting and checking are equal. Note the order of causation. Value hands drive the aggression; the bluffs simply tag along because the strategy wants a high frequency. Betting trash is not better than checking it, it is merely allowed. Even here the very middle of your range, like a weak pocket pair under the board, still has to check.

**Common mistake.** Checking second pair on a king turn because "it's only second pair now", ignoring that the king barely exists in the caller's range.

**Example.** positions: BTN vs BB | hero: JcTc | board: Js6d3h Kd | action: BTN opens, BB calls. Flop: BTN bets 33%, BB calls. Turn: king, BB checks. | decision: Is this a check-back or a value bet? | answer: A value bet is fine. BB folded almost all king-high on the flop and 3-bet much of it preflop, so the king rarely helps them. Your pair of jacks is still ahead of most hands that call, and the world is favourable enough to bet around 75% pot.

**Hooks.** _Second pair. King turn. Bet for value. Here's why._ · _Your bluffs aren't the reason you're betting. Your value is._ · _'Only second pair' is the wrong way to think about this._

Review: [ ]

### On a four-straight river, a strong ace-high can still bet pot after a checked-down hand
`c-cash-6max-gp32-ace-still-pots-on-four-straight-007` · advanced · river · srp · ip · consensus 0.50 · sources: rio · **draft**

**Claim.** A four-card straight on the board does not kill value for the in-position player who checked twice. The opponent's range is weak, so a hand like ace-high or top pair remains a value bet, and pot-size bets are frequently correct.

**Why.** In a checked-down pot neither player has shown strength, so the chance the opponent holds the straight is low. Meanwhile the board scares the opponent's medium hands, and the in-position range is heavy in the exact high cards that benefit from a large size. The solver often bets big here precisely because the opponent is capped and the hand has enough showdown strength to be called by worse. Fear of the four-straight is a population leak, not a reason to check.

**Common mistake.** Checking back a strong ace or top pair when the straight completes, because the board "looks too dangerous".

**Hooks.** _Four to a straight. Ace-high. Bet pot._ · _The scary river you should be betting big on._ · _Checking back the four-straight is a leak._

Review: [ ]

### Half pot is the main river size after a checked-down hand, and it goes thin
`c-cash-6max-gp32-half-pot-dominant-thin-value-002` · intermediate · river · srp · ip · consensus 0.50 · sources: rio · **draft**

**Claim.** On most textures where the hand checks to the river, the solver's most common in-position bet is around half pot, and it uses that size with second pair, weak top pair and even small pocket pairs. Pot-size bets are reserved for the top of the range on textures where the opponent holds a lot of calling hands.

**Why.** The opponent who checked three times is capped and holds many weak pairs and unpaired hands. A half-pot bet gets called by enough of those hands to make value bets with medium strength profitable, while keeping the loss small when you run into something better. Going big with everything folds out exactly the hands you want to be called by. Players who default to pot leave a layer of thin value unbet, which quietly lowers their river betting frequency.

**Common mistake.** Checking middle pair or a low pocket pair on the river because it does not feel strong enough for a pot-size bet, instead of sizing down.

**Numbers.** Example texture: top pair ~23% of river range; another ~11% of second pair and low pocket pairs value bet at half pot

**Hooks.** _Second pair on the river. Bet half pot, don't check._ · _The river size most players never use enough._ · _Pocket deuces can value bet this river. Really._

Review: [ ]

### 3-bet sets and top two more often when the K72 check-raiser is stronger
`c-cash-6max-tc33-3bet-sets-two-pair-more-005` · intermediate · flop · srp · btn · consensus 0.50 · sources: 2cc · **draft**

**Claim.** Against a big blind whose check-raising range on K72 holds more sets, two pair and good top pairs than theory, re-raise your sets and top two pair more often, and add some top pairs and pocket aces to the 3-bet range.

**Why.** A stronger raising range continues more often against a 3-bet, sometimes by 4-betting. That is bad news for your bluffs but good news for your best hands, because you get more money in while ahead than the solver would against a weaker theoretical raise. The biggest jump in 3-bet frequency sits exactly in the two-pair-and-set region, with top pairs and pocket aces rising a little as well.

**Hooks.** _Stronger check-raise range? Good. Raise your sets._ · _When they stop bluffing, charge them more with the nuts._ · _Why a set should 3-bet K72 against real players._

Review: [ ]


## check-raising  (14)

### Check a strong hand to induce only when you are nearly certain the opponent will bet
`c-cash-6max-br6-induce-only-when-they-will-bet-006` · beginner · multi-street · srp · any · consensus 0.50 · sources: br79 · **draft**

**Claim.** Checking the nuts to let an opponent bet into you is only correct against a player who is aggressive, tilted, or otherwise very likely to fire. Against a passive or tight player who checks behind most of the time, just bet. The inducing play fails far more often than people posting hands online seem to think.

**Why.** The check-to-induce line has two costs when it fails: you miss a full street of value, and if the opponent has a draw you hand them a free card to beat you. It only pays off when the probability they bet is very high, which usually means a player who has just lost a pot, is visibly aggressive, or has been bluffing at checked pots. Against a nit who checks back the large majority of the time the expected loss is obvious. Make the opponent read first, then pick the line.

**Common mistake.** Checking a monster against a passive player hoping for a bet, then watching them check behind twice and show down a hand that would have called three streets.

**Numbers.** do not try to induce against a player who checks behind ~90% of the time

**Hooks.** _Checking the nuts is a trap. For you._ · _Before you slow-play, answer one question about your opponent._ · _The induce play fails more often than forums admit._

Review: [ ]

### Ace-high flops: check-raise average vs small bets, low vs big; low flops stay high
`c-cash-6max-gp23-ace-high-check-raise-by-size-016` · advanced · flop · srp · oop · consensus 0.50 · sources: rio · **draft**

**Claim.** As the caller on ace-low-low or ace-mid-low flops, check-raise at about an average rate against a small c-bet. When the bet is large, which usually happens on two-Broadway ace boards like A98-type textures, drop to a low check-raise frequency. On all-low flops keep a high check-raise frequency even against big bets, and on two-Broadway boards stay low even against a quarter pot.

**Why.** Bet size and texture interact. A small bet on a dry ace board is often a range bet, so there is plenty of weak stuff to attack and your sets, two pairs and backdoor draws can raise at a normal clip. A large bet on an ace board with two Broadways comes from a strong, polarized range that will not fold much, so raising mostly isolates you against the top of it. On low boards your range advantage is large enough that even a big bet should still face frequent raises. Two-Broadway boards without an ace are the raiser's territory regardless of size.

**Common mistake.** Using one check-raise frequency for "ace-high boards" without noticing that the bet size tells you which kind of ace-high board you are on.

**Hooks.** _Same ace-high flop, two bet sizes, two different plans._ · _Big bet on a low board? Raise anyway._ · _The bet size tells you how often to check-raise._

Review: [ ]

### Low and paired flops are the highest check-raise textures for the caller
`c-cash-6max-gp23-check-raise-low-boards-011` · advanced · flop · srp · oop · consensus 0.50 · sources: rio · **draft**

**Claim.** Facing a c-bet as the caller, the boards with the highest check-raise frequency are all-low and mid-low-low textures, plus paired and trips boards. The relative ranking of textures holds against both small and medium c-bets, but the absolute frequency drops as the bet gets bigger.

**Why.** Low boards favor the caller: your preflop defense is full of suited connectors and small pairs that make sets, two pairs and strong draws, while the raiser's high cards whiff. That equity edge is what justifies raising often. On paired boards the raiser bets small with almost everything, so a raise with trips, pairs and good draws attacks a range that is mostly air. One caveat: on the lowest boards you rarely face a quarter-pot bet, so the report for the medium size is the one that actually describes most of your check-raise decisions there.

**Common mistake.** Check-raising mostly on high-card boards where you hit top pair, which is where the raiser's range is strongest and the raise does least.

**Hooks.** _The flop where the caller should raise most. Not what you think._ · _852 rainbow: the raiser is the one in trouble._ · _Check-raise low boards, not high ones._

Review: [ ]

### Facing a 75%+ c-bet on a Broadway flop, drop check-raising entirely
`c-cash-6max-gp23-no-check-raise-broadway-big-bet-015` · advanced · flop · srp · oop · consensus 0.50 · sources: rio · **draft**

**Claim.** On Broadway-heavy flops the caller's check-raise frequency is already low, so when the c-bet is 75% pot or larger it is reasonable to simplify to never check-raising. The case gets stronger if the raiser barrels the turn at a high rate after betting the flop big.

**Why.** High-card boards give the raiser the nut advantage and a large bet polarizes an already strong range, leaving the caller few hands that gain from raising rather than calling. When the solver frequency is a few percent, removing it costs almost nothing and buys execution accuracy. Against an opponent who fires the turn a lot after a big flop bet, calling is even better: you let them keep bluffing into your strong hands instead of raising and folding out the bluffs you want to keep around.

**Common mistake.** Check-raising top pair on KQJ into a big bet "for protection", turning a comfortable call into a spot where only better hands continue.

**Numbers.** vs 75%+ pot c-bet on Broadway flops: check-raise ~0%

**Hooks.** _Never check-raise this flop. Yes, never._ · _Big bet on a Broadway board? Just call._ · _The simplest flop defense rule you will ever learn._

Review: [ ]

### Store check-raise frequencies as high, medium or low relative to a per-size baseline
`c-cash-6max-gp23-relative-frequencies-013` · advanced · flop · srp · oop · consensus 0.50 · sources: rio · **draft**

**Claim.** Instead of memorizing a check-raise percentage for every texture, learn one baseline per bet size and tag textures as high, medium or low relative to it. Against a small bet a baseline near 15% might make high about 25% and low about 8%; against an overbet with a baseline near 4%, high is perhaps 7-8% and low is 0-1%.

**Why.** Absolute numbers for every combination of texture and size are too many to recall in game, and they go stale as soon as the sizes in your pool change. A relative scale captures the part that actually transfers: which textures favor the caller and which do not. Pair that with a feel for how bet size compresses every frequency, and you can produce a sensible frequency on the fly in a spot you never studied. It is a model you understand rather than a table you recite.

**Common mistake.** Trying to memorize "check-raise 23% on this board, 11% on that one" and freezing when the bet size does not match the one in the sim.

**Numbers.** vs small c-bet: baseline ~15% check-raise, high ~25%, low ~8% · vs overbet: baseline ~4%, high ~7-8%, low ~0-1%

**Hooks.** _Stop memorizing check-raise frequencies. Learn one number._ · _High, medium, low: all you need for flop check-raises._ · _Overbet changes your check-raise frequency more than the board does._

Review: [ ]

### Most of your missing check-raises live in the spot facing a small c-bet
`c-cash-6max-gp31-check-raise-more-vs-small-cbet-005` · intermediate · flop · srp · bb · consensus 0.50 · sources: rio · **draft**

**Claim.** When you need to raise your flop check-raise frequency from the big blind, look at the node facing a roughly quarter-pot c-bet. That is where solvers raise most and where passive players leave the most on the table. Against a large c-bet, the gap is much smaller.

**Why.** A small c-bet is made with a wide, weak range and offers you a cheap raise that puts real pressure on the in-position player. Solvers respond with far more check-raises there than against a big bet, which is already polarized and expensive to attack. If your overall check-raise stat is low, the deficit is almost certainly concentrated against the small size, so that is where drilling pays off fastest.

**Common mistake.** Defending against a 25% bet mostly by calling, letting the bettor realize equity cheaply with the whole range.

**Numbers.** Drill focus: facing ~25% pot c-bet; low priority facing ~150% pot

**Hooks.** _They bet a quarter pot. You call. That's the leak._ · _Small c-bets are an invitation. Accept it._ · _Where are your missing check-raises hiding? One spot._

Review: [ ]

### Low check-raise boards are not zero check-raise boards
`c-cash-6max-gp31-double-broadway-low-not-zero-007` · intermediate · flop · srp · bb · consensus 0.50 · sources: rio · **draft**

**Claim.** Two-Broadway flops are among the lowest check-raise textures for the big blind, even against a small c-bet. Low still means a few percent, not never. If you currently raise zero there, add a handful of raises with your strongest hands and best draws.

**Why.** On boards with two high cards, the opener has the range and nut advantage, so the caller mostly plays defensively. But a strategy that never raises is too predictable and lets the bettor realize equity with weak holdings at no risk. A low single-digit raise frequency keeps the bettor honest while still respecting the texture. Knowing the baseline is low is useful; rounding it to zero is a leak.

**Common mistake.** Writing off entire board classes as "never raise" and giving the in-position player a free pass there.

**Numbers.** Coach's own check-raise on double-Broadway: often 0%, target roughly 5%

**Hooks.** _'Never check-raise high boards' is costing you money._ · _Low frequency is not zero frequency._ · _KQ4 flop. Villain bets small. Do you ever raise?_

Review: [ ]

### A small check-raise size shows up mainly on high paired and monotone flops
`c-cash-6max-gp31-small-raise-paired-monotone-006` · advanced · flop · srp · bb · consensus 0.50 · sources: rio · **draft**

**Claim.** If you add a small check-raise size to your flop strategy, use it on higher paired boards and monotone boards. On most other textures, stick to your standard raise size.

**Why.** On paired and monotone flops, both players' ranges contain many hands that are either very strong or almost hopeless, and equities move less from turn to river. A small raise lets you attack a small c-bet cheaply with a wide range without inflating the pot on a texture where your strong hands are already hard to get paid. On more dynamic boards, the larger raise does more work denying equity and charging draws.

**Common mistake.** Using one check-raise size everywhere, which gives up the cheap pressure option on static textures.

**Hooks.** _A tiny check-raise on monotone flops. Here's why it works._ · _Paired board, small bet, small raise._ · _Not every check-raise needs to be big._

Review: [ ]

### Check-raise bluff with the live backdoor suit, flat or fold without it
`c-cash-6max-gp34-check-raise-bluffs-need-suit-006` · advanced · flop · 3bet-pot · oop · consensus 0.50 · sources: rio · **draft**

**Claim.** When the 3-bettor checks and faces a flop bet, bluff check-raises should come from hands holding a backdoor flush draw plus some straight or overcard interaction. The same hand without the suit should call if it has showdown or draw equity, and fold if it does not.

**Why.** The intuitive logic of "too weak to call, so raise" is backwards. Raising builds a pot you want to continue in, so the raising hand should be the one that improves most often and blocks the opponent's strongest continuing combos on common runouts. A backdoor flush draw does both: it adds turn cards that let you barrel and it removes suited combos from the opponent's range. Solvers consistently raise the suited version and flat or fold the unsuited version of the same hand class. Weak backdoor gutshots without the suit are mostly folds, not raises.

**Common mistake.** Check-raising ace-high or king-high hands with no backdoor suit because they feel too weak to call, while flatting the same hands when they do have the suit.

**Hooks.** _Too weak to call, so you raise? That's backwards._ · _The one card that turns a fold into a check-raise._ · _Why your check-raise bluffs keep running into it._

Review: [ ]

### After range-checking a dry high flop, check-raise aggressively into the stab
`c-cash-6max-gp36-check-raise-the-float-on-dry-high-boards-011` · advanced · flop · 3bet-pot · oop · consensus 0.50 · sources: rio · **draft**

**Claim.** When the 3-bettor checks a jack-to-king-high dry flop, the in-position caller is supposed to bet about half the time and in practice often bets more. A high check-raise frequency, including value hands, attacks that line and gets more money in than c-betting would.

**Why.** The caller's natural stabs on these boards are hands with a small pair, a low connector or a wheel draw, plus broadway hands that connect with the king or queen. Those are easy bluffs to find, so real players stab at least as often as theory. Against a large check-raise the caller must fold medium and low pocket pairs that bet the flop and fold the overcards that lack a backdoor flush draw, and most players under-fold here. Value hands in the 3-bettor's range therefore collect extra bets and fewer folds by check-raising than by leading, which is a core reason to prefer the range check on this texture.

**Common mistake.** Checking the flop as the 3-bettor with a strong hand and then only calling the stab, giving up the raise that the texture is built for.

**Hooks.** _Let them stab, then raise. The dry-flop trap for 3-bettors._ · _Why your top pair wants to check-raise, not c-bet, here._ · _They bet half the time into your check. Punish it._

Review: [ ]

### On 774 the big blind check-raises draws that carry extra backdoor equity
`c-cash-6max-tc17-bb-check-raise-draw-selection-004` · advanced · flop · srp · bb · consensus 0.50 · sources: 2cc · **draft**

**Claim.** As the big blind on 774 two-tone, the draws that check-raise most are flush draws with straight backdoors (65s, 63s, 53s), straight draws like 65 and 63 of any suit, and offsuit king-through-nine high cards holding one card of the flush suit.

**Why.** A paired board offers few clean draws, so the solver wants extra equity before a hand becomes a check-raise. Lower flush draws raise more than higher ones because the 5x and 6x combos add wheel and six-high straight possibilities. Offsuit high cards with one suited card have a backdoor flush plus overcards that can improve, enough to make raising better than calling. Almost every unmade hand that raises either has a direct straight draw or holds a card of the flush suit.

**Numbers.** GTO check-raise with 65-type straight draws ~65-80%

**Hooks.** _Low flush draw beats high flush draw as a check-raise. Why?_ · _One spade in your hand changes the whole decision._ · _Which draws check-raise 774? Not the obvious ones._

Review: [ ]

### The big blind check-raises over 20% on 774, including low pairs for protection
`c-cash-6max-tc17-bb-check-raise-low-pairs-protection-003` · advanced · flop · srp · bb · consensus 0.50 · sources: 2cc · **draft**

**Claim.** Facing a button c-bet on 774 two-tone, theory has the big blind check-raise more than 20% of the time. Trips and full houses are the core, and second and third pairs plus hands like 33, 55 and 66 raise about 30% of the time even though they are not classic value hands.

**Why.** The big blind has more trips and boats than the button here, so a lot of hands want to raise for value, and that licence spreads to other parts of the range. Low pairs raise for protection. Nearly every turn card is an overcard, and many give the button a pair or a straight draw it can keep betting. If you call with pocket fives and the turn is a jack, a hand like J8 has outdrawn you and the button can barrel plenty of other cards too. Raising now folds out those six-out hands before they get there.

**Numbers.** GTO BB check-raise >20% on 774 · second/third pairs and 4x check-raise ~30%

**Hooks.** _Check-raising pocket fives on 774? The solver does._ · _Why bottom pair raises on a paired board._ · _Every turn card is an overcard. Raise before it comes._

Review: [ ]

### On K72 the big blind check-raises low ace-highs and calls with high ace-highs
`c-cash-6max-tc32-bb-check-raise-k72-draws-003` · advanced · flop · srp · bb · consensus 0.50 · sources: 2cc · **draft**

**Claim.** As the big blind on K72 two-tone, check-call A8 and better, but check-raise A6 through A3 often, especially flush draws and hands holding a flush-suit card plus wheel straight possibilities. Lower down, raise flush draws and backdoor flush draws that also carry a backdoor straight, such as JT, J9, QT and 54 or 43 with a suited card.

**Why.** Two overcards to the seven give A8 and up enough equity to call and improve. The lower aces lack that, so they need a wheel draw or a suited card to justify continuing, and a raise uses that equity more aggressively than a call would. The same filter runs through the queen-high and lower region. A backdoor flush alone is marginal, a backdoor flush plus a backdoor straight is a raise. Hands like Q8, J8 and T8 have no straight backdoor and are the ones that fold.

**Hooks.** _Ace-five raises, ace-nine calls. Same board._ · _The weaker ace is the better check-raise. Here is why._ · _Backdoor flush alone is a fold. Add a backdoor straight and raise._

Review: [ ]

### The big blind check-raises K72 about 13.5% with sets, top two and kicker-driven pairs
`c-cash-6max-tc32-bb-check-raise-k72-made-hands-002` · advanced · flop · srp · bb · consensus 0.50 · sources: 2cc · **draft**

**Claim.** Facing a button c-bet on K72 two-tone, theory has the big blind check-raise about 13.5% and call about 54%. Sets almost always raise, K7 raises more than K2, top pairs raise sometimes with higher kickers or a flush draw, second pairs raise with an ace kicker or a backdoor flush, third pairs raise mainly with low kickers, and underpairs never raise.

**Why.** With the raiser holding most of the kings, the big blind's raise is built from the few hands that beat top pair plus a layer of pairs that gain from folding out overcards. Second pair with an ace kicker has outs to the best hand when called. Third pair with a low kicker brings backdoor straight equity that higher kickers lack. Pocket pairs below the king have neither extra outs nor blockers, so they simply call.

**Numbers.** GTO BB check-raise ~13.5%, call ~54% on K72

**Hooks.** _Bottom pair with a three raises. Bottom pair with a nine calls._ · _Why pocket nines never check-raise K72._ · _The kicker decides your check-raise on K72._

Review: [ ]


## defending  (31)

### Call wider against a min-raise, even out of position, when the raiser is weak
`c-cash-6max-br1-defend-wider-vs-min-raise-012` · beginner · preflop · oop · consensus 0.50 · sources: br79 · **draft**

**Claim.** A minimum raise offers a great price, so defend noticeably more hands against it than against a normal-sized open, including out of position. Do this especially when the raiser is a recreational player, and keep folding true trash that flops poorly.

**Why.** Your preflop price is set by the raise size. A min-raise roughly halves what you must invest compared with a 3x open, and the hands you add are ones that can flop a strong pair, two pair or a draw against someone who plays badly after the flop. The usual reason to avoid out-of-position calls, being outplayed later, matters much less against a player who rarely applies pressure. Against a competent opener with a standard size, the same hands go back to the muck.

**Common mistake.** Folding hands like K7 or J8 to a min-raise from a fish on principle, or taking the great price to flat with a hand that cannot make anything.

**Hooks.** _A min-raise is an invitation. Accept it more often._ · _Half the price, twice the hands. Simple math._ · _Facing a min-raise from a fish? Fold less._

Review: [ ]

### Defend a bit lighter against a maniac because top pair wins their stack
`c-cash-6max-br2-peel-lighter-vs-maniacs-005` · beginner · preflop · ip · consensus 0.50 · sources: br79 · **draft**

**Claim.** Against a wild player who overbets and shoves with weak holdings, call preflop and on the flop with somewhat weaker hands than usual, such as Q8 or a middling pair. Any top pair you make is likely to be paid in full.

**Why.** The value of a preflop call is not just its showdown equity but what you win when you connect. Against a normal opponent a hand like Q8 makes top pair and wins a small pot. Against a maniac the same top pair collects a whole stack, because they keep firing with worse. That extra payout justifies entering more pots. The same logic says to avoid bloating the pot preflop with marginal hands: you want to see a flop cheaply and let them do the betting once you have something.

**Common mistake.** Playing your standard tight range against a maniac and letting other players at the table collect the stack.

**Hooks.** _Against a maniac, queen-eight becomes a call. Here is why._ · _Top pair wins a stack here. Pay to see flops._ · _Implied odds are not just for suited connectors._

Review: [ ]

### With middle pair facing aggression from an unknown, fold rather than hero-call
`c-cash-6max-br3-middle-pair-no-hero-call-007` · beginner · multi-street · srp · any · consensus 0.50 · sources: br79 · **draft**

**Claim.** When your middle pair faces a bet or raise from a player you have no information on, and a plain second pair or better beats you, fold. Hero-calling weak players is unnecessary because their stack will come to you later in a clearer spot.

**Why.** A hero call needs the opponent to be bluffing far more often than their play suggests. Against an unknown there is no evidence of that, and recreational players bet with a bizarre collection of real hands more often than with air. Being bluffed off a pot occasionally is cheap; paying off with a hand that loses to any legitimate holding is expensive. Your edge against this type comes from value, not from calling down.

**Common mistake.** Calling a river raise with middle pair because "he could be bluffing" and seeing a set.

**Hooks.** _Getting bluffed is cheap. Paying off is not._ · _Middle pair facing a raise. The answer is simpler than you think._ · _Hero calls at the micros are mostly just calls._

Review: [ ]

### Speculative hands against a fish are a call in position and a fold from the blinds
`c-cash-6max-br4-call-ip-fold-oop-vs-fish-015` · beginner · preflop · ip · consensus 0.50 · sources: br79 · **draft**

**Claim.** A hand like J-9 is worth calling a raise with when a weak player is in the pot and you have position, especially deep-stacked. The same hand facing the same raise from the small or big blind is a fold.

**Why.** The profit from a speculative hand comes from implied odds, and implied odds depend on acting last: you need to see what the opponent does before you decide how much to invest, and you need them to pay you when you hit. Out of position both are weaker, and against a raise you also face c-bets with no information. A weak opponent who overplays one pair and deep stacks on both sides make the in-position call clearly good and the out-of-position call still bad.

**Common mistake.** Defending the blinds with suited and connected junk "because the fish raised" and then being outplayed on every street.

**Hooks.** _Jack-nine is a call. Unless you are in the blinds._ · _Implied odds need position. Here is why._ · _Same hand, same raise, two different answers._

Review: [ ]

### Do not fold to a min-bet; the price is almost always right
`c-cash-6max-br5-never-fold-to-a-min-bet-014` · beginner · multi-street · srp · any · consensus 0.50 · sources: br79 · **draft**

**Claim.** Facing a bet of one big blind or a tiny fraction of the pot, call with nearly anything that has outs or showdown potential. The pot odds justify it almost every time, and the small bets of wide-range players carry little information. Fold later if the price goes up.

**Why.** A min-bet lays you enormous odds, so even a gutshot or bottom pair is a profitable call. Weak players use small bets both with monsters and with nothing, so the bet does not narrow their range much either. Folding gives up equity you were offered almost for free. The danger is only on later streets if the sizing jumps, and you can reassess then.

**Common mistake.** Folding a gutshot or weak pair to a one-blind bet because the hand feels too weak, ignoring the price on offer.

**Hooks.** _Never fold to a min-bet. Here is the math._ · _He bet one blind. Your hand does not matter yet._ · _The cheapest call in poker, and people still fold._

Review: [ ]

### Versus a relentless 3-bettor on your left, fold sevens OOP; fight back smarter or move
`c-cash-6max-br6-facing-a-relentless-3bettor-on-your-left-009` · beginner · preflop · 3bet-pot · oop · consensus 0.50 · sources: br79 · **draft**

**Claim.** When a player keeps 3-betting you and you are out of position, do not call with pocket sevens to make a stand. Either 4-bet, or call with hands like nines and tens that can continue on many more flops. If it keeps happening, change seats or tables. Keep your ego out of it.

**Why.** Sevens out of position in a 3-bet pot face two overcards and a c-bet most of the time, so the call is a slow bleed, not a counter-strategy. If you want to push back, pick a weapon that works: a 4-bet that denies them equity, or a flat with a hand that sees plenty of one-overcard flops. Repeated 3-bets are annoying but not expensive if you fold the junk; getting frustrated and taking a stand with a bad hand is what makes them expensive. Seat changes are free.

**Common mistake.** Calling or 4-betting light with a mediocre hand after the third 3-bet purely to show the opponent you will not be pushed around.

**Hooks.** _He 3-bet you four times. Do not take a stand with sevens._ · _The right way to fight back against a 3-bet machine._ · _Seat changes are free. Spite calls are not._

Review: [ ]

### Ace-king need not play a huge pot; fold top pair to a bet and a raise when barely invested
`c-cash-6max-br8-do-not-marry-ace-king-005` · beginner · flop · 3bet-pot · oop · consensus 0.50 · sources: br79 · **draft**

**Claim.** When you have only put a few blinds in with ace-king, for example by calling a 3-bet out of position rather than cold 4-betting an unknown, and the flop brings top pair but then a bet and a raise in front of you, fold. At micro stakes a flop raise into two players is a strong hand, and your preflop investment is small enough that folding costs almost nothing.

**Why.** Players get married to ace-king because it is the best unpaired hand, but once the flop comes it is just top pair, and against a bet and a raise top pair is rarely good. Cold 4-betting an unknown with ace-king turns the hand into a bluff that only gets action from better; calling keeps the pot small and lets you see the action before committing. When that action is strong, fold and move on. Your win rate depends on avoiding high-variance pots with one pair, not on winning every pot where you hold a big hand.

**Common mistake.** Treating ace-king as a hand that must get stacks in, 4-betting unknowns with it and then calling off top pair against a bet and a raise.

**Schools disagree.** Solver-based play 4-bets or stacks off with ace-king against most 3-bets at 100bb; the coach prefers flatting unknowns and folding top pair to heavy flop action, keeping variance low against a weak population.

**Hooks.** _Ace-king flopped top pair. We folded. Here is why._ · _Stop getting married to ace-king._ · _The flop raise at NL10 that should end your hand._

Review: [ ]

### When your range dwarfs his, do not fold any hand to a small bet
`c-cash-6max-cc03-never-fold-extreme-advantage-011` · intermediate · flop · srp · ip · consensus 0.50 · sources: cc · **draft**

**Claim.** When your range is massively stronger than your opponent's and he makes a small bet into you, fold nothing. Even your worst hands are entitled to a big share of the pot against a range that feeble. Fold frequency depends on favourability, not just on bet size.

**Why.** If your range were only aces and his only seven-deuce, you would never fold to a shove, and even a small frequency would be absurd; a horrible play does not become fine by doing it rarely. The same logic applies on boards like K-K-7 rainbow when the big blind leads 25% pot into the preflop raiser from early position: the raiser's range is so much stronger that every hand in it continues. Pot odds give the baseline fold frequency for symmetric ranges, but range inequality pushes it towards zero in your favour and towards over-folding when you are the one being smashed.

**Common mistake.** Mechanically folding the bottom of your range to a tiny lead because "I have to fold something", regardless of how weak his range is.

**Numbers.** vs a 25% pot donk on K-K-7 as the early-position raiser: fold 0%

**Hooks.** _Sometimes the correct fold frequency is exactly zero._ · _A horrible play done rarely is still a horrible play._ · _He donks into your monster range. Fold nothing._

Review: [ ]

### MDF overstates how much you should defend when your range is behind
`c-cash-6max-cc06-mdf-assumes-equal-ranges-014` · intermediate · flop · oop · consensus 0.50 · sources: cc · **draft**

**Claim.** Minimum defense frequency assumes both ranges are roughly equal. When you face a bet with a large range disadvantage, folding more than MDF suggests is the theoretically correct response, not a leak.

**Why.** MDF answers the question "how often must I continue so the bettor's pure bluffs break even". That is only the right target when making the bettor indifferent is achievable and desirable. Against a range that is much stronger than yours, the bettor is simply profitable - they are not indifferent, and trying to hold them to break-even means calling with hands that lose money. Solvers show the disadvantaged side folding well above the MDF-implied rate on flops where the raiser's range dominates. The flip side is the bettor's edge - their bluffs and thin value bets work because the correct response includes a lot of folding.

**Common mistake.** Forcing yourself to call "to meet MDF" as the big blind on a flop where the raiser's range is far ahead, bleeding chips with hands that should fold.

**Schools disagree.** Common teaching: 'always defend at least MDF or you are exploitable'. This lesson says MDF is a poor guide whenever ranges are asymmetric, which is most of the time.

**Hooks.** _MDF is wrong most of the time. Here's why._ · _Folding more than MDF can be the theory play._ · _Stop defending to make him break even. He's ahead._

Review: [ ]

### Write a one-line folding threshold per flop category to anchor your adjustments
`c-cash-6max-gp23-folding-threshold-baseline-014` · intermediate · flop · srp · oop · consensus 0.50 · sources: rio · **draft**

**Claim.** For each flop category and the common bet size you face, describe in a few words the weakest hand class that still continues. This is not a minimum-defense target and not something to recite; it is a reference line you need before you can float lighter or fold more against a specific opponent.

**Why.** Minimum defense frequency is a poor guide on early streets because equity realization and future-street play matter more than a single ratio. A hand-class line such as "double overcard with a backdoor" is something you can actually recall at the table and compare your hand against. More importantly, exploitative adjustments only make sense relative to a baseline. If you want to punish an over-folding opponent by floating, you need to know where the line was to begin with. Over time, through play and drilling, the line becomes intuition and the written note is only a reminder.

**Common mistake.** Trying to defend to an MDF percentage on the flop, or having no idea whether a given float is a slight stretch or a huge one.

**Hooks.** _MDF on the flop is misleading. Use this instead._ · _One sentence per board. That is your whole defense plan._ · _You cannot adjust from a line you never drew._

Review: [ ]

### Fold very little to a quarter-pot c-bet, except on high monotone and high paired flops
`c-cash-6max-gp23-sticky-vs-quarter-pot-012` · intermediate · flop · srp · oop · consensus 0.50 · sources: rio · **draft**

**Claim.** Heads-up as the caller facing a 25% pot c-bet, your fold frequency should stay very low on almost every texture. The few boards where folding climbs toward ~28% are high-card monotone and high paired boards, where a chunk of your range flopped nothing at all.

**Why.** A quarter-pot bet offers 5-to-1, so almost any hand with a pair, a draw or a backdoor plus an overcard has the equity to continue. Folding more than the bare minimum hands the raiser a profitable bet with any two cards. The exceptions are structural: on a high monotone board, hands without the suit are drawing very thin, and on a king- or ace-high paired board most of your unpaired low cards have no realistic way to win. There, the folds are forced by equity, not by choice, and even then the fold rate stays under a third.

**Common mistake.** Folding bottom pair, ace-high or any hand that "missed" to a small bet, which lets the raiser print money with a range bet.

**Numbers.** max fold frequency vs 25% pot c-bet ~28%, only on high monotone and high paired flops

**Hooks.** _You fold too much to small bets. Here is the number._ · _5-to-1 odds and you are folding ace-high?_ · _The two flop types where folding to a quarter pot is right._

Review: [ ]

### Study your flop defense against the sizes your opponents actually use
`c-cash-6max-gp23-study-sizes-you-face-010` · intermediate · flop · srp · oop · consensus 0.50 · sources: rio · **draft**

**Claim.** When building a facing-c-bet plan, assume the bet sizes your pool really uses on each texture, not the sizes a solver prefers. Each bet size needs its own response, so there is no value in preparing a precise answer to a size you never see.

**Why.** The correct check-raise frequency and folding threshold change sharply with bet size, so a defense built against a quarter-pot bet is wrong against a two-thirds bet. Aggregate reports can only be run against one size at a time, which forces you to pick the sizes that matter. If your pool bets 2/3 pot on every board, that is the report to study, even if theory says they should be betting a quarter. The same logic applies when the pool's sizing differs from your own c-bet plan: your defense sheet should mirror what you face, not what you would do.

**Common mistake.** Memorizing solver responses to 33% and 150% bets and then facing a 55% pot bet every hand with no plan.

**Hooks.** _You are studying a bet size nobody uses on you._ · _Study the 2/3 pot c-bet. That is what you face._ · _Why your solver defense fails at NL25._

Review: [ ]

### On ace-high flops facing a small bet, let the kicker decide which king-highs continue
`c-cash-6max-gp30-king-high-kicker-ace-board-006` · intermediate · flop · srp · oop · consensus 0.50 · sources: rio · **draft**

**Claim.** Against a quarter-pot c-bet on an ace-high board, not every king-high hand has to call. Use the second card as the differentiator: king-high with a second overcard to the board continues, while king-high with a weak kicker and no backdoor equity is in the folding region.

**Why.** On an ace-high flop your king-high is rarely the best hand at showdown, so its value comes from improving to a pair that beats the raiser's bluffs and medium hands. A second overcard doubles the outs to a pair that is good, and a backdoor straight or flush draw adds more. Without those, king-rag is close to a pure bluff-catcher that cannot improve, and even at a cheap price the solver folds a share of them. This is a deliberate hand-quality split, not a randomizer.

**Common mistake.** Treating "king-high" as a single hand class and either calling all of it or folding all of it to a small bet on an ace board.

**Example.** positions: BTN vs BB | hero: Kh4c | board: Ad8s3c | action: BTN opens, BB calls. BB checks, BTN bets 25%. | decision: Call or fold with king-high, no backdoors? | answer: Fold is fine. Swap the four for a ten or a nine and the second overcard makes it a continue.

**Hooks.** _King-high on an ace board: the kicker is the whole decision._ · _Which king-high calls a small bet? Not all of them._ · _One card decides whether K-high continues here._

Review: [ ]

### Monotone flop vs small c-bet: any suit card continues; pairs and straight draws never fold
`c-cash-6max-gp30-monotone-any-suit-card-calls-009` · intermediate · flop · srp · oop · consensus 0.50 · sources: rio · **draft**

**Claim.** Facing a small c-bet on a monotone board, a single card of the board's suit is enough to continue with everything. Without a suit card, pairs and real straight draws still continue across the board; check-raises without a suit card come from pairs and straight draws, and light floats come from quality high cards with a backdoor straight draw.

**Why.** A small bet on a monotone board is often a range bet, because the raiser cannot credibly size up when so many of the caller's hands have a flush draw. Any flush-suit card gives you a draw to a strong hand with a cheap price, so folding those is giving up equity. Without the suit, you lean on hands that can win at showdown or make a straight, which is why pairs and straight draws hold up as continues and as the natural raising hands. Against players who bet small with their whole range on these boards, you can press harder with raises and floats than the baseline suggests.

**Common mistake.** Folding a weak pair or a straight draw to a small bet on a monotone board out of fear of the flush, or folding a hand with a lone high suit card.

**Example.** positions: BTN vs BB | hero: Qc7h | board: Th8h3h | action: BTN opens, BB calls. BB checks, BTN bets 25%. | decision: Fold, call or raise with one heart and no pair? | answer: Call. A single suit card is enough to continue against a small bet on a monotone flop.

**Hooks.** _One card of the suit is all you need to call._ · _Monotone flop, small bet: the rule that covers 90% of spots._ · _Stop folding pairs on monotone boards._

Review: [ ]

### On a high monotone flop without a suit card, ace-high needs a real kicker to continue
`c-cash-6max-gp30-monotone-high-board-ace-high-010` · advanced · flop · srp · oop · consensus 0.50 · sources: rio · **draft**

**Claim.** When the monotone board is high, such as queen-jack-x, and you hold no card of the suit, speculative ace-high stops continuing against a small bet. Only ace-high with a strong kicker (around A9 or A8 and up) stays in, alongside pairs, front-door straight draws and quality overcards; two undercards are out.

**Why.** On a low monotone board your ace-high is two overcards and often the best unpaired hand, so it can float. When the board is queen-jack high, the ace is a single overcard, the raiser's range is full of Broadway pairs, and your unpaired hand needs interaction with the board or a draw to have enough equity. Removing straight draws from the board has a similar effect in the other direction: with fewer draws available, the caller floats a bit more with high cards, and double overcards with a backdoor get in most of the time.

**Common mistake.** Calling any ace-high on any monotone flop because "ace-high is strong heads-up", regardless of how high the board is.

**Hooks.** _Ace-high on QJ7 monotone with no suit? Usually a fold._ · _The monotone board where ace-high stops being a hand._ · _High board, no suit card: here is what still calls._

Review: [ ]

### The folding line moves enormously between a quarter-pot bet and an overbet
`c-cash-6max-gp30-overbet-vs-small-threshold-004` · intermediate · flop · srp · oop · consensus 0.50 · sources: rio · **draft**

**Claim.** Against a 25% pot c-bet on a two-tone Broadway flop, nearly any two cards of the flush suit continue, even nine-high, and single-suit-card hands fold only with two undercards. Against a 150% overbet on the same board, nut backdoor flush draws, ace-high with a suit card, gutshots and some bottom pairs fold; the line sits around strong bottom pair or weak middle pair.

**Why.** Price drives the threshold. At 5-to-1 nearly every hand with some equity and a path to improve is a profitable continue, so folding is reserved for pure air. At an overbet you are offered worse than 2-to-1 against a polarized range, and a hand needs real showdown value or a strong draw to continue. The practical lesson is that "I have a backdoor" is a reason to call a small bet and no reason at all to call a big one. If your pool uses both sizes, you need two separate thresholds per texture, not one.

**Common mistake.** Calling an overbet with a gutshot or a backdoor flush draw because "it worked against the small bet", or folding bottom pair to a quarter-pot bet.

**Numbers.** vs 25% pot: any two of the flush suit continue, down to nine-high · vs 150% pot: fold nut backdoor flush, ace-high with one suit card, gutshots; continue from strong bottom pair up

**Example.** positions: CO vs BB | hero: Td9d | board: KdJs5c | action: CO opens, BB calls. BB checks, CO bets 150% pot. | decision: Call with a gutshot plus backdoor flush draw? | answer: Fold. Against the overbet this hand class is below the line. Against a quarter-pot bet it would be an easy continue.

**Hooks.** _Backdoor draws call small bets. They fold to overbets._ · _Same flop, same hand, opposite answer. The bet size decides._ · _Facing an overbet? Even bottom pair is close._

Review: [ ]

### Facing a flop check-raise, defending enough matters far more than finding 3-bets
`c-cash-6max-gp31-defend-vs-check-raise-not-3bet-010` · intermediate · flop · srp · ip · consensus 0.50 · sources: rio · **draft**

**Claim.** After c-betting and getting check-raised in a single-raised pot, focus on continuing with enough draws, marginal floats and weak pairs. Flop 3-bets are a minor part of the strategy and can mostly be ignored while you fix overfolding.

**Why.** The check-raiser's range is wide and includes many bluffs, so the in-position player must call with hands that feel uncomfortable. Players coming from tighter formats or full-ring games tend to carry over a folding reflex and give up hands that are clear continues against a wide raising range. Re-raising the flop adds little EV in comparison and is easy to overdo. Spend the training time on the call-or-fold line and only note when a 3-bet would have been clearly better.

**Common mistake.** Folding weak pairs and backdoor draws to a flop check-raise because they "can't be good", which lets the raiser bluff profitably.

**Hooks.** _You c-bet, they raise, you fold. That's the leak._ · _Weak pair facing a check-raise? Calling is often right._ · _Forget flop 3-bets. Fix your folds first._

Review: [ ]

### Fixing a low check-raise frequency usually fixes an overfold at the same time
`c-cash-6max-gp31-overfold-overraise-linked-008` · intermediate · flop · srp · bb · consensus 0.50 · sources: rio · **draft**

**Claim.** A big blind who raises too little against small c-bets is usually folding too much in the same spot. Drilling the raise decision tends to repair both stats because the hands you learn to raise are the ones you were folding.

**Why.** Against a quarter-pot bet, the price is so good that very little of your range should fold. Players who are too passive feel they cannot call with weak draws and backdoors, and they do not raise them either, so those hands become folds. Once you start raising the marginal candidates, the folds that remain are the truly hopeless hands and your fold frequency drops toward the target.

**Common mistake.** Working on fold-to-c-bet and check-raise as two separate leaks when they are one habit.

**Numbers.** Coach's fold vs small c-bet was about 5 percentage points too high

**Hooks.** _Two leaks, one fix._ · _Fold too much vs small bets? Start raising._ · _The hands you fold should have been raises._

Review: [ ]

### A backdoor flush draw in the wrong suit does not make a hand a float
`c-cash-6max-gp31-wrong-suit-is-not-a-float-009` · intermediate · flop · srp · any · consensus 0.50 · sources: rio · **draft**

**Claim.** When you consider peeling a flop bet or check-raise with a weak hand, your suit needs to match the board. Two suited cards in a suit that is not on the flop add almost nothing and do not turn a fold into a call.

**Why.** Floats and light continues are justified by the ways a hand can improve on the turn. A backdoor flush draw that shares a suit with the board gives you extra turn cards to continue on and bluff with. If your suit is absent from the flop, you need two perfect cards just to get to a draw, so the hand plays essentially as offsuit. In drills, this was the most common way the coach found himself calling too light.

**Common mistake.** Treating any suited hand as a candidate to continue, regardless of which suits are on the board.

**Hooks.** _Suited doesn't mean you can float._ · _Your backdoor draw needs the right suit._ · _One suit check that saves you a bad call._

Review: [ ]

### Facing a river check-raise after a checked-down hand, you hold only bluff-catchers
`c-cash-6max-gp32-river-raise-all-bluffcatchers-009` · advanced · river · srp · ip · consensus 0.50 · sources: rio · **draft**

**Claim.** When you bet a checked-down river in position and get raised, there is no hand in your range that is an easy call. Everything is a bluff-catcher at mixed frequency, so use a randomizer and accept folding a decent hand some of the time.

**Why.** Your river betting range in this line consists of medium-strength value and bluffs; the nutted hands were bet on earlier streets. The opponent's raise represents the few strong hands that checked twice plus bluffs. The solver's response is a set of indifferent calls spread across your value hands, with no hand calling always. Expecting a "clear call" here leads to either hero-calling too much or folding everything. Pick a frequency and stick to it.

**Common mistake.** Snap-calling the river raise with any top pair because it felt strong when you bet it.

**Numbers.** Solver call frequencies seen in the drill ranged from ~12% to ~36% depending on the hand

**Hooks.** _You bet the river and get raised. Nothing is a clear call._ · _Every hand is a bluff-catcher here. Flip a coin._ · _Why folding top pair to a river raise is fine._

Review: [ ]

### Aggregate benchmarks for the 3-bettor who checks and faces a flop bet
`c-cash-6max-gp34-benchmarks-vs-float-004` · advanced · flop · 3bet-pot · oop · consensus 0.50 · sources: rio · **draft**

**Claim.** Across all flop textures, the out-of-position 3-bettor who checks and faces an in-position bet check-raises roughly 11% of the time and folds roughly 35%. Use these as rough anchors for your database, not as targets to hit exactly.

**Why.** Aggregate solver reports blend every texture and assume equilibrium bet sizes from the opponent. If your own plan converts some mixed-check textures into pure checks, your check-raise frequency should sit above the aggregate, because value hands that would have bet now check-raise instead. If your fold number is lower than the benchmark, the cause may be that opponents bet small more often than equilibrium suggests, and small bets should be folded to less. A deviation from the benchmark is a prompt to investigate, not proof of a leak.

**Common mistake.** Seeing a stat in red against the solver benchmark and immediately forcing the number back toward it without asking why it differs.

**Numbers.** Aggregate check-raise vs flop float as OOP 3-bettor: ~11% · Aggregate fold vs flop float as OOP 3-bettor: ~35%

**Hooks.** _Your stat is above the solver's. That might be correct._ · _One fold number that tells you how sticky you really are._ · _Check-raising more than theory can be by design._

Review: [ ]

### On a rainbow one-straight low board, weak aces and small pairs fold to half pot
`c-cash-6max-gp34-one-straight-rainbow-fold-weak-aces-009` · advanced · flop · 3bet-pot · oop · consensus 0.50 · sources: rio · **draft**

**Claim.** When the 3-bettor checks a rainbow low board with a single straight and faces a half-pot bet, ace-five suited with no backdoor flush draw is a clear fold, and even a small pocket pair below the board folds. Continue with straight draws and clean broadway overcards.

**Why.** Without a flush draw possible, the only improving cards for a weak ace are the three remaining aces, and the board's straight already dominates its low-card outs. Against half pot that is not enough, and the sim shows calling loses around one big blind. A small pair below the board faces the same problem: it has no overcard and few outs. The hands worth defending are the ones that can make the straight or make top pair with a strong kicker.

**Common mistake.** Peeling any ace-high or any pocket pair against a stab because the bet "isn't that big".

**Numbers.** A5s no backdoor flush vs half pot on rainbow one-straight low board: fold, calling loses ~1bb

**Example.** positions: BB vs BTN | hero: Ad5d | board: 9c7h3s | action: BTN opens, BB 3-bets, BTN calls. Flop: BB checks, BTN bets 50% pot. | decision: Call or fold? | answer: Fold. No flush draw possible, the straight cards are not yours, and the call loses about a big blind.

**Hooks.** _Pocket fives on a low board. Facing half pot. Fold._ · _This ace-high call costs a full big blind every time._ · _Rainbow boards punish weak floats harder than you think._

Review: [ ]

### Facing a small stab after checking, rank weak hands by how live their outs are
`c-cash-6max-gp34-rank-floats-by-live-outs-007` · advanced · flop · 3bet-pot · oop · consensus 0.50 · sources: rio · **draft**

**Claim.** Among hands with no pair, continue with the ones whose draws can actually arrive and whose overcards are clean. A backdoor straight draw that uses cards already on the board, or that cannot turn an open-ender, is close to dead and should fold even to a small bet.

**Why.** Low-equity floats survive on the turn cards that improve them. One clean overcard plus some straight interaction is a better hand than a junky backdoor gutshot because it has more ways to make a pair that is good and more turns to barrel. On a king-queen-high board, interaction with the low card can matter more than interaction with the top cards, but a two-gapper that cannot pick up an open-ended draw still folds. On a paired board or a board with no overcard for you, having an overcard plus a combo backdoor is what keeps a seven-high suited connector in the hand.

**Common mistake.** Calling any suited connector with three-to-a-straight because it looks connected, without checking whether the straight cards are already dominated by the board.

**Hooks.** _Three to a straight can be a dead hand. Here's when._ · _Not all backdoor draws deserve a call._ · _The float you make every day that loses a blind._

Review: [ ]

### Your continue threshold vs a float moves a lot between 30% and 60% pot
`c-cash-6max-gp34-sizing-changes-float-defense-008` · advanced · flop · 3bet-pot · oop · consensus 0.50 · sources: rio · **draft**

**Claim.** On a high-low-low two-tone board where the 3-bettor checks, ace-jack high continues against a 30% pot stab almost regardless of suits, but against a 60-65% pot stab it continues only with the backdoor flush draw and folds without it. Half pot sits in between and is roughly a fold without the suit.

**Why.** A small bet offers a cheap price, so marginal overcards with no draw still have enough equity and playability to peel. A bet of two-thirds pot roughly doubles what you risk and demands more raw equity, and the backdoor suit is what pushes an ace-high hand over the line. If you run a high-checking plan as the 3-bettor, you will face more stabs than most players, so you need the thresholds for the sizes your opponents actually use, not only the size you prepared for your own bets.

**Common mistake.** Learning the defence against one small stab size and applying the same calling range when the opponent bets half pot or more.

**Numbers.** AJ no backdoor suit on T54 two-tone: pure continue vs ~30% pot, pure fold vs ~60-65% pot · AJ with backdoor suit: pure continue vs both sizes

**Example.** positions: BB vs BTN | hero: AhJc | board: Td5s4s | action: BTN opens, BB 3-bets, BTN calls. Flop: BB checks, BTN bets. | decision: Call or fold vs 30% pot; vs 65% pot? | answer: Vs 30% pot call; vs 65% pot fold without a spade, call with the spade backdoor.

**Hooks.** _Ace-jack high, flop stab. Half pot changes the answer._ · _The size you studied is not the size they use._ · _One suit decides whether this ace-high calls or folds._

Review: [ ]

### Facing a big c-bet full of overpairs, call with your strong hands instead of jamming
`c-cash-6max-gp35-call-dont-jam-coolers-vs-big-bet-013` · advanced · flop · 3bet-pot · ip · consensus 0.50 · sources: rio · **draft**

**Claim.** On low flops in 3-bet pots where the opponent's large c-bet is heavy in overpairs, resist the urge to raise all-in with your sets and two pairs. Solvers mostly call there and build the raising range from hands lower in the range.

**Why.** When the big bet is dominated by overpairs, those hands are not folding to a raise and will often get it in anyway on later streets. Jamming your strongest hands only speeds up money that was coming, while giving away that your raising range is nutted. Calling keeps the opponent betting the turn with the whole overpair range and keeps your raises, when you do make them, built from hands that benefit from folds. Against a population that overcommits with overpairs, the temptation to jam is strong, but the extra value is smaller than it looks.

**Common mistake.** Shoving a set over a big c-bet because "they have an overpair and will call", when calling extracts the same money and hides your range.

**Hooks.** _Flopped a set vs a big bet? Don't shove yet._ · _Jamming coolers is slower money than you think._ · _Why solvers call with sets in 3-bet pots._

Review: [ ]

### IP vs a 3-bet pot c-bet: raise about 7%, mostly on paired and low flops
`c-cash-6max-gp35-raise-vs-cbet-7pct-paired-low-001` · intermediate · flop · 3bet-pot · ip · consensus 0.50 · sources: rio · **draft**

**Claim.** After calling a 3-bet in position and facing a flop c-bet, your total raising frequency should be low, around 7%. The raises concentrate on paired boards and boards with low cards; on two-Broadway boards you almost never raise.

**Why.** The 3-bettor's range is strong and the pot is already large, so most of your defence is calling. Raises make sense where the out-of-position player c-bets small with a wide range, which happens on paired and low textures where their high cards missed. On high-card boards they bet large with a range that connects, and a raise mostly runs into overpairs and top pair. Knowing the overall number stops you from either never raising or inventing raises on the wrong boards.

**Common mistake.** Raising top pair on a king-high flop in a 3-bet pot "for protection", into a range full of overpairs and better kings.

**Numbers.** Overall raise vs flop c-bet IP in 3-bet pots: ~7%

**Hooks.** _One number for raising c-bets in 3-bet pots: 7%._ · _Stop raising high flops in 3-bet pots._ · _Where do solver raises live in 3-bet pots? Two textures._

Review: [ ]

### Underpair bets into a check, gets raised: fold it; pairs of the board continue
`c-cash-6max-gp35-underpair-bets-are-bluffs-017` · intermediate · flop · 3bet-pot · ip · consensus 0.50 · sources: rio · **draft**

**Claim.** When you bet a small pocket pair below the board into the 3-bettor's check and get raised, fold. A pair that matches one of the board cards, by contrast, is a clear continue against the same raise.

**Why.** Betting a pocket pair that is under the board is essentially a bluff with a little showdown value; against a check-raise its equity is poor and it is often drawing to two outs. A pair of the board card has more outs to improve, blocks the opponent's value and holds up against bluffs. Weak hands that bet for thin reasons should be ready to let go when the opponent pushes back, rather than calling because they were "already in the pot".

**Common mistake.** Calling a check-raise with pocket fives on a 9-7-6 board because the hand was good enough to bet.

**Hooks.** _You bet pocket fives and got raised. Let it go._ · _Underpair vs check-raise: it was a bluff, fold it._ · _Which pairs continue against a flop raise? Not the low ones._

Review: [ ]

### Call wider versus a 774 check-raise, but not as wide as the solver
`c-cash-6max-tc18-call-wider-but-not-everything-007` · advanced · flop · srp · btn · consensus 0.50 · sources: 2cc · **draft**

**Claim.** Against a big blind whose check-raising range is weaker than theory, continue with more hands, meaning good straight draws, backdoor flush draws and anything better. The max-exploit output folds under 3% and calls hands like J5 with no draw, which is not practical.

**Why.** The solver calls almost everything because the node-locked opponent keeps playing later streets as if their range were the theoretical one, and the solver knows every resulting error. A human cannot cash in on tiny later-street mistakes with jack-five. What you can count on is that a weaker raising range lets your medium hands and backdoor draws realise more equity, so extending calls to backdoor flush draws and good straight draws is a sound widening. Only the lowest ace, king and queen high cards with no suit interaction fold.

**Common mistake.** Copying the max exploit's near-zero fold rate and floating pure air against a raiser who may well adjust.

**Numbers.** max exploit folds <3% vs the check-raise

**Hooks.** _The solver calls jack-five here. You should not._ · _Wider calls, yes. Every hand, no._ · _Backdoor flush draw facing a check-raise? Keep going._

Review: [ ]

### Facing a check-raise on 774, theory 3-bets about 4% and calls about 57%
`c-cash-6max-tc18-gto-vs-check-raise-774-001` · advanced · flop · srp · btn · consensus 0.50 · sources: 2cc · **draft**

**Claim.** When the big blind check-raises your button c-bet on 774 two-tone, the solver re-raises only about 4% and calls around 57%. Re-raises come from A7, K7, some Q7, a few 4x as blockers, and ace-king plus lower high cards as the bluff share.

**Why.** The big blind has more trips and full houses than you on this board, so most of your made hands do better calling and keeping their weaker raises in the pot. The hands that re-raise are either the best trips, which still want a bigger pot, or hands whose cards block the nut region. High cards with no showdown value are the natural bluffs; they have little to lose and fold out the part of the raising range that is only backdoor equity.

**Numbers.** GTO vs check-raise on 774: 3-bet ~4%, call ~57%

**Hooks.** _Check-raised on 774 with trips? The solver mostly calls._ · _Why 3-betting is rare on paired low boards._ · _Four percent. That is how often theory re-raises here._

Review: [ ]

### Lower overpairs 3-bet for protection on 774, aces prefer to call
`c-cash-6max-tc18-overpairs-3bet-protection-003` · intermediate · flop · srp · btn · consensus 0.50 · sources: 2cc · **draft**

**Claim.** Against a check-raise on 774 from a draw-heavy big blind, re-raise some pocket eights, nines and tens but mostly call with pocket aces.

**Why.** A check-raising range full of overcards and draws will hit many turns against a medium overpair. Re-raising folds out king-high and queen-high hands that would otherwise outdraw you, so eights through tens buy protection. Pocket aces do not need it. Almost nothing in the raising range is an overcard, and letting the big blind keep their bluffs and draws leads to more value on later streets.

**Common mistake.** Playing all overpairs the same way, either always raising or always calling, regardless of how many overcards can beat them.

**Hooks.** _Pocket tens raise, pocket aces call. Same flop._ · _Protection is a reason to 3-bet. Not with aces._ · _Which overpair re-raises a 774 check-raise?_

Review: [ ]

### Facing a check-raise on K72, theory almost never 3-bets and calls about 57%
`c-cash-6max-tc33-gto-vs-check-raise-k72-001` · advanced · flop · srp · btn · consensus 0.50 · sources: 2cc · **draft**

**Claim.** When the big blind check-raises your K72 c-bet, the solver re-raises under 1%, so in practice you can simply never 3-bet. It calls around 57%, meaning every third pair and better, most ace-highs with a backdoor flush draw, nearly all suited backdoor flush draws, and offsuit broadway combos like JT, T9 and 98 that hold a backdoor flush.

**Why.** The raiser's range on K72 is tight, so bluff 3-bets have little to fold out and value 3-bets have few worse hands to get paid by. A re-raising range under 1% is not worth the effort of balancing. Calling is the workhorse. Any pair is ahead of enough of the raise, and backdoor flush plus backdoor straight equity is enough to continue once, because the raiser has to keep betting into a range that still holds many kings.

**Numbers.** GTO vs check-raise on K72: 3-bet <1%, call ~57%

**Hooks.** _Check-raised on K72? Theory says never re-raise._ · _A one percent 3-bet range is not worth having._ · _Backdoor flush plus backdoor straight equals a call here._

Review: [ ]


## exploits  (33)

### Against players who do not fold, stop bluffing and bet made hands
`c-cash-6max-br1-dont-bluff-stations-004` · beginner · multi-street · any · consensus 0.50 · sources: br79 · **draft**

**Claim.** The simplest profitable plan against a recreational player is to make a decent hand and bet it. Do not build a habit of trying to bluff them off pots; the one thing they reliably refuse to do is fold.

**Why.** A bluff only earns money when the opponent folds a hand that beats you. A player who calls with any pair, any draw and sometimes ace-high removes that fold equity almost entirely, so every chip you bluff is mostly donated. The same stickiness makes them the perfect value target: they pay off top pair, second pair and even weaker holdings. Redirect the aggression from bluffs to value bets and your variance drops while your win rate rises.

**Common mistake.** Firing a second and third barrel at a calling station because the board looks scary, then being shown bottom pair.

**Hooks.** _Bluffing a calling station is just a donation with extra steps._ · _Most micro players bluff the one opponent who never folds._ · _You do not need to bluff. You already have the best hand._

Review: [ ]

### Pot control is cheap against passive players because they rarely punish it
`c-cash-6max-br1-passive-fish-pot-control-008` · beginner · multi-street · ip · consensus 0.50 · sources: br79 · **draft**

**Claim.** With a medium-strength hand against a passive recreational player, checking a street costs little. They seldom respond with a large bet that puts you in a hard spot; when they do bet, the size is often small or odd and gives you a comfortable call.

**Why.** The usual argument against pot control is that checking hands the initiative to the opponent, who can then bluff you off a decent hand. That argument depends on the opponent being capable of a well-sized bluff. Passive players mostly check behind or bet amounts that give you direct odds. So you get to see cheap turns and rivers with hands like second pair, avoid stacking off when you are behind and still collect a bet later when you are ahead.

**Common mistake.** Betting a marginal hand "for protection" against a passive player, getting raised and having to fold a hand that would have won at showdown.

**Hooks.** _Checking here makes you more money than betting. Here is why._ · _Passive players let you pot-control for free. Use it._ · _The cheapest showdown in poker is against a station._

Review: [ ]

### One wild play is enough to assume the next one is coming
`c-cash-6max-br2-dumb-once-dumb-again-004` · beginner · multi-street · any · consensus 0.50 · sources: br79 · **draft**

**Claim.** When an opponent shows one absurd play, such as getting all-in with jack-six on nothing, assume they will do it again and loosen your stack-off range against them right away rather than waiting for a second confirmation.

**Why.** Players who make a wild play once are rarely doing it as a one-off balanced bluff; it is how they play. Waiting for more evidence means passing up the exact spot their stack is offered to you, and at these stakes they often bust or leave quickly. The cost of being wrong once is one stack; the cost of being too cautious is missing the most profitable opponent you will see all session. Paired with a small or odd buy-in, the read is nearly certain.

**Common mistake.** Folding a decent hand to a known gambler's shove because "he might have it this time".

**Hooks.** _Did something dumb once? He will do it again._ · _You only need one hand to read a gambler._ · _Waiting for confirmation is how you miss the easiest stack._

Review: [ ]

### Never show your cards unless there is a showdown
`c-cash-6max-br3-never-show-cards-006` · beginner · any · consensus 0.50 · sources: br79 · **draft**

**Claim.** Do not voluntarily show a hand after the pot is won, whether it was a bluff or a monster. Every shown card is free information for everyone at the table, and you gain nothing from giving it away.

**Why.** Showing a hand feels harmless, but it tells observant opponents how you size with strong hands, what you fold, what you call with and how you bluff. Those same opponents will use that against you in later pots while you receive nothing in return. The reverse is a gift: when a recreational player shows a fold, note it and adjust. Keep your own information private and collect theirs.

**Common mistake.** Showing a big fold to look disciplined or a bluff to look tricky, then wondering why a regular plays differently against you.

**Hooks.** _Showing your cards is paying for nothing._ · _Free information only flows one way. Make sure it is toward you._ · _The reg thanks you every time you show._

Review: [ ]

### Against a frequent 3-bettor on your left, steal tighter and 4-bet wider for value
`c-cash-6max-br4-adjust-vs-frequent-3bettor-013` · beginner · preflop · btn · consensus 0.50 · sources: br79 · **draft**

**Claim.** When the player behind you re-raises often, drop weak steals like K4 and widen your 4-bet value range to include hands such as A-Q, tens and jacks. Hold off on firm conclusions until the pattern is clear, since anyone can be dealt good hands for an orbit. Better still, move seats so that player is on your right.

**Why.** A frequent 3-bettor makes marginal opens unprofitable because they rarely get to see a flop, and makes medium-strong hands more valuable because the 3-bet range is wide enough that they are ahead of it. Both adjustments follow directly. The caution about sample size matters because over-adjusting to a player who simply ran hot costs money in the other direction. Aggressive players are a nuisance on your left and an asset on your right, where their raises come before your decision.

**Common mistake.** Deciding a player is a maniac after two 3-bets, or continuing to open K4 into them orbit after orbit.

**Hooks.** _He 3-bets everything. Here is the two-part fix._ · _Ace-queen becomes a 4-bet against this player._ · _An aggressive player on your left is a seat problem._

Review: [ ]

### Pass up thin edges against a weak player; their stack is coming anyway
`c-cash-6max-br4-pass-small-edges-vs-fish-012` · beginner · multi-street · any · consensus 0.50 · sources: br79 · **draft**

**Claim.** Against a clearly bad opponent, skip the close, high-variance spots such as stacking off with a marginal hand or a weak draw. You will get their stack soon in a clear spot with a strong hand, and a low-variance style keeps you off tilt.

**Why.** The total you can win from a weak player is roughly their stack plus rebuys. Taking a 55/45 gamble now risks losing a stack you would otherwise collect at 80/20 a few hands later, and losing it hurts your decision-making for the rest of the session. The small edge forgone is real but tiny compared with the value of staying calm, in the game and positioned on the weak player. This is the opposite of how you should treat a regular, where thin edges are all you get.

**Common mistake.** Shoving a gutshot with two overcards into a fish's small bet because "I am probably ahead of his range".

**Hooks.** _You do not need to gamble with a fish. Wait._ · _The thin edge you skip is the stack you keep._ · _Why patience beats aggression against bad players._

Review: [ ]

### Do not bluff passive players off draws; their small bets give you odds anyway
`c-cash-6max-br4-passive-fish-never-pressure-006` · beginner · multi-street · srp · any · consensus 0.50 · sources: br79 · **draft**

**Claim.** When your flush draw misses the turn against a passive weak player, check rather than barrel. If you bet and get called you are committed to a river you may not want; if you check, they typically bet a tiny amount that prices you in to see the river for almost nothing.

**Why.** The danger of checking is normally that the opponent applies pressure and takes your draw's equity away. Passive players do not do that. They bet amounts that have no relation to the pot, which means you get to realize your equity cheaply while never putting yourself in a hard spot. Barrelling them achieves little since they rarely fold a pair, and it removes the chance to see the river cheaply. This is a large part of why these opponents are so profitable: they never make you guess for real money.

**Common mistake.** Firing a big turn bet with a missed draw into a station and being forced to call a river with nothing.

**Hooks.** _Missed draw against a fish? Check. They price your river._ · _Passive players never make you guess. Stop guessing for them._ · _The cheapest river card in poker comes from a station's bet._

Review: [ ]

### Start a session tight and straightforward; do not try to build an image
`c-cash-6max-br4-tight-start-no-image-004` · beginner · any · consensus 0.50 · sources: br79 · **draft**

**Claim.** With no information on new opponents, play tight and apply pressure only in clear spots. Attempts to set up an image early are wasted at micro stakes, where most opponents are not watching closely enough for an image to exist.

**Why.** Image plays only pay off against opponents who notice and adjust. Recreational players do not track your frequencies, and regulars have not seen enough hands yet. Meanwhile a loose, flashy start puts money at risk against players you have not typed. Keeping it simple for the first orbits lets you gather reads for free and spend chips only once you know who the weak players are and where they sit.

**Common mistake.** Opening wide and 3-betting light in the first two orbits "to look aggressive" against players who will never notice.

**Hooks.** _Nobody at NL5 is watching your image. Stop building one._ · _The first two orbits are for reads, not for moves._ · _Fancy play at the micros is just expensive noise._

Review: [ ]

### Let weak players have the small pots; you do not need an image against them
`c-cash-6max-br5-dont-fight-small-pots-vs-fish-004` · beginner · multi-street · any · consensus 0.50 · sources: br79 · **draft**

**Claim.** When a bad player makes a strange play against you, such as min-raising the turn with a medium pair, there is no need to raise back to show who is boss. Pass on thin spots against them. If you ever want to establish an image, do it against a regular who will actually notice.

**Why.** Weak players give their stacks away over time regardless of how you play the small pots, so fighting for them adds variance without adding much profit. Image plays are wasted on opponents who are not paying attention: they already think you are a maniac after you win a single pot, and they will not adjust in any coherent way. Your edge against them comes from big pots with big hands, not from winning every skirmish. Save the creative plays for regulars, where they can actually change future behaviour.

**Common mistake.** Raising a weak player's silly turn bet with air out of pride, then having to barrel the river into a player who never folds.

**Hooks.** _Stop fighting weak players for small pots._ · _He min-raised you with tens. The correct response is boring._ · _Image plays are wasted on players who are not watching._

Review: [ ]

### Moderate stats can hide big leaks, but chase the highest VPIP first
`c-cash-6max-br5-prioritize-highest-vpip-002` · beginner · any · consensus 0.50 · sources: br79 · **draft**

**Claim.** A player with ordinary-looking numbers (around 33/25) can still cold-call a 3-bet with king-nine and stack off, so never rule someone out on stats alone. But when deciding whom to isolate and whom to sit next to, prioritize the biggest VPIPs (60% and up), because they put the most money in with the worst hands.

**Why.** Stats describe how often a player enters pots, not how badly they play them. Some players with tame preflop numbers make huge postflop errors, and you should take the money when they offer it. Over a session, though, the player who sees 60% of flops gives you far more opportunities than the one who sees 30%, so your seat choice and isolation range should be built around the loosest player at the table.

**Common mistake.** Ignoring a player because their VPIP looks reasonable, or spending the whole session trying to outplay a 33/25 instead of the 62/5 two seats over.

**Numbers.** prioritize players with ~60%+ VPIP; a 33/25 can still make huge mistakes

**Hooks.** _His stats looked fine. He stacked off with king-nine anyway._ · _Not every bad player has bad stats._ · _Which seat makes you the most money? Check one number._

Review: [ ]

### Do not bluff players who do not fold; use cheap calls to see their hands instead
`c-cash-6max-br6-do-not-bluff-stations-call-to-see-hands-007` · beginner · multi-street · srp · any · consensus 0.50 · sources: br79 · **draft**

**Claim.** Against a loose passive player, skip the bluffs: no river bluffs, no semi-bluff raises with a draw when they will not fold, and check back draws rather than get blown off them. When a call is cheap, call to see the showdown; the information you gain for tagging them is worth more than the few blinds.

**Why.** Bluffs profit from folds, and this player type does not fold. Raising a draw into a player who will call or shove with any pair just builds a pot where you are behind. Checking your draws keeps you in the hand cheaply and lets their small bets give you odds. Cheap showdowns are a bonus: seeing that someone called down with ace-high or limped six-deuce lets you tag them with confidence and adjust for the rest of the session.

**Common mistake.** Trying to barrel a station off a pair, or raising a flush draw into a player whose range is nearly all made hands they will never fold.

**Hooks.** _Bluffing a calling station is just donating._ · _A cheap river call that pays for the whole session._ · _Why we check our draws against this player type._

Review: [ ]

### Do not ramp up preflop aggression against weak players; your edge lives after the flop
`c-cash-6max-br6-keep-preflop-pots-small-vs-fish-005` · beginner · preflop · 3bet-pot · any · consensus 0.50 · sources: br79 · **draft**

**Claim.** Against a loose weak player, resist getting medium pairs such as nines all in preflop or stacking off with a draw that is not huge. Call and play the hand out, because your advantage over them is largest on the flop, turn and river. Shoving money in early turns the hand into a who-hits-the-board lottery that only helps them.

**Why.** A weak player's mistakes happen postflop: calling too wide, betting silly amounts, folding to pressure in the wrong spots. Every chip that goes in preflop is a chip they get to put in before they have had a chance to make those mistakes, and nines against a loose range is close to a flip anyway. Keeping the pot smaller early means you get to realize your skill edge across three streets, and they will never put you in a genuinely tough spot: when they bet odd amounts with draws or made hands you can simply call with the right price.

**Common mistake.** 4-betting nines against a loose player because it looks like a value spot, converting a large postflop edge into a near coin flip.

**Schools disagree.** Equity-based and solver-based advice would happily get nines in preflop against a very loose player's 3-bet; this coach deliberately declines, preferring to keep the pot small and exploit postflop.

**Hooks.** _Nines all in preflop versus a fish? We say no._ · _Your edge against weak players is not where you think._ · _Stop turning your best spots into coin flips._

Review: [ ]

### Weak players react to the last pot: tilt after losing, go quiet after winning
`c-cash-6max-br6-weak-players-react-to-the-last-pot-008` · beginner · multi-street · any · consensus 0.50 · sources: br79 · **draft**

**Claim.** Right after a weak player loses a big pot, especially to you or after getting felted, expect them to play more hands and bet more: play as many pots with them as you can and let them bet into you. Right after they win a big pot off you, expect far less aggression: your bets get through. Time inducing plays for when you have been winning, not when they have.

**Why.** Recreational players are driven by the last result rather than by strategy. A loss makes them want it back, so they spew; a win makes them protective and passive. If you track who won the last few pots at the table, you can predict their next aggression level better than any HUD stat. A check-raise with the nuts, for example, only works against someone who is primed to bet, which is the player who just lost, not the one who just won.

**Common mistake.** Running a check-raise or induce line against a player who just dragged a big pot and is now content to check everything down.

**Hooks.** _He just lost a stack. Here is what he does next._ · _The best read at micro stakes is not on your HUD._ · _Time your tricky plays by who won the last pot._

Review: [ ]

### On very dry boards opponents must call ace-high, so value bet thinner and bluff more
`c-cash-6max-cc03-dry-board-ace-high-calls-020` · intermediate · turn · srp · ip · consensus 0.50 · sources: cc · **needs-review** · review note: _Edge case; strip solver-config-specific numbers before publishing._

**Claim.** When a board is so dry that almost nothing connects, the defender is supposed to keep calling unpaired overcards, ace-high and backdoors. That makes medium and even small pairs strong value bets on the turn (pocket sevens can land around 70% equity after being called), and it makes every air hand a fine bet against humans, who do not call ace-high nearly enough.

**Why.** Finishing equity depends on what the opponent continues with. On a wet texture his continuing range is full of pairs and draws, so middle pair with a gutshot is an underdog once called. On a bone-dry paired or king-high rag board his continuing range is mostly unpaired hands, so a low pair dominates it. The same fact works in reverse for bluffing: because theory asks him to call with hands like ace-nine, a human who folds those is over-folding, and betting your whole air range at a 3/4 size becomes highly profitable. Hands as low as pocket deuces can even show a slim value-plus-denial bet in theory here, which illustrates how far the dry-board effect goes, though that is an edge case rather than a rule.

**Common mistake.** Checking back middle or low pairs on a blank turn because "I only beat ace-high", when ace-high is exactly what he is calling with.

**Numbers.** example dry turn, 75% pot bet: pocket sevens ~72% landing equity, ace-six ~70%, pocket nines ~78%, pocket jacks ~80% · ace-queen and ace-ten high: check

**Hooks.** _On this board he has to call ace-high. Punish it._ · _Pocket sevens, 72% equity after he calls. Bet._ · _Dry board, blank turn: every air hand is a bet._

Review: [ ]

### Open the smallest pairs from early position only when weak players are behind
`c-cash-6max-cc06-open-small-pairs-vs-weak-players-023` · beginner · preflop · utg · consensus 0.50 · sources: cc · **draft**

**Claim.** Deuces and threes from the first seat are a marginally losing open against competent opponents, so a chart will say fold. With one or more weak players left to act, open them - the extra post-flop EV turns the open profitable.

**Why.** Equilibrium charts tell you what is barely losing against players who punish you correctly. The margin on the smallest pairs is tiny, which means table composition swings the answer. Against a table of regulars, folding costs almost nothing and avoids playing a weak hand out of position. Against passive callers who pay off sets and give free cards, the same hand gains more than the chart loss. Treat the chart as a baseline for the hardest conditions and move off it when the conditions are softer, not as a rule to follow regardless of who is sitting behind you.

**Common mistake.** Following a preflop chart rigidly and folding small pairs from early position at a table full of players who will call and pay off.

**Hooks.** _The chart says fold deuces. Sometimes the chart is wrong._ · _One table change that flips a preflop fold to an open_ · _Why charts assume the toughest table_

Review: [ ]

### Against opponents who rarely check-raise rivers, keep going big with your value
`c-cash-6max-gp32-big-size-vs-low-check-raisers-003` · intermediate · river · srp · ip · consensus 0.50 · sources: rio · **draft**

**Claim.** Solvers mix half-pot bets into strong hands partly to protect against river check-raises. Against the typical opponent who almost never check-raises the river, that protection is unnecessary, so betting the largest size your hand can support remains the better play.

**Why.** The reason a solver spreads strong hands across sizes is that a pure big-betting range would be easy to attack with raises. Real players at most stakes raise rivers far less than equilibrium, so the big bet faces calls or folds, not pressure. Against them, maximizing the amount called with each value hand matters more than balance. Learn the equilibrium sizes in the trainer, but do not let a check-raise-heavy solver talk you out of a habit that profits against your actual pool.

**Common mistake.** Copying the solver's half-pot frequency against players who will never punish the bigger size.

**Schools disagree.** Some coaches teach copying solver river sizing mixes regardless of opponent; this source says go big against passive pools.

**Hooks.** _The solver bets half pot. You should bet more._ · _Most regs never check-raise rivers. Punish that._ · _Why your river bets should be bigger than GTO._

Review: [ ]

### Treat a regular's single flop size on a texture as their whole strategy there
`c-cash-6max-gp34-one-size-is-their-size-010` · advanced · flop · 3bet-pot · oop · consensus 0.50 · sources: rio · **draft**

**Claim.** When a thinking opponent uses one bet size on a flop texture, assume that is their simplified size for that spot and run your sim with only that size available to them. One observation is enough for an opponent known to simplify early streets.

**Why.** Strong players build their flop plans around one or two sizes per texture, so a single sighting usually reveals the whole strategy for that board class. Solving with the opponent restricted to that size gives you hand rankings for the spot you will actually face, rather than for a mix of sizes the opponent never uses. Solving to around 2% accuracy is plenty for hand-ranking questions, because the frequencies and relative hand values converge long before suit-level details do.

**Common mistake.** Studying against the solver's default mix of bet sizes when the opponent in front of you has shown they only use one.

**Hooks.** _One bet from a reg tells you their whole flop plan._ · _Stop solving against sizes your opponent never uses._ · _You don't need a perfect sim to rank hands._

Review: [ ]

### When a 3-bettor checks a flop they normally bet and then raises, fold your marginal hands
`c-cash-6max-gp35-fold-marginal-vs-rare-check-raise-016` · intermediate · flop · 3bet-pot · ip · consensus 0.50 · sources: rio · **draft**

**Claim.** If the out-of-position player checks a flop that the population almost always c-bets, treat the check itself as suspicious. When they then check-raise your bet, fold marginal hands even if the solver shows a close call.

**Why.** A spot that is near-indifferent in theory becomes a clear fold when the opponent's line is far more weighted to strength than equilibrium assumes. Most players only check these flops with hands they are trapping with or giving up on, and only raise with the former. There is also very little to gain: these spots are rare, the sim is less accurate deep in the tree, and sticking around with a weak pair wins almost nothing even when correct. Reserve your tough calls for the common spots where the opponent's range is actually balanced.

**Common mistake.** Hero-calling a check-raise in a line nobody takes as a bluff because the trainer showed a mixed strategy.

**Hooks.** _They checked a flop they always bet. Be suspicious._ · _A close call in theory is a fold in practice here._ · _Rare spot, marginal hand, big raise. Just fold._

Review: [ ]

### Against passive opponents, keep a big bet on high-low-low boards when checked to
`c-cash-6max-gp35-keep-big-bet-vs-passive-high-low-low-007` · intermediate · flop · 3bet-pot · ip · consensus 0.50 · sources: rio · **draft**

**Claim.** On a high-low-low flop like J64 rainbow in a 3-bet pot, your range when checked to contains many strong top pairs. If the opponent plays passively against small bets, keep the large size in your strategy for value instead of simplifying it away.

**Why.** On these boards, hands like ace-jack, king-jack and queen-jack make up a big share of your range and want to grow the pot against the opponent's medium pairs and weaker jacks. The solver's small bet relies on the opponent raising with draws and bluffs; a passive player does not, so the small bet gives up value exactly where you have the most of it. Keep the small size for your bluffs and marginal hands, but let strong hands bet big on this texture against this type.

**Common mistake.** Applying a single small-bet simplification to every opponent, including ones who only call or fold.

**Example.** positions: BTN vs SB, 3-bet pot | hero: KhJs | board: Jd6c4s | action: BTN calls a 3-bet from SB. Flop: SB checks. | decision: Bet 30% or bet large? | answer: Against a passive opponent who rarely check-raises, bet large; the small size only pays off if they raise enough with worse.

**Hooks.** _Checked to on J64 in a 3-bet pot? Bet big._ · _Passive villain, strong top pair, small bet. Three mistakes._ · _The solver's small bet assumes something your opponent won't do._

Review: [ ]

### Only frequency mistakes make a bet size profitable, not hand-selection mistakes
`c-cash-6max-gp36-frequency-vs-selection-mistakes-006` · advanced · flop · 3bet-pot · oop · consensus 0.50 · sources: rio · **draft**

**Claim.** When judging whether opponents will misplay a bet size, ask whether they will fold or raise the wrong amount overall. Defending with the wrong hands at the right frequency barely changes your EV; folding noticeably too often does.

**Why.** A solver response to a small bet contains hands that look impossible to find, such as raising an offsuit ten-nine with no pair, while also folding some offsuit broadways. Real players will swap one for the other, but that is a hand-selection error and roughly a wash. If instead their total fold frequency climbs from about 17% to about 28% against a small bet, your whole betting range gains automatic profit and the small size becomes clearly right. Focus on aggregate fold and raise frequencies when choosing a size, and use node-locking only if that specific question is the deciding factor.

**Common mistake.** Picking a bet size because one branch of the solver response looks hard to play, without checking whether opponents actually fold or raise too much overall.

**Numbers.** Example: fold vs 30% pot moving from ~17% to ~28% turns the small bet into a clear win

**Hooks.** _They defend the wrong hands. That makes you nothing._ · _The only opponent mistake that pays your bet size._ · _Stop chasing solver lines nobody could find anyway._

Review: [ ]

### Barrel far more often on 774 after the big blind only calls the flop
`c-cash-6max-tc16-barrel-wide-after-flop-call-001` · advanced · turn · srp · btn · consensus 0.50 · sources: 2cc · **draft**

**Claim.** As the button in a single-raised pot on a 774 two-tone flop, once the big blind just calls your c-bet you can raise your turn barrel frequency from the solver's roughly 54% to about 85%, close to a range bet on most turn cards.

**Why.** Real big blinds check-raise 774 with more of their flush draws, straight draws and A7 than theory does. Every hand they raise on the flop is a hand that is missing from their calling range. So the range that reaches the turn by calling is thinner than the solver's version, with fewer draws and fewer strong trips. A thinner calling range folds more to a second bet, and that is exactly what a wide barrel punishes. This is the cautious exploit, computed against an opponent who may notice and readjust, so the barrels stay roughly balanced between value and bluffs.

**Common mistake.** Barreling at the same ~50% clip the solver uses against a theoretical range, and letting a weak, draw-light calling range see a free river.

**Numbers.** GTO turn barrel ~54% on 774 after BB calls flop · exploit barrel ~85% when BB over-check-raises the flop

**Hooks.** _Most players barrel 774 half the time. Try 85%._ · _What they check-raise with tells you what they cannot call with._ · _The flop call is the leak. The turn barrel collects._

Review: [ ]

### Barrel every flush-completing turn on 774, except the ace
`c-cash-6max-tc16-flush-turn-range-barrel-002` · advanced · turn · srp · btn · consensus 0.50 · sources: 2cc · **draft**

**Claim.** When the flush card arrives on the turn of a 774 two-tone board after the big blind called your c-bet, barrel at or near 100% of your range. The ace of the suit is the one exception.

**Why.** A typical big blind check-raises more flush draws on 774 than the solver would. Whatever they check-raise cannot also sit in their flop calling range, so when the third suited card lands they hold far fewer flushes than the board suggests. That lets you lean on them with your whole range, for value and as a bluff alike. The ace is different because it changes the top-pair picture for both players and cuts how often your medium hands want to bet.

**Numbers.** barrel ~100% on non-ace flush-completing turns

**Hooks.** _The flush came in. Bet everything. Here is why._ · _Scared of the third spade on 774? Your opponent should be._ · _One turn card you can range-bet against most players._

Review: [ ]

### Low straight turns and blanks on 774 stay barrel-heavy, the four does not
`c-cash-6max-tc16-straight-and-blank-turns-003` · advanced · turn · srp · btn · consensus 0.50 · sources: 2cc · **draft**

**Claim.** After a flop call on 774, barrel heavily on 3x, 5x and 6x turns that complete straights, and on blanks from a deuce up through the queen. Slow down on the four.

**Why.** Hands like 65, 63 and 53 get check-raised more often than theory by a real big blind, so their calling range reaches the turn with fewer completed straights than the board implies. The same logic covers blanks. Flush draws and A7 have also partly left the calling range, so what remains is weaker across the board and continues less than a solver range would. The four is the exception because it hands trips or a full house to the many 4x combos that do call the flop.

**Numbers.** 8x through Qx turns of any suit barrel heavily

**Hooks.** _A six hits on 774. Why you keep betting anyway._ · _The one turn card to stop barreling on 774._ · _Straight-completing turn? Their straights are mostly gone already._

Review: [ ]

### C-bet about 37% instead of 57% on 774 when the big blind over-check-raises
`c-cash-6max-tc17-cbet-less-vs-over-check-raiser-006` · advanced · flop · srp · btn · consensus 0.50 · sources: 2cc · **draft**

**Claim.** If you expect the big blind to check-raise 774 more often and fold less often than theory, cut your c-bet frequency by roughly 20 points, from about 57% to about 37%, and bet a stronger range.

**Why.** A c-bet on this board will meet aggression more often than the solver assumes. When a bet gets raised more and folds less, the marginal bets with high cards and thin pairs lose value, while the hands that do bet should be the ones happy to continue against a raise. Reaching the check-raise node with a stronger range gives you more leverage against a draw-heavy raiser and avoids being pushed off equity you could have realised by checking.

**Common mistake.** Keeping the solver's thin c-bets in the range while the opponent's raise frequency climbs, then getting check-raised off six-out hands over and over.

**Numbers.** exploit c-bet ~37% vs GTO ~57% on 774

**Hooks.** _They check-raise too much? Bet less, not more._ · _Twenty points fewer c-bets on one flop. Here is why._ · _Bring a stronger range to the fight you know is coming._

Review: [ ]

### Real big blinds check-raise 774 more and fold less than theory
`c-cash-6max-tc17-population-check-raises-774-more-005` · advanced · flop · srp · bb · consensus 0.50 · sources: 2cc · **draft**

**Claim.** Against a button c-bet on 774, the population check-raises about 23% instead of just over 20%, calls about one point more, and folds less. The extra raises come mostly from flush draws, especially ace-high ones, combo draws like 53 and 65, and A7; the extra calls come from queen-high and king-high backdoor hands.

**Why.** Players like to play draws fast on paired boards and almost never slow-play strong trips the way a solver does, so A7 gets raised where theory would often call. Straight draws such as 65 move from a 65-80% raise to 90-95%. Second and third pairs, underpairs, overpairs, full houses and quads behave roughly as in theory. The net effect is a check-raising range that is heavier in draws and weaker on average, and a flop calling range that is slightly wider but missing many of its draws.

**Numbers.** population check-raise ~23% vs GTO ~20% · 65-type straight draws raised 90-95% vs 65-80% GTO · calls ~1-2 points above GTO

**Hooks.** _Real players never slow-play trips on 774. Use that._ · _On paired boards, the check-raise is usually a draw._ · _Three extra points of check-raises change everything._

Review: [ ]

### 3-bet about 22% on 774 against a draw-heavy check-raiser
`c-cash-6max-tc18-3bet-22-vs-draw-heavy-raiser-002` · advanced · flop · srp · btn · consensus 0.50 · sources: 2cc · **draft**

**Claim.** Against a big blind who check-raises 774 with more flush draws, straight draws and A7 than theory, lift your 3-bet frequency from about 4% to about 22%, fold more than 10 points less, and move many hands that would have called into the re-raise.

**Why.** The real check-raising range is weaker than the solver's because it carries more draws and fewer slow-played monsters. Draws still have to continue against a 3-bet, so your strong hands get more money in while ahead. Full houses go from a 12-13% re-raise to over 40%, trips from around 15% to more than half, and A7 almost always. The lower 7x still lean toward calling, as in theory, but the whole curve shifts toward aggression.

**Numbers.** 3-bet ~22% vs ~4% GTO · full houses 3-bet 40%+ vs 12-13% · trips 3-bet ~50-55% vs ~15% · fold >10 points less than GTO

**Hooks.** _Five times more 3-bets on one flop. Here is the read._ · _Stop slow-playing trips against people who raise draws._ · _Their check-raise is a flush draw. Make it pay._

Review: [ ]

### Max exploit vs a 774 check-raise is to 3-bet all trips and better, except quads
`c-cash-6max-tc18-max-exploit-3bet-value-only-006` · advanced · flop · srp · btn · consensus 0.50 · sources: 2cc · **needs-review** · review note: _Max-exploit line; publish only framed as theoretical ceiling (see tc17-007)._

**Claim.** If the big blind will never readjust, re-raise every 7x and better at 100% against their check-raise and never re-raise a bluff. Pocket sevens is the one exception; it calls.

**Why.** A check-raising range stuffed with flush draws and backdoor draws is behind trips and keeps putting money in anyway, sometimes even 4-betting. The most profitable response is to raise only hands that are happy to be called. Quads break the pattern because they hold both remaining sevens, so they block all of the big blind's trips and get no value from a raise; calling and letting draws keep bluffing earns more. The line is unbalanced by design, which is why it only works against an opponent who does not adapt.

**Numbers.** max exploit: 3-bet value at 100%, bluffs 0%

**Hooks.** _The one monster that never 3-bets: quads._ · _Zero bluffs in the raising range. Still correct here._ · _When they raise draws, raise only your best hands back._

Review: [ ]

### Barrel slightly less on K72 after a typical big blind calls the flop
`c-cash-6max-tc31-barrel-slightly-less-k72-001` · advanced · turn · srp · btn · consensus 0.50 · sources: 2cc · **draft**

**Claim.** On a K72 two-tone flop in position, after you c-bet your whole range and a typical big blind calls, barrel the turn about 35% rather than the solver's 38%, assuming the opponent might readjust.

**Why.** Real big blinds fold more and call less on K72 than theory, so the range that reaches the turn by calling has less air in it. At the same time your flop range was wider than the solver's because you were range-betting. A stronger calling range meeting a weaker betting range means fewer profitable second barrels. The gap is small, but the direction is the opposite of the paired-board adjustment, which is why reads have to be checked board by board.

**Common mistake.** Assuming an exploitable opponent always means betting more. A tighter flop caller earns a slightly tighter barrel.

**Numbers.** cautious-exploit barrel ~35% vs GTO ~38% on K72

**Hooks.** _You range-bet the flop. Now barrel less. Here is why._ · _Exploit does not always mean more aggression._ · _Three percent fewer barrels on K72, and it matters._

Review: [ ]

### Barrel your whole range on flush turns on K72 if the big blind will not adapt
`c-cash-6max-tc31-range-barrel-heart-turns-002` · advanced · turn · srp · btn · consensus 0.50 · sources: 2cc · **needs-review** · review note: _Max-exploit line; publish only framed as theoretical ceiling (see tc17-007)._

**Claim.** Against a big blind who check-raises K72 with their king-high flush-suit combos and flush draws, the maximum exploit barrels almost 100% of hands on any turn that completes the flush.

**Why.** Population check-raises top pair holding a card of the flush suit, and most flush draws, on this flop. Those combos leave their flop calling range, so when the third suited card arrives they are much lighter on flushes than the board suggests. That lets you bet value and bluffs alike. This is a maximum exploit, meaning it is only correct against an opponent who will not notice and start calling down with more flushes.

**Numbers.** max exploit barrel ~100% on flush-completing turns

**Hooks.** _The flush card is your card, not theirs._ · _Why most players have no flushes when the third heart lands._ · _One turn card you can bet with any two on K72._

Review: [ ]

### Real big blinds check-raise K72 with stronger hands and less backdoor junk
`c-cash-6max-tc32-population-check-raise-composition-004` · advanced · flop · srp · bb · consensus 0.50 · sources: 2cc · **draft**

**Claim.** Against a button c-bet on K72, the population check-raises at roughly the solver's frequency but with a different mix. Fewer raises and calls with offsuit backdoor hands like Q9, J9, Q8 and T8, fewer raises with second and third pairs, more raises with good top pairs such as KQ and K8-plus with a flush draw, and a bit more with two pair and sets. Overall they call less and fold more.

**Why.** Most players do not continue with offsuit nine-high backdoor draws out of position, so the bottom of the theoretical range simply folds. They also tend to raise strong top pairs for value or protection rather than call with them. Removing air from the bottom and adding strength at the top makes the real check-raising range considerably stronger than the solver's, which matters both for how often you should bet and for how you respond to the raise.

**Hooks.** _Same check-raise frequency, much stronger range. Adjust._ · _Nobody check-raises jack-nine offsuit on K72. Theory does._ · _When a reg check-raises K72, believe them._

Review: [ ]

### Range-bet K72 against typical big blinds
`c-cash-6max-tc32-range-bet-k72-vs-population-005` · intermediate · flop · srp · btn · consensus 0.50 · sources: 2cc · **draft**

**Claim.** Against a typical big blind on K72 two-tone, c-bet 100% of your range rather than the solver's 80%. Both the cautious and the maximum-exploit models agree, and the adjustment gains a little EV over theory.

**Why.** The population folds more to a c-bet than the solver and check-raises no more often, so every hand that theory checked for showdown reasons now profits from betting. A range bet also simplifies your decisions and hides your hand. The one caveat is that your flop betting range becomes wider and weaker, which affects how often you can barrel the turn when called.

**Common mistake.** Checking back ace-high and queen-high on K72 against players who fold the flop too often, giving away the fold equity a range bet collects.

**Numbers.** exploit c-bet 100% vs GTO ~80% on K72

**Hooks.** _One flop where the simple play is also the best play._ · _K72 against most players: bet every single hand._ · _Eighty percent is theory. One hundred is the exploit._

Review: [ ]

### Against a real K72 check-raise, fold most backdoor draws and continue with flush draws
`c-cash-6max-tc33-fold-backdoors-vs-real-check-raise-002` · advanced · flop · srp · btn · consensus 0.50 · sources: 2cc · **draft**

**Claim.** When the big blind check-raises K72 with fewer offsuit backdoor hands and more sets and two pair than theory, fold far more of your air. Almost all offsuit ace-highs go, only a few AQ, AJ and AT holding the ace of the flush suit call, and among suited hands only flush draws plus the best backdoor flush draws (AQs down to about ATs, QJs to 98s in the second suit) continue.

**Why.** The real raising range has trimmed its air at the bottom and added strength at the top, so your hands with only backdoor equity are in worse shape and meet fewer bluffs. A direct flush draw still has enough equity, a backdoor one no longer does unless it also has high-card value. Overall 3-betting rises from under 1% to about 3% and calling falls, which is the normal response to a stronger raising range.

**Common mistake.** Floating the raise with every backdoor flush draw because the solver did so against its theoretical opponent.

**Numbers.** exploit 3-bet ~3% vs <1% GTO · continuing hands: direct flush draws plus the strongest backdoor flush draws only

**Hooks.** _Their check-raise got stronger. Your floats have to go._ · _No flush draw, no call. The K72 rule against real players._ · _Ace-ten offsuit facing a check-raise? Fold it._

Review: [ ]

### Max exploit vs a K72 check-raise is to 3-bet only value and call only draws and pairs
`c-cash-6max-tc33-max-exploit-value-only-006` · advanced · flop · srp · btn · consensus 0.50 · sources: 2cc · **needs-review** · review note: _Max-exploit line; publish only framed as theoretical ceiling (see tc17-007)._

**Claim.** If the big blind will never readjust, re-raise their K72 check-raise with top pair plus a flush draw, ace-king and pocket aces holding a flush-suit card, and every two pair and set, all at 100%. Never 3-bet anything else. Call all flush draws, AQ through AT and JT with a backdoor flush, 2x, second pairs and underpairs, and fold everything else.

**Why.** With a value-only 3-bet range you get the most money in against a raiser who continues and 4-bets with a stronger range, and the flush-draw requirement on the top pairs adds equity against the sets you sometimes meet. The calling range is pure made hands and direct draws because the raiser's range has too little air left to let backdoor hands realise their equity. The line is wildly unbalanced, so it only belongs against an opponent who never notices.

**Numbers.** max exploit: 3-bet value at 100%, bluffs 0% · calls: flush draws, AQ-AT and JT backdoor flush, 2x, second pair, underpairs

**Hooks.** _Zero bluff 3-bets. Against most players, still correct._ · _Top pair plus flush draw: raise, never call._ · _The max exploit is simple. That is what makes it dangerous._

Review: [ ]


## bet-sizing  (27)

### Size up to a slight overbet when they will call anyway
`c-cash-6max-br1-overbet-vs-nonfolders-005` · beginner · multi-street · any · consensus 0.50 · sources: br79 · **draft**

**Claim.** When you hold a strong hand against a micro-stakes player who never folds a draw or a pair, bet a bit more than the pot on the turn and river. If their calling range does not shrink as the bet grows, a smaller bet is simply money left behind.

**Why.** Bet sizing is a trade between how often you get called and how much you win when called. Against a thinking opponent a larger bet cuts their calling range, so you balance the two. Against a player who calls draws and weak pairs regardless of price, the first half of the trade disappears. You are being called the same amount of the time whatever you bet, so the only lever left is the size. This also charges draws correctly on wet boards where you would otherwise give them a cheap card.

**Common mistake.** Betting half pot "to keep them in" against someone who was never going anywhere.

**Numbers.** Slight overbet (a little above 100% pot) on turn and river against stations

**Hooks.** _If they always call, why are you betting half pot?_ · _The overbet is a value tool at micro stakes, not a bluff._ · _Betting small against a station is leaving money on the table._

Review: [ ]

### Open bigger with strong hands when the callers behind you do not care about size
`c-cash-6max-br4-raise-bigger-vs-callers-008` · beginner · preflop · any · consensus 0.50 · sources: br79 · **draft**

**Claim.** If the players likely to call your raise call 4x as readily as 3x, raise 4x or more with your big hands. Against a limper you intend to isolate when deep, 8-9 big blinds is fine. There is no reason to use a small size when a larger one is called just as often.

**Why.** Open sizing is a balance between getting action and getting value. When the opponent's calling decision does not depend on the size, only the value side remains, so a bigger raise simply builds a bigger pot while you hold the better hand. Isolating a limper with a large raise also thins the field so you play the hand against the weak player rather than the whole table. Keep a sensible size when thinking players are the likely callers.

**Common mistake.** Using one fixed open size against everyone and leaving value behind against players who call anything.

**Numbers.** Raise ~4x instead of 3x with big hands vs sticky callers · Isolate a limper ~8-9bb when deep

**Hooks.** _If they call 4x anyway, why raise 3x?_ · _Your open size should change with who is behind you._ · _One sizing tweak that adds a bet to every big pot._

Review: [ ]

### Raise premiums bigger when a loose player is behind or you are out of position
`c-cash-6max-br5-size-up-premiums-vs-loose-callers-003` · beginner · preflop · any · consensus 0.50 · sources: br79 · **draft**

**Claim.** A standard open is about 3x from every seat, but with a premium hand and a weak player left to act, go 4x: if they call 4x as readily as 3x, you simply earn more. The same logic applies to isolating limpers: around 4x in position, a bit more when you will be out of position so they cannot limp and peel cheaply.

**Why.** Weak players at NL2-NL10 decide whether to play a hand, not whether the price is right, so their calling frequency barely changes between 3x and 4x. Charging more with your strongest hands against those players is free money, and it also builds a bigger pot for the streets where you have the equity edge. Out of position you want fewer multiway, cheap-peel situations, so a bigger raise narrows the field and puts the limper to a real decision. Micro-managing sizes like this is fine at these stakes because nobody is tracking your sizing tells.

**Common mistake.** Opening kings for the same 3x against a 100% VPIP player who would have paid 4x or 5x without blinking.

**Numbers.** standard open ~3x from every position · ~4x with premiums when a loose player is behind · isolate limpers ~4x in position, a little more out of position

**Hooks.** _If he calls 4x as often as 3x, why raise 3x?_ · _Your kings deserve a bigger raise against this player._ · _One sizing tweak that prints against loose callers._

Review: [ ]

### At micro stakes, bet bigger with strong hands and smaller with the rest
`c-cash-6max-br7-size-bets-by-hand-strength-at-micros-007` · beginner · multi-street · srp · any · consensus 0.50 · sources: br79 · **draft**

**Claim.** Use different bet sizes for different hand strengths: around 60% pot for a standard stab, 75% with top pair against a weak player, closer to full pot when you want stacks in. Opponents at NL2-NL10 do not track your sizing, so this unbalanced approach earns more than a single standardized size. Standardize only once you move up to stakes where players pay attention.

**Why.** A single bet size is a defence against observant opponents who would otherwise read your hand from your sizing. At the micros that defence is unnecessary because the population reacts to its own cards, not to your patterns. That frees you to charge the maximum with your strong hands and risk the minimum with your bluffs and stabs, which is simply more money per hand. Against players with very wide ranges, size up even your medium value bets, because they call with more.

**Common mistake.** Betting a rigid one-third pot with everything because a video said to, leaving value on the table against players who would have called much larger.

**Numbers.** bet presets ~60%, 75% and 100% of pot · ~75% pot with top pair against a weak player; a bit above 60% against very wide-range callers

**Schools disagree.** Balanced, standardized sizing is the solver-era default; the coach explicitly recommends unbalanced, hand-strength-based sizing at micro stakes because the population does not exploit it.

**Hooks.** _Balanced bet sizing is costing you money at NL10._ · _Bet big with the goods. Nobody at this stake will notice._ · _We studied how coaches size bets at micros. Two very different answers._

Review: [ ]

### Against short stacks, raise premiums smaller to get action and skip marginal isolations
`c-cash-6max-br8-adjust-raises-to-short-stacks-004` · beginner · preflop · any · consensus 0.50 · sources: br79 · **draft**

**Claim.** When the players likely to call are half-stacked or shorter, shrink your raise with aces or kings so they come along; you do not need a big preflop pot to get their whole stack in. Conversely, do not isolate a 40bb limper with a marginal hand: after the flop there is only a bet or two before all the money is in, and marginal hands play badly in that structure.

**Why.** Stack size dictates how many decisions remain after the flop. Against a short stack a premium hand wants a call, because any flop bet plus one more gets everything in, so a smaller raise that keeps them in is worth more than a big raise that folds them. A marginal isolation hand wants the opposite, room to use position and fold equity across streets, and short stacks remove that room, leaving you to commit or fold with a weak hand on the flop. Read the stacks before choosing both the hand and the size.

**Common mistake.** Raising aces to the same size against a 40bb stack as against a full stack and watching them fold, or isolating a short stack with queen-eight suited and having to commit on a nothing flop.

**Numbers.** a ~40bb stack leaves roughly one or two postflop bets before all-in

**Hooks.** _Aces versus a short stack: raise less, not more._ · _Why marginal hands and short stacks do not mix._ · _One stack check that changes your preflop sizing._

Review: [ ]

### If limpers insta-call your isolation raise, you are raising too small
`c-cash-6max-br8-calibrate-iso-raise-size-by-their-reaction-003` · beginner · preflop · limped · any · consensus 0.50 · sources: br79 · **draft**

**Claim.** The most common preflop sizing error at micro stakes is raising too little. The right isolation size is one that leaves the limper genuinely torn between calling and folding. If they call instantly every time, raise more; if they fold instantly every time, you could raise a bit less. Add extra when you are out of position or facing several limpers.

**Why.** A limper who calls without thinking is getting a price that makes their whole range playable, which hands them cheap flops in position against you. Raising to the point of indecision maximizes the mistakes they make either way: folding too much equity or calling with too little. More limpers and worse position both argue for a bigger raise because the pot is more likely to go multiway and you will have less control after the flop.

**Common mistake.** Raising a fixed 3x into three limpers from the blinds and then playing a four-way pot out of position.

**Numbers.** normal iso-raise OOP with several limpers would be larger than the standard open

**Hooks.** _They called your raise instantly. That is a sizing error._ · _The perfect raise size makes the limper hesitate._ · _Most micro players raise too small. Here is the fix._

Review: [ ]

### Huge range advantage with no nut advantage means range-bet small
`c-cash-6max-cc06-big-range-edge-no-nut-edge-bet-small-019` · intermediate · flop · srp · ip · consensus 0.50 · sources: cc · **draft**

**Claim.** On boards where your range has far more equity but the opponent can easily hold the nuts - a queen-paired board against a big blind who defends many queens, for instance - bet almost your whole range for a small size. Betting big would pile money in against an uncapped range.

**Why.** Your range equity can be enormous, around two-thirds of the pot, mainly because the big blind is full of junk and you have more decent hands like ace-king or a lower pocket pair. That justifies a very high betting frequency. But trips on a paired queen board need only a queen plus any kicker, which a big blind defender holds often. You do not have "way more" trips than they do as a share of range, and your quads and pocket aces are too few combos to count. With the top of the two ranges roughly equal, there is no benefit in building a big pot immediately; the small bet collects the frequency edge without exposing your many medium hands to a strong nut region.

**Common mistake.** Seeing 66% range equity and reaching for a large bet, when the opponent's uncapped trips region argues for betting small.

**Numbers.** Example: HJ vs BB on AQQ, raiser holds ~66% range equity but no large nut edge - range-bet small

**Hooks.** _66% range equity. Still bet small. Here's why._ · _When a big edge still calls for a small bet_ · _Who really has the trips here?_

Review: [ ]

### Bet frequency and bet size are separate dials with separate inputs
`c-cash-6max-cc06-frequency-and-size-are-independent-016` · intermediate · flop · srp · any · consensus 0.50 · sources: cc · **draft**

**Claim.** 'If I bet rarely I should bet big' is a fallacy. Frequency follows range advantage and size follows nut advantage, so all four combinations exist - including betting rarely and small, and betting your whole range big.

**Why.** The two often move together because the most common post-flop situation is a polarized bettor against a condensed caller - the caller has the range edge, the bettor has the nut edge, so bets are infrequent and large. That correlation gets mistaken for causation. But consider a blind-vs-blind monotone flop where both players hold flushes equally and the raiser's range is only slightly ahead - no nut advantage and little range advantage, so the correct play is to bet infrequently and small. Or a low paired board where the raiser's overpairs are untouchable and the big blind is full of junk - both advantages, so range-bet large. Diagnose the two inputs separately and let the outputs fall where they fall.

**Common mistake.** Asking "shouldn't we bet bigger since we only bet sometimes here?" and sizing up on a board where the opponent holds the nut region as often as you do.

**Numbers.** Example quadrant: SB vs BB monotone, ~52% range equity, no nut edge: low frequency, small size · Example quadrant: BTN vs BB low connected board, ~50% range equity but strong overpair edge: low frequency, big size

**Hooks.** _Betting rarely does not mean betting big._ · _Four c-bet strategies. Most players only know two._ · _Frequency and size: two dials, not one_

Review: [ ]

### Every hand has an investment ceiling - do not bet it past the pot it can handle
`c-cash-6max-cc06-investment-ceiling-022` · beginner · multi-street · any · consensus 0.50 · sources: cc · **draft**

**Claim.** Each hand can comfortably value bet up to a certain pot size and no further. Nutted hands have a near-unlimited ceiling and want a fast-growing pot; second pair has a low one. Choosing big sizes because "my range is ahead" can build a pot too large for the hand you actually hold.

**Why.** A set is happy in any pot size and benefits from geometric growth that leaves a river shove on the table. Second pair betting big on three streets creates a pot where it can no longer be a value bet, so the money went in for no purpose. This is the per-hand reason the nut-advantage rule exists - when the range is dense with high-ceiling hands, big flop sizing serves most of the range; when it is not, big sizing drags medium hands past their ceiling. Before sizing up, ask what pot your hand still wants to be in on the river.

**Common mistake.** Firing large bets with a medium hand on the back of a range read, then arriving at the river with a pot too big to value bet and no good option.

**Hooks.** _Your second pair cannot afford the pot you just built._ · _Every hand has a ceiling. Find yours before you size up._ · _Why sets bet big and second pair bets small_

Review: [ ]

### Nut advantage picks your flop c-bet size - 75% with it, 33% without it
`c-cash-6max-cc06-nut-advantage-sets-flop-size-015` · intermediate · flop · srp · any · consensus 0.50 · sources: cc · **draft**

**Claim.** Simplify flop c-betting to one size per board. When your range holds many more very-high-equity hands than the opponent's, use about 75% pot. When the top ends of the two ranges are similar, use about 33%. Range advantage decides how often you bet; nut advantage decides how big.

**Why.** Hands with 85-90% equity want to build a large pot quickly so that by the river an overbet or shove is available. If your range is dense with such hands, accelerating pot growth on the flop serves the whole range. If the opponent can hold the top hands as easily as you can, a big bet gains little and exposes your medium hands. Using one size keeps the strategy learnable and the lesson is that the choice should be made from the nut region of both ranges, not from how often you plan to bet. A bigger size will naturally mean fewer hands qualify as value bets, so you will be more polarized when you bet big, but polarity is a consequence of the size, not the reason for it.

**Common mistake.** Reasoning "I'm going to be polarized here, so I'll bet big". The causation runs the other way - the nut advantage justifies the big size, and the big size makes you polar.

**Numbers.** Large nut advantage: single flop size ~75% pot · No large nut advantage: single flop size ~33% pot

**Hooks.** _One rule for flop c-bet size. 33% or 75%._ · _Range advantage = frequency. Nut advantage = sizing._ · _You're betting big for the wrong reason._

Review: [ ]

### Barrel the turn with one size (~75% pot) while you learn
`c-cash-6max-cc07-single-size-turn-barrel-001` · beginner · turn · srp · ip · consensus 0.50 · sources: cc · **draft**

**Claim.** Until your fundamentals are solid, double-barrel the turn with a single size of roughly three-quarters pot instead of mixing several sizes. Limiting yourself to one size costs close to nothing as long as you still choose the right hands and frequency.

**Why.** A solver given three turn sizes will often spread its bets across them, or settle on an overbet. That looks intimidating, but the EV gap between a 75% bet and a 150% bet with the same hands is tiny, usually within solver noise. What really costs money is betting the wrong hands, checking your whole range, or folding draws: those are big EV leaks. Sizing choice between two sensible options is not. One familiar size lets you learn where the bottom of your value range sits and which bluffs are allowed, which is far more valuable at this stage than a complex sizing tree. Add overbets later, once you have stopped making the large mistakes.

**Common mistake.** Copying a solver's overbet-heavy turn strategy without understanding it, then misplacing value and bluff thresholds and losing far more than the sizing ever gained.

**Numbers.** Turn barrel size: ~75% pot as the single default · Restricting a solver from a 150% to a 75% turn size changed EV by a fraction of a percent of pot (noise)

**Hooks.** _You do not need three turn sizes. One is enough._ · _The solver overbets here. You can still bet 75%. Here's why._ · _Most turn sizing worries are noise. This isn't._

Review: [ ]

### Three-Broadway, one-straight flops take big sizes; three-straight boards take medium
`c-cash-6max-gp23-broadway-overbet-004` · advanced · flop · srp · ip · consensus 0.50 · sources: rio · **draft**

**Claim.** In position in a single raised pot, flops with three Broadway cards and only one possible straight (for example AKJ or KQT-type boards) favor large bets and overbets. Boards where three different straights are already possible shift toward a medium size around 75% pot, with the rare monotone exception using a small bet.

**Why.** On high Broadway boards the raiser owns nearly all the two-pair, set and top-pair-good-kicker combos, and the caller's range is capped and full of weak pairs and gutshots. That nut advantage is what licenses an overbet: you can polarize into strong hands plus bluffs and charge the maximum. Once a board offers three live straights, the caller holds more nutted and robust hands, so the raiser's advantage shrinks and the size comes down. Counting possible straights is a quick proxy for how much of the nut advantage you keep.

**Common mistake.** Betting the same 1/2 or 2/3 pot on every high-card board, which leaves value on the table when you hold the nut advantage and overcommits when you do not.

**Numbers.** overbet ~150% pot on three-Broadway, one-straight flops IP · ~75% pot on boards with three possible straights

**Hooks.** _Count the straights before you pick a size._ · _AKJ rainbow: why 150% pot beats half pot._ · _The flop where overbetting is the standard play._

Review: [ ]

### Pick one c-bet size per flop category and use it with your whole betting range
`c-cash-6max-gp23-one-size-per-texture-005` · intermediate · flop · srp · ip · consensus 0.50 · sources: rio · **draft**

**Claim.** Decide your flop c-bet size from the board texture, not from your hand. For example, every bet on an ace-high board is 25% pot and every bet on an all-low board is 75% pot, regardless of whether you hold a set or air.

**Why.** Solvers mix several sizes on most flops, but the EV gained from the mix is small compared with the cost of trying to execute it at the table. Fixing one size per texture loses only a sliver of EV while giving you a strategy you fully understand and can play without hesitation. It also removes the most common leak at small stakes: sizing that leaks hand strength. A single size forces your bluffs and value to look identical, and it makes studying turns far easier because there is only one pot size to prepare for in each category.

**Common mistake.** Betting big with strong hands and small with weak ones, which is exactly the pattern observant opponents exploit.

**Numbers.** ace-high flops: 25% pot only · all-low flops: 75% pot only

**Hooks.** _Your bet size should depend on the board, not your hand._ · _One size per flop. Here is why the pros simplify._ · _Sizing by hand strength is the leak you cannot see._

Review: [ ]

### Two-Broadway flops: keep the overbet and the quarter-pot bet, cut the checks
`c-cash-6max-gp30-two-broadway-keep-both-sizes-003` · advanced · flop · srp · ip · consensus 0.50 · sources: rio · **draft**

**Claim.** On flops with two Broadway cards and no ace, the solver uses both a 25% bet and a 150% overbet heavily and assigns each to clearly different hand classes. The right simplification is to keep both sizes and remove checking. Put an ace on the same board and the strategy usually collapses to a full range bet.

**Why.** Simplification means removing the option that is closest in value to another one. When two bet sizes are each used a lot and each has strong, consistent hand-class preferences, they are doing different jobs and dropping one costs real EV. Checks on these textures are the weak third option, so they go. The ace changes things because it gives the raiser an even larger range and nut edge, which pushes everything toward a single small bet. Before committing, it is worth scanning the caller's response to the small bet and the check-back line to confirm the simplification holds.

**Common mistake.** Collapsing KQx and KJx boards to a single medium size, which loses the value of the overbet with strong hands and the cheap pressure of the small bet with the rest.

**Numbers.** two-Broadway flops IP: 25% and 150% pot, checks removed

**Hooks.** _Two sizes, zero checks: the KQ7 plan._ · _Why the solver wants both a quarter pot and an overbet here._ · _Add an ace and the plan flips to one size._

Review: [ ]

### Size the river bet for the hands your opponent actually holds
`c-cash-6max-gp32-size-for-what-they-hold-011` · advanced · river · srp · ip · consensus 0.50 · sources: rio · **draft**

**Claim.** Choose the value size by asking which hands in the opponent's range will call. If the natural target is rare, say a jack on a low board after three checks, size to get called by what is actually there, like ace-high. If your hand blocks the main calling hands, size down.

**Why.** A value bet is only as good as the calling range it targets. After a checked-down hand, the opponent's medium pairs may be nearly absent, so a pot-size bet aimed at them is aimed at nothing; a size that ace-high or king-high calls does better. Likewise, holding one of the cards the opponent needs to call with cuts the calling range, so the same hand should bet smaller than its naked version. The solver's sizing choices in these spots mostly reflect this logic rather than hand strength alone.

**Common mistake.** Sizing by absolute hand strength ("top pair bets pot") without checking what remains in the opponent's range.

**Hooks.** _Who is calling your river bet? Size for them._ · _Top pair doesn't decide the size. Their range does._ · _Blocking their calls? Bet smaller._

Review: [ ]

### A big bet is right when the opponent will not put the money in for you
`c-cash-6max-gp35-big-bet-when-they-wont-raise-006` · intermediate · flop · 3bet-pot · ip · consensus 0.50 · sources: rio · **draft**

**Claim.** The small bet is only better for your strong hands if the opponent reacts by raising often enough. If they mostly call or fold against the small size, your top pair and better make more money by betting large yourself.

**Why.** Betting small with a strong hand is a trap play: you offer a cheap price hoping the opponent raises with draws, weaker pairs and bluffs, building a pot you will win. If they rarely raise, the pot stays small and you miss one or two streets of value against hands that would have paid a bigger bet. The small size still helps your bluffs and marginal hands, which want folds at a cheap price. So the decision hinges on the opponent's most common error against small bets, and for most players that error is passivity.

**Common mistake.** Betting a third of the pot with top pair "because the solver does" against someone who never raises and only calls or folds.

**Hooks.** _Small bets only work if they raise you. Do they?_ · _Your top pair is losing money to a small bet._ · _The question that decides big bet or small bet._

Review: [ ]

### One bet size per flop texture when checked to in a 3-bet pot, and know what it costs
`c-cash-6max-gp35-one-size-per-texture-cost-005` · advanced · flop · 3bet-pot · ip · consensus 0.50 · sources: rio · **draft**

**Claim.** After the 3-bettor checks, most textures have one clearly dominant in-position bet size, so simplify to it. Dropping the larger size on paired and high-low-low boards is a fine simplification, but it trades away some value from the top of your range.

**Why.** A single size per texture is easier to execute and keeps your ranges coherent under pressure. The downside is that the solver's big bet on some textures exists to extract value with strong but not premium hands. Removing it pushes those hands into the small size, where they win less against a passive caller. That is acceptable if you decide so consciously; it is a leak if you do it without noticing which hands pay for it.

**Common mistake.** Simplifying to a small bet everywhere and never asking which hands lost value in the process.

**Hooks.** _Simplifying your bet sizes has a price. Know it._ · _One size per flop. Here's what you give up._ · _The hidden cost of 'just bet small'._

Review: [ ]

### Two-Broadway flops in 3-bet pots want a geometric two-street size or a check
`c-cash-6max-gp36-geometric-two-street-sizing-003` · advanced · flop · 3bet-pot · oop · consensus 0.50 · sources: rio · **draft**

**Claim.** On flops with two Broadway cards, the 3-bettor's strategy is mostly checking with a low frequency of large bets sized so that two equal bets get all the money in by the turn. Expect to bet roughly a fifth to a quarter of the time and check the rest.

**Why.** Geometric sizing splits the remaining stack into equal bets across the streets you plan to bet, so a two-street version is a big flop bet followed by a turn shove. On two-Broadway boards the caller's range connects well, so the 3-bettor has little reason to bet medium hands and instead bets a polarized range of strong value and strong draws for a size that sets up stacks. A three-street version uses three equal bets to be all in by the river and shows up as an in-between flop size. This is a harder strategy to execute than range betting and deserves dedicated study.

**Common mistake.** Betting one-third pot on K-Q-x or A-K-x as the 3-bettor because it is a "high board", then having no plan when called.

**Numbers.** Two-Broadway textures: ~20-25% large-bet frequency, otherwise check

**Hooks.** _K-Q-x in a 3-bet pot: mostly check, sometimes bet huge._ · _The flop size that sets up a turn shove._ · _Why the 3-bettor goes big or goes quiet on Broadway flops._

Review: [ ]

### On low-low-low flops in 3-bet pots the big bet is the essential size
`c-cash-6max-gp36-low-boards-overbet-or-check-007` · advanced · flop · 3bet-pot · oop · consensus 0.50 · sources: rio · **draft**

**Claim.** On three-low-card flops, removing the small bet from the 3-bettor's strategy costs nothing, while removing the large bet or the check costs EV. Overbet-or-check and a single-size range bet are both near-zero-loss simplifications.

**Why.** The 3-bettor's range on a low board is mostly overcards with a few overpairs and sets, so the strategy wants to polarize: bet big with hands that can set up stacks and check the rest. A simplifier shows the small bet is redundant, that a pure overbet-or-check plan loses no EV while checking about 82% of the time, and that a full-range bet at one medium size loses only around 0.01 big blinds. Both are far easier to execute than the solver mix. Adding a wheel draw shifts preference toward a three-quarter pot size, which is why a single geometric three-street size is a robust catch-all for the category.

**Common mistake.** Firing one-third pot on 7-5-2 as the 3-bettor because low boards "look good for the raiser", when that size is the one the solver throws away first.

**Numbers.** Overbet-or-check on a low rainbow board: ~18% bet, ~82% check, 0 EV loss vs full mix · Removing checks on the same board: ~0.01bb loss · Range bet one medium size: ~0.01-0.02bb loss

**Hooks.** _On low flops the small c-bet is the size you can delete._ · _Check 82% of the time and lose nothing. Here's where._ · _Two simple plans for 7-5-2 that match the solver._

Review: [ ]

### When a category mixes sizes, keep the one that works on the most textures
`c-cash-6max-gp36-pick-size-that-fits-most-textures-005` · advanced · flop · 3bet-pot · oop · consensus 0.50 · sources: rio · **draft**

**Claim.** If a board class shows a mix of small, medium and large bets, simplify to the size that stays useful across the widest set of boards in the group, then check the few textures that preferred another size to confirm the loss is small.

**Why.** Low paired boards in 3-bet pots mix three sizes, but adding a high card to the texture removes the large bet entirely while the small bet survives, and a related high-paired board uses only the small bet. A size that keeps showing up across variations is the safe default for the whole category. Before committing, look at the boards where the bigger size was preferred and check the opponent's response to the small bet there. If they must still defend a wide, awkward set of hands, the small size is good enough and the strategy stays simple.

**Common mistake.** Choosing the size that looks best on one representative flop and applying it to the whole category without checking the neighbours.

**Hooks.** _Three solver sizes, one table decision. Pick like this._ · _The bet size that survives every version of the board._ · _Simplify sizing without giving away the pot._

Review: [ ]

### Use one c-bet size per flop instead of mixing four
`c-cash-6max-tc12-one-cbet-size-per-flop-001` · intermediate · flop · srp · btn · consensus 0.50 · sources: 2cc · **draft**

**Claim.** As the preflop raiser in position, pick a single c-bet size for each flop class rather than trying to mix several sizes across your range. Decide only which hands bet and which check.

**Why.** A full solver output for the button on a given flop mixes four or five bet sizes plus a check, and every single combo (even per suit) splits differently between them. Nobody can execute that at the table. Collapsing to one size turns an impossible memorisation task into two questions, bet or check and with what, which you can actually answer in real time. A simplified strategy you play accurately beats a theoretically perfect strategy you play badly.

**Common mistake.** Trying to copy a raw solver output with multiple sizes, then applying it inconsistently and bleeding more EV than the simplification ever would have cost.

**Numbers.** Solver default for BTN on a flop like AT9 rainbow mixes four bet sizes (small, medium, big, overbet) plus a check · A single marginal hand can split across all five options with a different mix for every suit

**Hooks.** _Solvers use four flop bet sizes. You should use one._ · _'Play like the solver' is costing you money. Here's why._ · _Stop mixing bet sizes on the flop. Do this instead._

Review: [ ]

### Restricting flop bet sizes costs almost no EV
`c-cash-6max-tc12-simplifying-sizes-costs-no-ev-002` · advanced · flop · srp · btn · consensus 0.50 · sources: 2cc · **draft**

**Claim.** Cutting the solver down to a single flop c-bet size loses little or no EV on most flops. You do not need to fear that simplification makes your strategy meaningfully worse.

**Why.** When you take sizes away, the solver compensates in two ways. First it changes frequencies, betting more often with a smaller size or less often with a bigger one, so the overall pressure on the opponent stays similar. Second it still has full freedom on the turn and river to repair whatever small inaccuracy the flop restriction created. The flop deviation therefore gets absorbed on later streets. On typical flops the EV of a one-size strategy matches the multi-size version to two decimal places.

**Common mistake.** Assuming a strategy with more options must be clearly better in practice, and refusing to simplify because of a theoretical EV gap that is close to zero.

**Numbers.** JT6 two-tone BTN vs BB: EV 3.27 with four bet sizes, 3.27 with a single size · Q96 rainbow: EV 3.48 with multiple sizes, 3.48 with only a 40% bet · Smaller allowed size -> solver bets more often; larger -> less often

**Hooks.** _We cut the solver to one bet size. EV didn't move._ · _One number tells you simplification is free: 3.27 vs 3.27._ · _Why the solver forgives you on the flop._

Review: [ ]

### BTN vs BB flop c-bets need only two sizes, 33% or 116%
`c-cash-6max-tc12-two-size-system-33-or-116-003` · intermediate · flop · srp · btn · consensus 0.50 · sources: 2cc · **draft**

**Claim.** In a single-raised pot, button against big blind, you can cover every flop with just two c-bet sizes - a small bet around a third of the pot or an overbet around 116% - and choose between them based on the texture.

**Why.** When a solver is forced to pick its single best size on each of roughly a hundred representative flops, it only ever chooses from about five options, roughly 25%, 40%, 67%, 116% and 150%. The small sizes can be merged into one third-pot bet and the overbets into one 116% bet with negligible loss. The 67% boards are the only ambiguous group, and checking them individually shows that moving them to the overbet loses less than moving them to the small bet. Two sizes is a system you can remember and execute under pressure.

**Common mistake.** Defaulting to one medium size like 50-67% on every flop, which is rarely the solver's preferred single size and leaves value on both the small-bet and overbet boards.

**Numbers.** Solver single best size across ~100 flops falls into ~5 buckets: 25%, 40%, 67%, 116%, ~150% · 25% and 40% merged into 33%; 150%+ overbets merged into 116% · 67% boards lose less EV when played as 116% than as 33% · Final system: 33% pot or 116% pot, nothing else

**Hooks.** _You only need two flop bet sizes. Not four._ · _Most small stakes players bet 60% on every flop. Wrong._ · _A third pot or an overbet. Nothing in between._

Review: [ ]

### Bet a third pot on low and connected flops where the big blind holds nutted hands
`c-cash-6max-tc13-bet-small-when-bb-has-nuts-003` · intermediate · flop · srp · btn · consensus 0.50 · sources: 2cc · **draft**

**Claim.** On low flops, especially paired or connected ones like 855, 742 or 654, c-bet small (around 33%) as the button. Do not overbet when the big blind's range contains as many or more of the nut hands as yours.

**Why.** The big blind's flatting range is heavy in small suited and connected cards that the button never opens. On 855 they hold far more 5x; on 742 they have 42s and 74s two pairs that the button cannot have; on 654 they hold 87, 73s and every small pair. When the opponent has plenty of sets, two pairs and strong draws, a big bet simply gets called or raised by hands that beat you, and your overpairs and overcards are not nearly as far ahead. A small bet keeps the pot manageable, still charges their weak holdings, and lets you reassess on the turn.

**Common mistake.** Firing big on a low board with an overpair because it 'looks like the nuts', then facing a check-raise from a range full of sets and two pairs.

**Numbers.** Small c-bet size ~33% pot · All 8-high, 7-high and 6-high flops in the sample fall in the small-bet group · Low paired flops like 855 and connected flops like 742, 654 are small-bet boards

**Hooks.** _Overbetting 654 with kings? That's a mistake._ · _The big blind has more nuts than you here. Bet small._ · _Low flop, big pair, small bet. Here's why._

Review: [ ]

### Overbet the flop on nine-high and higher boards with two big cards
`c-cash-6max-tc13-overbet-high-card-flops-001` · intermediate · flop · srp · btn · consensus 0.50 · sources: 2cc · **draft**

**Claim.** Button against big blind, the flops that want an overbet c-bet (around 116% pot) are all at least nine-high and usually contain two high cards, such as JT6, KQ3, KJ3, AQ4 or AK7. Low flops never want the overbet.

**Why.** On these boards two parts of the button's range gain a huge edge at once - overpairs and high-card pairs. The big blind three-bets most of QQ+, AK, AQ, KQ and similar before the flop, so after a flat call those hands are nearly absent from their range while the button still has all of them. At the same time the big blind can rarely hold the nuts here. On JT6 they have few jacks or tens, one possible set and some JT. When one player has most of the strongest hands and the other almost none, the big size is what gets paid.

**Common mistake.** Betting a medium size on high-card flops out of habit, failing to charge the big blind's capped range when the button's nut advantage is at its peak.

**Numbers.** Overbet size ~116% pot · All overbet flops are 9-high or higher; no 8-high, 7-high or 6-high flops overbet · Typical overbet boards: JT6, KQ3, KJ3, KT3, AQ4, AK7, AJ9

**Hooks.** _Overbet the flop here. Most players bet half pot._ · _KQ3 and JT6 share one feature. It decides your bet size._ · _Why the big blind can't have the nuts on these flops._

Review: [ ]

### Do not overbet paired boards where the big blind also holds trips
`c-cash-6max-tc13-paired-high-boards-no-overbet-004` · intermediate · flop · srp · btn · consensus 0.50 · sources: 2cc · **draft**

**Claim.** On a flop like QQT the button should not use the overbet even with a big overpair. When both players hold plenty of trips, the nut advantage that justifies the overbet is gone.

**Why.** The overbet works when the button has most of the nutted hands and the big blind has almost none. On QQT the button has many queens, but the big blind calls plenty of Qx preflop too. If the button overbets, the big blind can simply continue with every queen and a hand like pocket kings is no longer good most of the time it is called. Without a one-sided nut distribution, the size that gets paid is the smaller one.

**Common mistake.** Seeing a high paired board, assuming 'I have the overpair, they can't have much', and sizing up into a range full of trips.

**Numbers.** QQT is a small-bet board despite being high; KK cannot be overbet profitably there

**Hooks.** _Kings on QQT. Why the overbet backfires._ · _High board, no overbet. One reason._ · _The big blind calls every queen here. Plan for it._

Review: [ ]

### The max exploit on K72 overbets its bluffs and bets small for value
`c-cash-6max-tc31-small-value-overbet-bluffs-004` · advanced · turn · srp · btn · consensus 0.50 · sources: 2cc · **draft**

**Claim.** When the big blind will not adjust, the solver's maximum-exploit turn strategy on K72 uses low sizes for its value barrels and overbets for its bluffs.

**Why.** Against a static opponent there is no reason to keep sizing balanced. A caller who folds too much folds even more to a large bet, so bluffs want the size that produces the most folds. Value hands want to be called, and the smaller bet keeps the weaker part of the calling range in. The approach is extremely unbalanced and an attentive opponent would punish it, which is why it belongs only against players who never readjust.

**Common mistake.** Using one turn size for both value and bluffs against an opponent who never reads sizing, and leaving fold equity on the table.

**Hooks.** _Big bet means bluff. Against some players, that is correct._ · _Balanced sizing is a courtesy. Not everyone deserves it._ · _Overbet the air, bet small the value. On purpose._

Review: [ ]


## board-textures  (18)

### Paired flops are hard to hit, so c-bet them and respect draws over trips
`c-cash-6max-br3-paired-boards-cbet-008` · beginner · flop · ip · consensus 0.50 · sources: br79 · **draft**

**Claim.** A paired flop like 9-9-4 is a good c-bet board because an opponent connects with it rarely, including in 3-bet pots. When you hold top pair or an overpair and a draw-heavy paired board gets action from a wide player, assume flush draws far more often than trips.

**Why.** Only two cards in the deck make trips, while a wide-ranging player holds many more combinations of flush draws and straight draws. On the pure fold-equity side that means a c-bet gets through often. On the stack-off side it means a weak player who raises or shoves on a wet paired board is more likely drawing than holding a nine. You will occasionally run into trips, but you win the draws' money far more often.

**Common mistake.** Shutting down on paired boards because "they could have trips" and giving free cards to the flush draws that actually make up their range.

**Hooks.** _Paired flop? Bet it. Here is why they almost never have it._ · _Two cards make trips. Nine cards make the flush. Do the math._ · _The board everybody is scared of is your best c-bet._

Review: [ ]

### Define wet and coordinated, then check your overcards on those flops
`c-cash-6max-br4-wet-coordinated-check-005` · beginner · flop · srp · oop · consensus 0.50 · sources: br79 · **draft**

**Claim.** A wet flop has a flush draw; a coordinated flop has several middling cards close together. When a flop is both, such as 8-7-5 with two of a suit, do not c-bet two unpaired overcards against a weak player. Their range connects too often and they will not fold.

**Why.** Naming the texture makes the decision automatic. Flush draws plus connected middle cards produce the maximum number of pairs, straight draws and combination draws in a wide calling range. Overcards alone have about six outs and almost no fold equity against a player who calls with any piece, so a bet mostly builds a pot you are behind in. Check, see what develops, and remember that a passive opponent will often bet a small amount that gives you a cheap look anyway.

**Common mistake.** Betting every flop as the raiser and only noticing afterward that the board was both wet and coordinated.

**Hooks.** _Wet and coordinated are different things. Know both before you bet._ · _Eight-seven-five two-tone. Your ace-king should check._ · _The flop texture that turns c-bets into donations._

Review: [ ]

### Nut advantage sets your bet size; range advantage decides whether you bet at all
`c-cash-6max-cc03-range-vs-nut-advantage-009` · intermediate · turn · srp · consensus 0.50 · sources: cc · **draft**

**Claim.** Having more nutted combos than your opponent does not mean you are in a favourable spot. Nut advantage controls sizing (bigger when you have it). Range advantage, meaning whose whole range has more equity, controls whether bluffing is allowed. You can hold the nut advantage and still be in a world where bluffing is a blunder.

**Why.** On an ace-high paired board after the flop checks through, the big blind has more trips than the in-position raiser. But trips are rare; the rest of his range is stuffed with eight-high and ten-high air, while the raiser's checking range keeps plenty of pairs and ace-x because it checks optional value hands rather than only junk. So the raiser retains the range advantage from preflop. If the big blind leads with air because "I have more fours", the raiser simply does not fold enough and the lead loses money. Judging favourability means looking at both complete ranges, not the top sliver.

**Common mistake.** Saying "I have the range advantage here" when what you actually have is more combos of the nuts.

**Hooks.** _More nuts than him? You still can't bluff here._ · _Range advantage and nut advantage are not the same thing._ · _'I rep the trips' is not a strategy._

Review: [ ]

### You check to the raiser because your range is behind, not because they have initiative
`c-cash-6max-cc06-check-to-raiser-is-about-equity-not-initiative-009` · beginner · flop · srp · bb · consensus 0.50 · sources: cc · **draft**

**Claim.** The big blind checks most flops to the preflop raiser because its range is at a large equity disadvantage, not because the raiser "has the initiative". On the rare flops where the big blind's range has caught up, leading some hands is correct.

**Why.** Initiative and momentum are psychological stories, not strategic facts. Nothing about having raised preflop entitles a player to the first bet. What decides who acts aggressively first is range-vs-range equity on that flop. On a brick board like nine-deuce-deuce the big blind is miles behind - having more deuces is irrelevant because they are a sliver of a range full of junk - so checking the whole range is right. On a low connected monotone flop like six-five-four, the raiser's big unpaired cards are terrible and the big blind's small suited and connected hands have connected hard, so the big blind's range does well enough to start leading. Knowing the real reason you check lets you spot the flops where you should not.

**Common mistake.** Checking every flop as the big blind on autopilot "because they raised", without asking whether this board is one where your range actually does well.

**Hooks.** _'Check to the raiser' - the reason you were taught is wrong._ · _Initiative is a myth. Here's what actually decides who bets._ · _The flops where the big blind should lead_

Review: [ ]

### Ace-high, paired, monotone and wet boards strip the raiser's nut advantage
`c-cash-6max-cc06-textures-that-remove-nut-advantage-020` · intermediate · flop · srp · ip · consensus 0.50 · sources: cc · **draft**

**Claim.** The raiser's nut advantage lives in overpairs. Any texture that neutralizes overpairs - an ace or king on board, a pair the defender often holds, three of a suit, or a connected board the defender hits hard - removes it and calls for small sizing. Low, dry, disconnected boards preserve it and call for big sizing.

**Why.** Preflop raisers carry queens, jacks and tens that the caller mostly lacks. On ten-high-and-lower dry flops those pairs are still near the top of the equity ladder. An ace on the flop lets any random ace beat them; a king does similar damage, though less, because the raiser also holds more kings. A paired board of a rank the defender plays gives them easy trips. A monotone board hands flushes to both sides. Connected low boards give the defender's small suited connectors two pair, straights and big draws. In every case the gap at the top of the two ranges closes, so the hands that wanted a big pot are no longer uniquely yours. The harder a board is to connect with, the more an overpair keeps its power.

**Common mistake.** Betting big on ace-high or king-high flops out of habit because "I'm the raiser", when the ace has just erased the hands that made big bets worthwhile.

**Hooks.** _The ace on the flop just killed your sizing._ · _Five board types where your overpairs stop mattering_ · _Dry and low? Bet big. Here's the full list._

Review: [ ]

### The ace turn is often the worst overcard for the c-bettor on a dry board
`c-cash-6max-cc07-ace-turn-fallacy-009` · intermediate · turn · srp · ip · consensus 0.50 · sources: cc · **draft**

**Claim.** After a small c-bet on a dry low flop is called, an ace turn is usually the least favourable high card for the bettor, not the best. Ace-high hands had every reason to call the flop, so the caller connects with the ace and leapfrogs your overpairs.

**Why.** On a bone-dry flop like 7-5-2 rainbow, ace-high is comfortably good enough to call a one-third pot bet, so the big blind arrives on the turn with lots of A-x. When the ace lands, their cheap A6 or A9 suddenly beats your kings, queens and jacks, which were unique to your range. Your nut advantage shrinks sharply. By contrast a queen, or a true brick like a three, keeps your overpairs on top and gives them nothing. The ace becomes good for the raiser only when the caller could not keep ace-high: on wet flops like 9-8-6 where A-J offsuit folds, when you opened from early position and hold a bigger share of aces, or when you used a larger flop size that pushed ace-high out.

**Common mistake.** Firing every ace turn as a "scare card" because you are the preflop raiser, when the caller holds more aces than you after calling a small bet on a dry board.

**Example.** positions: SB vs BB | hero: KhKs | board: 7d5c2s Ah | action: SB opens, BB calls. Flop: SB bets 33%, BB calls. Turn: ace. | decision: Is the ace a good barrel card for the preflop raiser here? | answer: Not especially. BB kept most ace-high hands against the small bet, so the ace improves their range more than yours and demotes your overpairs. The world stays slightly favourable because of your remaining strong hands, but it is the lowest-EV turn of the thirteen ranks, so barrel more carefully than on a queen or a brick.

**Hooks.** _The ace turn is a scare card. For you._ · _'Ace turn, I'm the raiser, I bet' is costing you money._ · _Why the ace is the worst high card to barrel here._

Review: [ ]

### A low "brick" turn usually hits the flop bettor, not the caller
`c-cash-6max-cc07-bricks-belong-to-the-bettor-006` · intermediate · turn · srp · ip · consensus 0.50 · sources: cc · **draft**

**Claim.** After a flop bet and call, a low unconnected turn card such as an 8 on a J-6-3 board is not a true blank. The bettor holds far more of that card, because low-card hands were bet as bluffs on the flop while the caller folded them.

**Why.** The flop bettor's range is polarized, so weak holdings with an 8 in them, like Q8 or 85 suited, were near the front of the queue to bluff, not the back. The caller, meanwhile, needed something to continue with on J-6-3, and random 8-x was exactly what they threw away. So a card that looks dead actually pairs the bettor's air with some regularity and keeps their nut advantage intact. It does not flip the range advantage, because the condensed caller still has more equity on average, but it makes the turn a slightly better transaction for the bettor and nudges the barrel frequency upward. Only cards like a deuce that neither range interacts with are closer to real bricks.

**Common mistake.** Labelling every low turn a "brick" and playing it identically, missing that your range, not theirs, is the one that connects with it.

**Hooks.** _That 'brick' turn is your card, not theirs._ · _Why an 8 on J-6-3 helps the bettor._ · _Bluffing the flop with junk pays off on 'blank' turns._

Review: [ ]

### A ten-to-king turn on a low board is the c-bettor's best barrel card
`c-cash-6max-cc07-broadway-turn-on-low-board-008` · intermediate · turn · srp · btn · consensus 0.50 · sources: cc · **draft**

**Claim.** After c-betting a low or middling flop and being called, a turn ten, jack, queen or king is close to the most favourable world you can get. Bet around 70% of the time, value bet thin and bluff almost anything.

**Why.** Those cards belong to you for two reasons. Preflop the big blind 3-bet many of their strong broadway hands, so you hold more of them. On the flop, king-high or queen-high was pure air for both players, which means you bet it often as a bluff and they folded it almost always. The card also keeps your overpairs on top. The result is a range that pairs the turn far more often than theirs, with a large nut advantage preserved. In such a world the EV of your range can approach two-thirds of the pot and you can barrel almost as often as a range bet, something that almost never happens elsewhere in a single-raised pot. The ace is the notable exception to this pattern because ace-high often calls small flop bets.

**Common mistake.** Slowing down on a king turn because "it's a scare card for both of us", when it is really a scare card almost only for the caller.

**Numbers.** King turn on a J-high board, BTN vs BB after flop bet-call: bet ~70%, BTN EV ~67% pot · BB folds ~43% to the 75% barrel there (roughly breakeven for a bluff)

**Hooks.** _The best turn card to barrel is not the ace._ · _Bet 70% of the time on this turn. Yes, really._ · _Why a king turn is a monopoly for the preflop raiser._

Review: [ ]

### Flush-completing turns favour the flop caller, especially against an OOP bettor
`c-cash-6max-cc07-flush-turn-favors-flop-caller-010` · intermediate · turn · srp · oop · consensus 0.50 · sources: cc · **draft**

**Claim.** When the turn completes a flush after a flop bet and call, the caller gains more than the bettor. Out of position this usually makes the world unfavourable for the bettor; in position it is closer to neutral.

**Why.** The caller's range has passed a strength test: to continue on a two-tone flop they needed a pair, a draw or a backdoor, and suited hands with the flush suit were a big part of that. The bettor needed no such reason, since a flop bet can be made with any two cards, so their range is thinner in flush combos. Preflop also matters: the big blind defends more suited hands and fewer big offsuit pairs. When the third suit arrives, a cluster of the caller's hands jumps ahead of the bettor's overpairs, two pairs and sets, which lose EV on this runout. Add the EV tax of being out of position and the bettor should check at a high frequency and protect that checking range. In position, nut advantage and positional control keep the spot roughly even instead.

**Common mistake.** Treating the flush turn as "scary for both" and barrelling anyway, when the caller is far more likely to hold the flush and will raise.

**Hooks.** _The flush came in. Whose card is it? Not yours._ · _They had to earn their place in this pot. You didn't._ · _The flop caller owns the flush turn. Here's why._

Review: [ ]

### Build flop categories from what the solver does, not from how the board looks
`c-cash-6max-gp23-categories-from-strategy-001` · advanced · flop · srp · ip · consensus 0.50 · sources: rio · **draft**

**Claim.** When grouping flops for study, start from solver output and cluster boards that share the same c-bet size and frequency. Do not start from intuitive labels like "ace-high" or "king-high" and then try to describe what happens inside them.

**Why.** A category is only useful if every board inside it plays roughly the same way. If you draw the boxes first, you end up with groups that mix a range-bet texture and a mostly-check texture, and the guideline you write for the group is wrong for half of it. Sorting an aggregate report by the frequency of the smallest size, then by check frequency, then by the largest size, reveals which boards cluster together. Labels that fall out of this process feel odd at first but become intuitive with repetition, and they let you study one representative board per group instead of hundreds of near-duplicates.

**Common mistake.** Memorizing a fixed list of texture names before looking at any solutions, then forcing every flop into one of those names even when the strategies inside the box disagree.

**Hooks.** _Your flop categories are backwards. Here is the fix._ · _Stop sorting flops by high card. Sort them by strategy._ · _One study trick that cuts your flop work by 90%._

Review: [ ]

### Define "high", "middle" and "low" boards relative to the preflop ranges in your game
`c-cash-6max-gp23-flexible-board-definitions-007` · intermediate · flop · srp · consensus 0.50 · sources: rio · **draft**

**Claim.** Describe flop categories in rank classes (high-low-low, middle, all-low, paired with high or low side card) rather than exact cards, and keep the boundaries flexible. A reasonable default is middle boards from queen-high down to ten-high and low boards nine-high and below, with the number of possible straights as a separate split.

**Why.** A category exists so that one representative board teaches you how to play dozens of others. K43, K72 and Q42 all belong to a high-low-low group and play almost identically, so studying one sim covers them all. Where exactly "high" ends and "middle" begins depends on which cards your opponents call with preflop, and that differs between a tight full-ring pool and a loose 6-max pool. Treating the boundaries as adjustable keeps the plan useful when the ranges in your game are different from the ones in the sim.

**Common mistake.** Studying twenty different king-high rag boards individually and relearning the same pattern each time instead of studying one and transferring the lesson.

**Hooks.** _K72 and Q43 are the same flop. Study them once._ · _Why 'ten-high' is a middle board, not a low one._ · _You are studying the same flop over and over._

Review: [ ]

### Ace-low-low rainbow in a 3-bet pot is its own texture: heavy c-betting, almost no raising
`c-cash-6max-gp35-ace-low-low-rainbow-own-category-002` · intermediate · flop · 3bet-pot · ip · consensus 0.50 · sources: rio · **draft**

**Claim.** Treat ace-low-low rainbow flops in 3-bet pots as a separate category from other ace-high boards. The 3-bettor c-bets these at a very high frequency and the in-position caller should raise almost never.

**Why.** The 3-betting range is dense in ace-x and high pairs, so on an ace with two low rainbow cards the out-of-position player has a huge range and nut advantage and can bet nearly everything. The caller's range rarely has a hand strong enough to raise for value and there is little equity to protect, since no draws exist. Raising as a bluff runs into a range that holds the ace very often. Other ace-high boards with Broadway cards or flush draws belong in their normal categories and play more conventionally.

**Common mistake.** Lumping every ace-high flop together and bluff-raising A72 rainbow in a 3-bet pot.

**Hooks.** _A72 rainbow in a 3-bet pot. Never raise. Here's why._ · _The one ace-high flop that plays differently._ · _Why they c-bet A-low-low every time._

Review: [ ]

### When the 3-bettor checks the flop, study mid and coordinated boards first
`c-cash-6max-gp35-facing-check-which-boards-matter-004` · intermediate · flop · 3bet-pot · ip · consensus 0.50 · sources: rio · **draft**

**Claim.** A balanced 3-bettor checks roughly half of flops out of position, but real opponents, especially in 6-max and tournaments, c-bet far more. Focus your facing-check study on the textures people actually check: middling boards, connected boards with straight draws, and to a lesser extent Broadway boards.

**Why.** Preparation time should follow how often a spot occurs against your pool, not just in theory. Most players c-bet ace-high and high-card flops almost automatically in 3-bet pots, so being checked to there is rare. Mid and coordinated boards are where they lose confidence and check, so your plan for betting into a check needs to be sharpest there. Monotone boards also get checked a lot but are worth less study time because they are dealt less often.

**Common mistake.** Building a detailed plan for being checked to on A-K-x in a 3-bet pot, a spot that practically never happens against most opponents.

**Numbers.** Recommended OOP 3-bettor flop check frequency: about 50%

**Hooks.** _They checked the flop in a 3-bet pot. Which boards matter?_ · _Study the checks that happen, not the ones in theory._ · _Why mid boards get checked and high boards don't._

Review: [ ]

### Ace or king high with no Broadway connection is still a range-bet for the 3-bettor
`c-cash-6max-gp36-disconnected-ak-high-range-bet-002` · intermediate · flop · 3bet-pot · oop · consensus 0.50 · sources: rio · **draft**

**Claim.** Flops like A-8-x or K-7-x, where the middle card does not connect to Broadway, remain high-frequency small-bet textures for the 3-bettor even in wide-range 3-bet pots. Paired boards behave the same way.

**Why.** The 3-bettor's range is heavy in big aces and big kings and light in middling connectors, so a single high card with disconnected low cards gives them a large share of top pairs while the caller's suited connectors and small pairs miss. Once the other two cards start connecting to Broadway (K-Q-x, A-J-T), the caller's broadway hands make pairs, draws and two-pair combos that erase the 3-bettor's edge, so those boards shift toward checking and polarized sizing. Lack of connectivity is the feature that makes the texture good for the aggressor.

**Common mistake.** Treating every ace-high board the same way instead of separating A-8-3 from A-J-T.

**Hooks.** _A-8-3 and A-J-T are not the same flop for a 3-bettor._ · _The flop feature that decides whether you range bet._ · _Why disconnected high cards are the 3-bettor's best friend._

Review: [ ]

### Define a "low paired" board by where offsuit hands stop making trips
`c-cash-6max-gp36-low-paired-defined-by-offsuit-trips-004` · advanced · flop · 3bet-pot · oop · consensus 0.50 · sources: rio · **draft**

**Claim.** In 3-bet pots, treat paired boards of 9-9-x and lower as one category and T-T-x and higher as another. The dividing line is the rank at which the caller's range stops playing the offsuit versions of that card at full frequency.

**Why.** Board categories should follow how the opponent's range interacts with the texture, and offsuit combos are what decide whether an interaction is a big part of a range or a sliver. A caller against a 3-bet continues almost all offsuit tens and up, so on T-T-x or higher they hold many trips combos and the 3-bettor must respect that. On 9-9-x and below the caller mostly needs suited hands to hold trips, which is a much smaller slice, so the 3-bettor can bet the whole range. This principle, counting where offsuit combos hit, is the general tool for drawing lines between board classes.

**Common mistake.** Lumping all paired boards together, or splitting them by gut feel rather than by what the calling range actually holds.

**Hooks.** _9-9-x and T-T-x are different flops. Here's the line._ · _One question defines every board category: do offsuit hands hit?_ · _Why trips are rarer than you think on low paired boards._

Review: [ ]

### Stress-test a board category by changing one feature at a time
`c-cash-6max-gp36-stress-test-board-categories-013` · advanced · flop · 3bet-pot · oop · consensus 0.50 · sources: rio · **draft**

**Claim.** Before trusting a board category, vary a single property (add a flush draw, a wheel draw, a second straight, a high card) and compare the strategies. Split the category only when the EV difference between the variants is material, not when the solver's preferred size merely shifts.

**Why.** Categories exist to make the game playable, so they should be as broad as the strategy allows. On low three-card boards, adding a wheel draw moves the preferred size from an overbet toward three-quarter pot, but the EV gap between the two is around a hundredth of a big blind and both range-bet and range-check remain cheap. That is a change in flavour, not a new category. A category should be broken off only when one variant genuinely demands a different plan, otherwise you end up with texture descriptions so fine-grained that you cannot recall them under pressure.

**Common mistake.** Creating a new board category every time a sim shows a different size, until the plan has more textures than anyone can remember.

**Hooks.** _Your board categories are probably too many._ · _One cheap test tells you whether a flop needs its own rule._ · _When does a wheel draw change the plan? Usually never._

Review: [ ]

### Never overbet a monotone flop; bet small instead
`c-cash-6max-tc13-never-overbet-monotone-005` · intermediate · flop · srp · btn · consensus 0.50 · sources: 2cc · **draft**

**Claim.** On any flop where all three cards share a suit, the button's single best c-bet size is the small one. No monotone flop in the sample wants an overbet, regardless of how high the cards are.

**Why.** The overbet is powered by the button's overpair and overcard advantage. On a monotone board both players hold made flushes and strong flush draws, and those hands beat every overpair and every top pair. The edge the button normally has in the high-card region is irrelevant when a big part of both ranges already has something better than a pair. A small bet denies some equity, keeps the pot small when behind, and does not commit a lot with hands that are vulnerable to a fourth suited card.

**Common mistake.** Applying the 'high board equals overbet' rule mechanically and overbetting a KQ3 flop that happens to be all one suit.

**Numbers.** Zero monotone flops in the 102-flop sample choose the 116% overbet · Monotone flops default to the ~33% c-bet

**Hooks.** _Three spades on the flop? Put the overbet away._ · _'High board, big bet' is a lie on monotone flops._ · _One texture breaks every sizing rule you know._

Review: [ ]

### Check more on monotone flops because the caller's range is more suited than yours
`c-cash-6max-tc15-monotone-bb-more-flushes-003` · intermediate · flop · srp · btn · consensus 0.50 · sources: 2cc · **draft**

**Claim.** On a three-suit flop the big blind holds a higher share of flushes than the button, so the nut advantage flips to the caller and the button's c-bet frequency should drop sharply.

**Why.** What matters is the proportion of suited hands inside each range, not the raw count. The button's opening range includes many offsuit broadways and offsuit aces, so its suited region is a smaller slice of the whole. The big blind's calling range is built heavily from suited hands - suited connectors, suited gappers, weak suited aces and kings - while many of its offsuit hands fold or three-bet. A monotone board therefore gives the big blind relatively more made flushes, and the player with more nuts is the one who wants to bet. For the button that is a reason to check back a lot.

**Common mistake.** Treating a monotone flop like any other high-card flop and continuation betting at the same rate.

**Hooks.** _Three spades flop. The big blind has more flushes than you._ · _Why the caller owns monotone boards._ · _Checking back on monotone flops makes you more money._

Review: [ ]


## blockers  (5)

### The worst turn bluff blocks their folds and unblocks their calls
`c-cash-6max-cc07-worst-bluff-blocks-their-folds-014` · intermediate · turn · srp · ip · consensus 0.50 · sources: cc · **draft**

**Claim.** In a neutral or unfavourable turn world, pick bluffs that interfere with hands that continue and leave their folding hands intact. A hand with no draw, no overcard, no flush-suit blocker and cards that only hit their weak pairs is the worst possible bluff.

**Why.** Imagine a jack-high board with two flush draws on the turn and you hold 9-7 offsuit with neither suit. You cannot improve to beat a jack. You hold no card of either flush suit, so every draw that would raise or call you is fully live in their range. And your nine and seven are exactly the cards in their hands that would fold, like 9-9 under the jack or A-9 high; you want them to hold those, and you are making it less likely. Compare a hand like K-8 with one flush card: it blocks some continuing draws and has an overcard to hit, so although still "trash", it is a far more acceptable bluff. In a very favourable world none of this matters, but when fold equity is tight, blocker quality is what separates allowed bluffs from losing ones.

**Common mistake.** Choosing turn bluffs by how "bad" the hand looks ("I have nothing, so I might as well bluff") instead of by what the cards block.

**Hooks.** _'I have nothing, so I'll bluff' is backwards._ · _The worst bluff in poker looks exactly like this._ · _Your bluff should block calls, not folds._

Review: [ ]

### Prefer the backdoor flush draw when choosing which marginal hand raises or continues
`c-cash-6max-gp35-backdoor-suit-for-aggression-014` · intermediate · flop · 3bet-pot · ip · consensus 0.50 · sources: rio · **draft**

**Claim.** Among two otherwise similar marginal hands in a 3-bet pot, the one holding a card in the board's suit is the one to raise, bet or continue with. Without the backdoor, the same hand drops to a call or a fold.

**Why.** A backdoor flush draw adds turn cards that let you keep barrelling or continue, which is what makes an aggressive line with a weak hand profitable. It also affects the raise-or-call line facing a small c-bet: a gutshot with the suit is a frequent raise, the same gutshot without it is a call. The coach found his biggest trainer mistakes, both betting and calling, came from taking aggressive actions with the non-suited version of a hand. Make the suit check a habit before pulling the trigger on a marginal play.

**Common mistake.** Treating the two offsuit and suited-in-the-wrong-suit versions of a hand as identical when choosing bluffs and raises.

**Hooks.** _Same hand, one suit different, opposite action._ · _The backdoor check that decides raise or fold._ · _Why your bluff needs a flush card you don't have yet._

Review: [ ]

### A4 is a 3-bet candidate on 774 because both cards block the nuts
`c-cash-6max-tc18-a4-double-blocker-3bet-004` · advanced · flop · srp · btn · consensus 0.50 · sources: 2cc · **draft**

**Claim.** Facing a check-raise on 774 from a typical big blind, re-raise second pair with an ace kicker far more than theory, around 15% instead of under 6%.

**Why.** The four blocks pocket fours and 74, which are the full houses the big blind can show up with. The ace blocks A7, the trips combo a real big blind check-raises much more often than the solver would. Holding both cards shrinks the strongest part of the raising range, which means the raise is more often a draw or a low-pair protection raise, and a 3-bet makes those hands fold or continue as underdogs.

**Numbers.** A4 3-bet ~15% vs <6% GTO

**Hooks.** _Second pair re-raises a check-raise. Blockers explain it._ · _A4 on 774: the hand that blocks everything scary._ · _Why the ace matters more than the four here._

Review: [ ]

### Bottom pair always continues vs a K72 check-raise, low pocket pairs barely do
`c-cash-6max-tc33-bottom-pair-blocker-vs-low-pairs-003` · advanced · flop · srp · btn · consensus 0.50 · sources: 2cc · **draft**

**Claim.** Facing a typical big blind's check-raise on K72, always continue with 2x and occasionally 3-bet it, but fold 33 through 66 without a flush-suit card and continue only about half the time with one.

**Why.** A deuce in your hand blocks pocket deuces and K2, a meaningful part of a check-raising range that is heavier in sets and two pair than theory. Fewer nut combos for the opponent means your bottom pair is relatively better and your occasional raise is more credible. A low pocket pair blocks nothing of the sort and loses to every pair on the board, so it needs the extra equity of a suited card to keep going. In theory those pairs always call; against the stronger real range they cannot.

**Hooks.** _Bottom pair beats pocket fives here. Blockers, not strength._ · _Why a deuce in your hand changes a fold into a call._ · _Pocket sixes on K72: fold to the raise more than you think._

Review: [ ]

### Second pair 3-bets more on K72, best in the suits that unblock their folds
`c-cash-6max-tc33-second-pair-3bet-unblock-004` · advanced · flop · srp · btn · consensus 0.50 · sources: 2cc · **draft**

**Claim.** Against a typical big blind's check-raise on K72, re-raise second pair hands like Q7, 87 and 72 about 9% of the time versus under 3% in theory, and prefer the combos without a card of the flush suit.

**Why.** Holding a seven blocks pocket sevens and K7, two of the strongest hands in a check-raising range that has grown more set- and two-pair-heavy. Suits work the other way. The big blind still check-raises some backdoor flush hands in the second suit, such as 98, and folds them to a 3-bet, so you want to leave those in their range. A seven paired with a club or diamond unblocks all of those raise-fold hands, which is what makes the re-raise profitable.

**Numbers.** second pair 3-bet ~9% vs <3% GTO

**Hooks.** _Second pair re-raising a check-raise. Three times more often._ · _The suit that makes your 3-bet work: not the flush suit._ · _Unblock their folds. That is the whole idea._

Review: [ ]


## multiway  (1)

### Do not auto c-bet a missed flop into three or more callers
`c-cash-6max-br1-no-cbet-into-many-callers-010` · beginner · flop · multiway · any · consensus 0.50 · sources: br79 · **draft**

**Claim.** When your open gets called in several places and you miss, check instead of firing a continuation bet, even on a board that looks good for you. With that many opponents, at least one usually holds a pocket pair or a piece they will not fold.

**Why.** A c-bet with nothing needs everyone to fold. Each extra caller multiplies the chance that someone has connected or holds a stubborn hand like pocket eights that beats your unpaired overcards and never goes away at these stakes. The fold-everyone outcome becomes rare, so the bet mostly builds a pot you are losing. Save the aggression for heads-up pots where one fold is all you need.

**Common mistake.** Treating "I was the preflop raiser" as a reason to bet regardless of how many people are in the hand.

**Hooks.** _Four callers, no pair, and you still c-bet? Stop._ · _Somebody always has pocket eights. Plan for it._ · _Multiway c-bets at NL2 are a slow leak._

Review: [ ]


## bankroll-moving-up  (1)

### Always buy in for the table maximum so you cover the weak players
`c-cash-6max-br4-buy-in-max-002` · beginner · any · consensus 0.50 · sources: br79 · **draft**

**Claim.** Buy in for the largest amount the table allows, for example 250 big blinds where that is the cap, even if nobody else has that much yet. Your goal is to cover any recreational player who sits down, so that when they make a big mistake you win all of it.

**Why.** The money you win from a weak player is limited by the smaller of the two stacks. If they sit with 150 big blinds and you have 100, the extra 50 they are willing to lose goes to someone else. Deep stacks also increase the value of position and postflop skill, which is exactly where your edge over this type is largest. The only requirement is a bankroll that comfortably supports the bigger buy-in.

**Common mistake.** Buying in for 100 big blinds at a deep table out of habit and getting outstacked by the fish.

**Numbers.** Buy in for the table max, e.g. 250bb where allowed

**Hooks.** _Buying in short is leaving the fish's money for someone else._ · _Why 250 big blinds beats 100 at the micros._ · _Cover the table. Every time._

Review: [ ]


## mental-game  (7)

### When a regular 3-bets you, let it go and refocus on the weak player
`c-cash-6max-br1-why-are-you-in-this-spot-011` · beginner · preflop · any · consensus 0.50 · sources: br79 · **draft**

**Claim.** If a competent regular re-raises you, fold marginal hands without a fight and do not start 4-betting light to prove a point. You are at the table for the weak player; a war with a regular is a distraction with little profit in it.

**Why.** Getting into a 3-bet and 4-bet battle with another thinking player is high variance for a small edge at best. Meanwhile the real source of your win rate, the recreational player two seats away, is being ignored. Each marginal confrontation also risks tilt, and tilt leaks into the hands that actually matter. Fold, keep your image calm and wait for the spots where the money is easy.

**Common mistake.** Asking "he has 3-bet me three times, should I 4-bet A3 suited?" instead of asking why you are tangling with him at all.

**Hooks.** _The reg 3-bet you again. The right answer is boring._ · _Fighting regulars is an ego expense, not a strategy._ · _Ask yourself what put you in this spot at all._

Review: [ ]

### Being willing to look weak is a profit skill
`c-cash-6max-br2-ego-off-the-table-011` · beginner · any · consensus 0.50 · sources: br79 · **draft**

**Claim.** Fold marginal hands to aggression from regulars and let them win small pots without worrying about your image. The only score that matters is your bottom line, and the big pots against weak players are where that score is decided.

**Why.** A lot of money at micro stakes is lost in spots where a player "has had enough" of being pushed around and makes a stand with a mediocre hand. That is ego, not strategy. Against a weak player you know a top pair hand is coming that will win their stack, so there is no reason to fight over bottom pair now. Keeping decisions simple and ego-free also keeps you off tilt, which protects every other hand you play.

**Common mistake.** Calling down a regular with middle pair to show you cannot be bluffed.

**Hooks.** _Looking weak is free. Proving a point costs a stack._ · _The most profitable players are fine with being pushed around._ · _Your image does not pay the bills. Your win rate does._

Review: [ ]

### Skip the pre-action buttons and make every decision when it is your turn
`c-cash-6max-br2-no-auto-buttons-012` · beginner · any · consensus 0.50 · sources: br79 · **needs-review** · review note: _Not poker strategy; low value._

**Claim.** Do not use check-fold or call-any buttons before the action reaches you, even when you already know what you will do. Deciding in the moment keeps you engaged and avoids giving away information through instant actions.

**Why.** Pre-selected actions lock in a decision before you have seen what happens in front of you, and a sudden raise or an unexpected caller can make the planned action wrong. They also make you predictable: a player who always folds instantly to raises is recognizably on autopilot, and observant opponents will pressure them more. Clicking the real button each time costs a second and keeps the habit of thinking through every spot.

**Common mistake.** Pre-checking "fold to any raise" with a hand that would have been a profitable call once a weak player enters the pot.

**Hooks.** _The auto-fold button is a small leak you can fix today._ · _Instant actions tell the table you are not paying attention._ · _One click habit that keeps you sharp over four tables._

Review: [ ]

### Treat opponents as one pool, not as individuals who owe you money
`c-cash-6max-br2-one-blob-of-players-010` · beginner · any · consensus 0.50 · sources: br79 · **draft**

**Claim.** When a player wins a pot off you and leaves, or sucks out and quits, do not take it personally or chase them. Think of every opponent as part of one large player pool; what one of them takes with luck, the next one gives back over the long run.

**Why.** Getting "hit and run" feels unfair, but nothing about your expected value changed. The same mistakes that made the pot profitable to play will be made by the next weak player who sits down. Fixating on one opponent leads to playing hands you should not, staying at tables you should leave and tilting money away elsewhere. Viewing the field as a blob removes the emotional charge and keeps your decisions tied to profit.

**Common mistake.** Posting angry forum threads about a hit-and-run instead of opening the next table.

**Hooks.** _He hit and ran you. Who cares? Here is the healthier view._ · _Nobody owes you a rematch. The pool pays you back._ · _Tilt starts the moment you take one player personally._

Review: [ ]

### Avoid marginal big pots partly to protect yourself from tilt
`c-cash-6max-br3-tilt-collateral-damage-003` · beginner · any · consensus 0.50 · sources: br79 · **draft**

**Claim.** At stakes full of weak players, do not put a lot of money into close, marginal spots. Beyond the direct cost, losing several of those pots tilts you, and the money thrown away afterward is often bigger than the pots themselves.

**Why.** Tilt has collateral damage: a lost coin flip against a regular does not just cost that pot, it degrades your decisions in the next hour of hands against the players who actually pay you. When easy profit is available from recreational players, the small theoretical edge in a marginal spot is not worth the emotional risk. A relaxed, low-variance style keeps your head clear for the spots that matter and keeps you in the session longer.

**Common mistake.** Taking every thin edge against regulars, then playing the next twenty hands on tilt.

**Hooks.** _The real cost of a lost coin flip is the next hour._ · _Thin edges have a hidden price. It is called tilt._ · _Why relaxed players beat the micros._

Review: [ ]

### The core plan is the same at every stake: find the fish, get position, play them
`c-cash-6max-br4-same-strategy-every-stake-014` · beginner · any · consensus 0.50 · sources: br79 · **draft**

**Claim.** Moving from one limit to the next changes how often you find very weak players, not what you should be doing. At any stake the job is to find recreational players, sit with position on them, play as many hands against them as possible and avoid tables of regulars.

**Why.** The lowest stakes are a circus where almost any aggressive, value-heavy strategy wins. One limit up the games already play more like the stakes above them, with fewer wild players and more table hopping needed, especially early in a session. What does not change is the source of profit: other players' mistakes, delivered to you by position. Sitting at a table full of competent players for the ego boost of beating them is far less profitable than it feels.

**Common mistake.** Treating a move up as a reason to play a fancier style instead of a reason to table-select harder.

**Hooks.** _Moving up changes the fish count, not the plan._ · _The strategy that works from NL2 to NL5000._ · _Beating a reg table is an ego boost, not a profit plan._

Review: [ ]

### Never bet to fix your red line or check to feel less spewy
`c-cash-6max-cc03-red-line-trap-012` · beginner · multi-street · consensus 0.50 · sources: cc · **draft**

**Claim.** Do not adjust your aggression in general. Fix the specific spot. Betting more "to be more aggressive" or checking more "to be less spewy" are both ways of avoiding the real question, which is whether this bet beats this check.

**Why.** A falling non-showdown line usually means you are missing mandatory bluffs, and that diagnosis is often correct. The wrong cure is to start betting randomly, because any fold equity will lift the red line while the showdown line drops by more, so the total graph gets worse. Labels like "too nitty" or "too aggro" operate at the level of whole frequencies and let you dodge engaging with the hand in front of you. Every decision is a comparison of two EVs in one spot, and no global adjustment can replace that.

**Common mistake.** Firing a river bet with a hand that has decent showdown value because the graph looked passive, then losing more at showdown than the bluffs gain.

**Hooks.** _Chasing a pretty red line costs you the green one._ · _'I need to be more aggressive' is not a plan._ · _Your red line is a symptom. Don't treat the symptom._

Review: [ ]


## study-methods  (30)

### Fewer tables means a higher win rate because you catch what the HUD misses
`c-cash-6max-br3-fewer-tables-011` · beginner · any · consensus 0.50 · sources: br79 · **draft**

**Claim.** Playing two to six tables lets you notice things like a player open-shoving two hands in a row or a fish about to rebuy. Those observations are worth real money and vanish at 18 or 24 tables, so expect a far better per-table win rate when you play fewer.

**Why.** HUD stats are slow to converge and never record context such as who just bought in short, who is tilting or who shoved the last two hands. With a handful of tables you keep that context in the corner of your eye and act on it immediately, for example calling an open-shover with a medium hand you would otherwise fold. Mass multi-tabling trades all of that for volume, and in today's games the trade is often a bad one.

**Common mistake.** Adding tables to "make up for" a low win rate, which lowers the win rate further.

**Numbers.** Coach recommends 2-6 tables over 18+ for win rate

**Hooks.** _Sixteen tables cost more win rate than you think._ · _Four tables saw the open-shover. Twenty would have missed him._ · _More tables, less money. Here is the trap._

Review: [ ]

### Read won-money-at-showdown to separate running bad from playing bad
`c-cash-6max-br6-won-money-at-showdown-as-variance-gauge-010` · beginner · any · consensus 0.50 · sources: br79 · **draft**

**Claim.** Won money at showdown (W$SD) should sit above 50% over any decent sample, typically closer to 55%. If it is in the 40s you are almost certainly running bad rather than playing badly. Treat the all-in EV graph with some caution: it does not capture coolers and set-over-set spots.

**Why.** After a losing session the hard question is whether you made mistakes or got unlucky. W$SD answers it quickly: it measures how often you had the best hand when the cards were turned over, which over a few hundred hands is dominated by run-outs rather than decisions. A number far below your norm points to variance, not leaks. The all-in EV line is a popular alternative but only counts hands that went all in before the river, so it ignores the many ways to run bad without an all-in.

**Common mistake.** Tearing up a sound strategy after a losing session without checking whether the showdown numbers simply show a bad run.

**Numbers.** W$SD should be above 50%, usually ~55% · W$SD in the 40s or lower signals running bad

**Hooks.** _One stat tells you if you ran bad or played bad._ · _Before you blame your strategy, check this number._ · _Your all-in EV graph is lying to you a little._

Review: [ ]

### Guess the equity before you look it up, every time
`c-cash-6max-cc03-calibrate-equity-guesses-021` · beginner · multi-street · consensus 0.50 · sources: cc · **draft**

**Claim.** To get good at estimating equity after a bet is called, commit to a number before opening the solver or equity calculator, then check and recalibrate. Repeating guess-check-adjust trains the intuition; reading the answer first trains nothing.

**Why.** Equity estimation is a motor skill like throwing a ball into a bucket: you improve through feedback on your own attempts, not by studying the physics. Players who write down a guess and then see they were ten points low learn why (for example, they forgot that the opponent must call many unpaired hands on a dry board). Doing it with a study group, where one person sets a texture and action sequence and the others guess the landing equity, makes it social and sticks better. Trying to memorise solver outputs without this step does not transfer to the table.

**Common mistake.** Opening the solver, nodding at the numbers, and never testing whether you could have produced them yourself.

**Hooks.** _Study tip: guess first, then look. Always._ · _You can't learn to throw by reading about physics._ · _Memorising solver outputs doesn't work. This does._

Review: [ ]

### Use a randomizer only for spots you know are a true mix
`c-cash-6max-cc07-rng-only-when-indifferent-019` · intermediate · multi-street · consensus 0.50 · sources: cc · **draft**

**Claim.** Randomize between bet and check only when you are confident the two actions have the same EV. If a hand is a clear check, a high RNG roll does not make betting right. And when you have a read, skip the randomizer and take the exploitative line.

**Why.** Mixing exists because some hands are genuinely indifferent in equilibrium, and a randomizer is the least stressful way to execute that without leaking patterns. The danger for developing players is using it before they know which spots are indifferent: rolling a 94 and betting a hand that loses significant EV when bet turns a tool into a blunder generator. So learn the thresholds first, randomize second. Also remember that equilibrium mixing is only the default. Against a station you simply value bet; against someone who overbluffs when checked to you simply check. Live, randomizing is rarely needed at all because reads are so plentiful. A HUD-based RNG is far more pleasant than opening a web page every hand.

**Common mistake.** Treating "the solver mixes here" as permission to let a random number choose, even in spots where one option is clearly better for the specific hand or opponent.

**Hooks.** _Your randomizer is making you worse. Here's when._ · _Rolling a 94 does not make a bad bet good._ · _Mix only when it's actually a mix._

Review: [ ]

### A solver picking one size does not mean your other size is wrong
`c-cash-6max-cc07-solver-sizing-is-not-a-verdict-002` · intermediate · multi-street · consensus 0.50 · sources: cc · **draft**

**Claim.** When a solver output shows a single sizing used at full frequency, do not conclude that a different sizing is a mistake. Compare the EVs of the two options; if they are within a fraction of a percent of the pot, both are fine.

**Why.** Any solver output is an approximation built from the limited sizes you gave it and the time you let it run. Stop it a minute later and it may flip from one size to another, because the two are nearly equal and it simply picks whichever is microscopically ahead at that moment. It never flips between a terrible option and a good one, so a hard switch between sizes is itself a sign that they were close. Treat the solver's colours as a hint and the EV numbers as the evidence. Forcing it to use a different size and seeing EV barely move proves the simplification is safe; forcing it to check its whole range or fold draws, by contrast, shows large losses.

**Common mistake.** Seeing an all-overbet turn node and panicking that your 75% bet has been losing money all along, instead of checking how much EV the two sizes actually differ by.

**Hooks.** _The solver overbets 100% here. That proves less than you think._ · _Stop reading solver colours. Read the EV._ · _'The solver only uses one size' is a trap._

Review: [ ]

### Aggregate solver reports work for the flop c-bet node but break down from the turn on
`c-cash-6max-gp23-aggregate-reports-flop-only-017` · advanced · multi-street · srp · consensus 0.50 · sources: rio · **draft**

**Claim.** Use aggregate multi-board reports to build flop c-bet and facing-c-bet categories, but switch to individual sims once you move to turn decisions. One node deeper the branches multiply and the report averages over bet-size sequences that would not actually happen on many of the boards.

**Why.** An aggregate report answers one question across hundreds of flops at once, which is exactly what you need to find texture groups. But it only works when the preceding action is identical, and each bet size you face needs its own report. By the turn the sequence depends on which flop size was used, which on a given texture may be rare or never chosen, so the averaged numbers describe lines that do not occur. At that depth, a few representative single-board sims per category teach more than a report that blends unrealistic lines.

**Common mistake.** Drawing turn barrel frequencies from an aggregate report that lumps together flop sizes the solver would never pick on that board.

**Hooks.** _Aggregate reports lie about the turn. Here is why._ · _Works on the flop, fails on the turn: aggregate reports._ · _Why your turn frequencies from reports are wrong._

Review: [ ]

### When you check a c-bet stat, also check how you respond to what comes next
`c-cash-6max-gp23-benchmark-next-node-009` · intermediate · multi-street · srp · ip · consensus 0.50 · sources: rio · **draft**

**Claim.** Comparing your tracker stats to solver benchmarks should cover both the action and the follow-up: flop c-bet frequency alongside fold-to-flop-check-raise, and flop check-back alongside fold-to-turn-probe. Then write down which of the two needs work before you open a sim.

**Why.** Strategy errors cascade. If your c-bet frequency is too high, the extra bets are weak hands that then fold too often to a check-raise, so both stats drift at once. If you only fix the headline number you leave the downstream leak in place. Looking at the pair tells you what kind of hands are wrong: too many thin value bets getting raised off their equity, or too many air bets that should have been check-backs. That diagnosis is what makes the following solver session targeted instead of a general browse.

**Common mistake.** Checking only "c-bet flop %" against a target number and declaring the spot fixed.

**Hooks.** _Your c-bet stat is fine. Your fold-to-raise stat is not._ · _One number tells you whether your c-bets are too thin._ · _Fixing one stat without the next one fixes nothing._

Review: [ ]

### Rank spots to study by how often they occur and how much they move your win rate
`c-cash-6max-gp23-study-priority-008` · intermediate · flop · srp · consensus 0.50 · sources: rio · **draft**

**Claim.** Give every node in your game plan a priority based on frequency and win-rate impact, and spend study time accordingly. The in-position flop c-bet in single raised pots is high priority on every texture; rare textures like monotone or trips flops drop in priority only in more specific scenarios.

**Why.** Study time is finite, and the biggest gains come from the most common decision points. The first-to-act flop decision as the raiser happens in a large share of all hands you play, so even a small mistake there compounds across thousands of hands. Monotone boards are dealt rarely, so a mistake there costs little in total even if it is large in isolation. Writing the priority next to each spot tells you where to start and when a spot is good enough to leave alone.

**Common mistake.** Spending hours on an exotic monotone turn spot while your basic flop c-bet frequencies are far from any benchmark.

**Hooks.** _Most players study the wrong spots. Here is the order._ · _The spot that decides your win rate is the boring one._ · _Stop studying monotone boards until you fix this._

Review: [ ]

### For rare textures like monotone flops, learn the basics once and deliberately oversimplify
`c-cash-6max-gp30-rare-spot-study-budget-011` · intermediate · flop · srp · consensus 0.50 · sources: rio · **draft**

**Claim.** Spend only enough study time on low-frequency spots to extract two or three rules of thumb against the bet size you most often face, then move on. Do not chase every nuance of monotone or trips boards; accept that an oversimplified plan is correct for how rarely they occur.

**Why.** Monotone flops are dealt so rarely that even playing them slightly wrong costs little over a year, while the variations between different monotone boards would take years of play to encounter. Every hour spent there is an hour not spent on the single raised pot c-bet and defense nodes that occur constantly. The right amount of effort is to open a few sims, write a broad rule such as "any suit card continues versus a small bet", note the hands that raise or float without a suit card, and stop. The goal is to avoid being lost in the spot, not to master it.

**Common mistake.** Treating every spot as equally worth solving and spending a study session on a texture you will see twice a month.

**Hooks.** _Monotone boards: study them for 20 minutes, then stop._ · _The spots you should deliberately play 'wrong'._ · _Perfectionism on rare flops is a study leak._

Review: [ ]

### Write each flop defense threshold as a short hand-class phrase you can recall in game
`c-cash-6max-gp30-short-threshold-notes-005` · intermediate · flop · srp · oop · consensus 0.50 · sources: rio · **draft**

**Claim.** After studying a texture, compress the folding threshold into a few words that name the strongest hand class that still folds sometimes, for example "queen-high with backdoors and worse" on low paired boards versus a small bet, or "king-high with an overcard and a backdoor flush draw" on high paired boards. Ignore the combo-by-combo exceptions.

**Why.** A sim shows dozens of mixed combos where this gutshot calls and that one folds, this bottom pair continues and that middle pair does not. None of that is processable in real time. What transfers is the general quality that separates continues from folds, and a phrase short enough for a flash card is what you will actually remember. Getting a borderline combo wrong, say continuing a king-ten instead of a suited king-seven, costs almost nothing. Missing the whole hand class costs a lot. Exposure to many sims is what lets you write the phrase with confidence.

**Common mistake.** Writing a paragraph per board with every exception, then remembering none of it when the hand actually comes up.

**Hooks.** _Your flop defense plan should fit on a flash card._ · _Stop memorizing combos. Memorize one phrase per board._ · _The borderline combo does not matter. The hand class does._

Review: [ ]

### Plug the flop leak before worrying about the turns and rivers it creates
`c-cash-6max-gp31-fix-earlier-street-first-001` · intermediate · flop · srp · any · consensus 0.50 · sources: rio · **draft**

**Claim.** When your stats show you check-raise or defend too little on the flop, raise that frequency first. Do not hold back because you are unsure how you will handle the new turn and river spots that follow.

**Why.** The flop decision comes up far more often than any branch after it, so that is where opponents are taking the most from you. Playing it more aggressively will land you in unfamiliar later-street spots and you will make some mistakes there, but those are smaller and rarer than the one you are already making every orbit. Work from the earliest street forward. Later nodes can get their own drills once you actually reach them in volume.

**Common mistake.** Keeping a passive flop strategy because the aggressive version feels uncomfortable on later streets.

**Hooks.** _Scared to check-raise more? That fear is the leak._ · _Fix the flop first. The river can wait._ · _Most NL10 players fix leaks in the wrong order._

Review: [ ]

### When drilling a frequency leak, force the missing action on every plausible hand
`c-cash-6max-gp31-force-the-action-you-lack-003` · intermediate · flop · srp · bb · consensus 0.50 · sources: rio · **draft**

**Claim.** If you know you check-raise too little, take the raise with every hand that looks like a candidate during the drill and let the trainer tell you when it was wrong. Keep leaning that way until the feedback starts marking you as too aggressive.

**Why.** Your instinct is already biased toward the passive option, so playing "what feels right" in the drill just reproduces the leak. Deliberately overshooting exposes the hand classes you have been missing and recalibrates your sense of what qualifies. The same logic applies in reverse: someone who raises too much should call or fold every mixed hand. The goal is to overcorrect until mistakes appear on the other side, then settle in the middle.

**Common mistake.** Playing the drill to get a high score, which only confirms habits instead of changing them.

**Hooks.** _Train to be wrong on purpose. Here's why it works._ · _Your gut says call. Raise anyway, then check the answer._ · _Overcorrect first. Fine-tune later._

Review: [ ]

### The goal of a check-raise drill is finding zero-EV raises, not avoiding blunders
`c-cash-6max-gp31-neutral-ev-raises-not-blunders-004` · intermediate · flop · srp · bb · consensus 0.50 · sources: rio · **draft**

**Claim.** In a frequency drill, a small negative EV mark on a raise that the solver mixes is a good result. You are hunting for the indifferent raises you never take in game, so avoiding every red mark means you are still too passive.

**Why.** Many flop check-raises are near-indifferent between calling and raising. If you never raise those hands, your frequency collapses and opponents can c-bet small with impunity. A trainer that flags a tiny EV loss on a hand that raises 50-60% of the time is confirming that the hand belongs in your raising range some of the time. Fixating on a clean score shifts your attention from the frequency problem you came to solve.

**Common mistake.** Treating every highlighted mistake as equal, then retreating to the safe passive play after the first red mark.

**Hooks.** _A red mark in the trainer can be good news._ · _Zero-EV raises are the ones you keep missing._ · _Stop chasing a perfect trainer score._

Review: [ ]

### Watch the trainer's showdown hands to learn the opponent's side of the node
`c-cash-6max-gp31-study-both-sides-of-node-013` · intermediate · flop · srp · any · consensus 0.50 · sources: rio · **draft**

**Claim.** When a trainer deals the opponent's holding from the solver's own range, pay attention to those showdowns. They show you what a correct check-raising or betting range looks like in that spot, so you learn both sides of the decision at once.

**Why.** Knowing your own action is only half of the spot. Seeing which hands the solver check-raises, floats or gives up with builds an accurate picture of the range you are facing, which is what makes your calls and folds feel justified rather than forced. It also helps you spot which hand classes you are missing from your own aggressive ranges. Since the showdowns are solver-driven rather than random, they are a reliable sample of correct play.

**Common mistake.** Clicking through the opponent's revealed hands without noting what they say about the raising range.

**Hooks.** _Your opponent's cards in the trainer are a free lesson._ · _Study both seats at once. Here's how._ · _What does a correct check-raising range look like? Watch._

Review: [ ]

### Give the most frequent spots the most drilling time, even when they feel basic
`c-cash-6max-gp31-train-most-frequent-spots-002` · intermediate · flop · srp · ip · consensus 0.50 · sources: rio · **draft**

**Claim.** Rank your training drills by how often the spot occurs. The in-position flop c-bet decision in a single-raised pot deserves a permanent place in your routine; a rare branch like facing a check-raise after a 75% c-bet gets a few minutes at most.

**Why.** Edge is frequency times EV gain. A fundamental spot you see every session, even with a small per-hand improvement, outweighs a flashy rare node where you might be badly off. Frequency leaks are also slow to move, so they need repeated sessions over months rather than one study block. Treat the common spots as the core of a recurring routine and let everything else be secondary.

**Common mistake.** Spending study time on exotic deep-tree spots because they are interesting, while the everyday c-bet decision stays unexamined.

**Hooks.** _The boring spot is the one making you money._ · _Study time should follow frequency, not curiosity._ · _You drill rivers. The flop is where you lose._

Review: [ ]

### Say how confident you are before the trainer reveals the answer
`c-cash-6max-gp31-verbalize-before-answer-012` · intermediate · multi-street · srp · any · consensus 0.50 · sources: rio · **draft**

**Claim.** Before each decision in a drill, state out loud whether you think it is clear, close, or a stretch. Then compare with the solution. A "clearly too loose" that turns out fine, or a "close" that turns out pure, is the feedback that moves your game.

**Why.** Drills are not about the score; they are about calibrating your internal read of a spot to the solution. If you only look at right or wrong, you miss the information in how sure you were. Verbalizing forces you to commit to a judgment, which makes it obvious afterward when your confidence was misplaced in either direction. It also helps you notice systematic patterns, like always feeling that correct calls are too loose.

**Common mistake.** Looking at the answer and thinking "yes, I knew that", when you had not actually decided.

**Hooks.** _Talk to your solver. Out loud. Seriously._ · _Right answer, wrong confidence. Still a mistake._ · _The drill habit that actually changes how you play._

Review: [ ]

### Drill river thresholds first; sizing and blocker details come later
`c-cash-6max-gp32-distribution-before-sizing-008` · intermediate · river · srp · ip · consensus 0.50 · sources: rio · **draft**

**Claim.** When training river stabs, aim first at getting the bet-or-check decision right across hand classes: not value betting too thin, not missing value, not bluffing with showdown value, not missing bluffs. Treat exact size choices and blocker nuance as a second pass.

**Why.** The largest river mistakes are frequency mistakes, like checking a whole class of thin value or bluffs. A sizing mix that is slightly off costs a fraction of a blind; a hand class that never bets costs far more. Running a fast drill with the single question "does this hand bet?" also lets you cover many textures in one session and reveals your thresholds quickly. Once the distribution is right, come back to size selection with a clear picture of which hands are betting.

**Common mistake.** Agonizing over half pot versus pot in the drill while whole hand classes are still being checked that should bet.

**Hooks.** _Stop fussing over river sizing. Fix this first._ · _Bet or check? Answer that before anything else._ · _The fast river drill that finds your thresholds._

Review: [ ]

### Skip drilling spots your strategy almost never reaches
`c-cash-6max-gp32-dont-study-unreachable-spots-010` · intermediate · river · srp · ip · consensus 0.50 · sources: rio · **draft**

**Claim.** Before studying a surprising river result, check how often your strategy actually gets there. A checked-down river on a paired board, for instance, barely exists because the in-position player bets most pairs on the flop or turn, so a strange value bet there is not worth your time.

**Why.** Trainer drills deal every possible path, including lines that are a small fraction of a small fraction of hands. Results in those lines are both rare in practice and less reliable, because solver accuracy degrades with every low-frequency branch. Spending study time on them teaches you something you will almost never use. Verify the path frequency, note it, and move on to spots that occur every session.

**Common mistake.** Deep-diving a bizarre solver play without noticing the line is taken a fraction of a percent of the time.

**Numbers.** Example: low pocket pairs bet ~74% on a paired flop, so they rarely reach a checked-down river

**Hooks.** _That weird solver play? You'll never be in that spot._ · _Study what happens, not what could happen._ · _One question before you analyze any hand._

Review: [ ]

### Find the cause of a stat deviation before you try to fix it
`c-cash-6max-gp34-diagnose-before-fixing-005` · intermediate · flop · 3bet-pot · oop · consensus 0.50 · sources: rio · **draft**

**Claim.** When a tracker stat disagrees with a solver benchmark, filter your database to that exact line, scan the hands by action, tag the ones that look off, then compare them to the closest sims you already own. Only run a custom sim when no existing one fits.

**Why.** A stat can be off for three different reasons: your strategy is deliberately different, your opponents are using sizes the aggregate did not assume, or you are misranking hands. Each has a different fix, and guessing wastes study time. Filtering to the line (3-bet preflop, check the flop, face a bet, any reaction) and sorting by what you did lets you check each bucket quickly. A rare spot with a small sample is where hand-by-hand review beats trainer drills, because you cannot trust the frequency and you need to see the individual decisions.

**Common mistake.** Reading one frequency, deciding it is a leak, and drilling the spot without ever looking at the hands that produced the number.

**Hooks.** _Your tracker says you're too loose. Prove it first._ · _Five tagged hands beat five hundred trainer reps for rare spots._ · _A study workflow for leaks with tiny samples._

Review: [ ]

### Study the counter-strategy at the same time as your own line
`c-cash-6max-gp34-study-both-sides-of-node-001` · intermediate · flop · 3bet-pot · oop · consensus 0.50 · sources: rio · **draft**

**Claim.** Whenever you build a strategy for one decision point, study the opponent's best response to it in the same session. Understanding how they should react explains why your line works and exposes problems before they show up at the table.

**Why.** A flop c-bet strategy is only half of the node. The other half is what happens when you check and the opponent bets, and what the opponent should do against your bet. Looking at both sides together links the mechanics of your strategy to the reasons it is built that way, and it keeps the next street in view while you are still deciding the current one. Out of position this matters more than in position, because your checking range has to react to a bet immediately rather than at leisure on the turn.

**Common mistake.** Memorizing c-bet frequencies for one side of the tree while having no plan for the check-call range that strategy creates.

**Hooks.** _Studying your c-bets without studying the response is half a lesson._ · _Why solver c-bet charts fail you the moment someone bets back._ · _The study habit that stops surprises on the turn._

Review: [ ]

### Work down the most frequent lines first and defer rare nodes
`c-cash-6max-gp34-study-priority-order-003` · intermediate · multi-street · 3bet-pot · any · consensus 0.50 · sources: rio · **draft**

**Claim.** Rank every decision point by how often your own strategy reaches it, study the high-frequency ones to completion, and only then return to nuances and rare branches. Nodes your plan never reaches get zero time until everything important is done.

**Why.** Study time is finite and the game tree is not. If your flop plan removes checks on a board class, every node below that check is dead for you and learning it is pure cost. The same logic applies to rare sizings and unusual runouts. A deliberately simple first decision point trims huge parts of the tree, which lets you go deep on the spots that come up every session instead of skimming everything equally.

**Common mistake.** Studying every node of a solver output with equal care, including lines the player's own strategy never takes.

**Hooks.** _Stop studying spots your own strategy never reaches._ · _The order you study poker spots in matters more than you think._ · _A simple flop plan is also a shorter study list._

Review: [ ]

### Before acting in a drill, say whether you think the hand is a pure action or a mix
`c-cash-6max-gp35-declare-pure-or-mix-018` · intermediate · flop · 3bet-pot · any · consensus 0.50 · sources: rio · **draft**

**Claim.** Commit out loud to "clear bet", "clear check" or "mixed" before the trainer shows the distribution. Being told a hand you called pure is actually 50-50 is the useful feedback; without the declaration you will just nod and believe you had it right.

**Why.** Trainers show frequencies, not just correct or incorrect. That extra information only improves your model of the spot if you had a prediction to compare it to. Declaring pure versus mix opens you up to being challenged on hands where your action matched the solver but your certainty did not. Over a session, this reveals whether you systematically see mixes as pures (too rigid) or pures as mixes (too random), which is a leak you cannot find from a score alone.

**Common mistake.** Looking at the solver grid afterward and concluding "I had the right idea" when you never committed to an idea.

**Hooks.** _Pure or mix? Say it before you click._ · _Right action, wrong certainty. Still a leak._ · _How to get twice the feedback from every drill hand._

Review: [ ]

### Facing a flop c-bet in a 3-bet pot is a must-train spot on every texture
`c-cash-6max-gp35-facing-cbet-3bet-pot-high-priority-003` · intermediate · flop · 3bet-pot · ip · consensus 0.50 · sources: rio · **draft**

**Claim.** Put the in-position decision against a 3-bet-pot c-bet at the top of your training list across all board types. It is frequent, the pot is already big, and the folding thresholds feel unnatural, so drill it even if your stats look fine.

**Why.** Mistakes scale with pot size, and a 3-bet pot on the flop is already several times the size of a single-raised pot. The spot comes up every session, and players who learned in tighter games tend to fold too much here because their instinct for what continues is calibrated to smaller ranges. A high-frequency, high-stakes node with a known bias is exactly what drills are for. Good stats over a sample do not excuse skipping it; they only mean you are maintaining rather than repairing.

**Common mistake.** Training exotic spots while the everyday 3-bet pot defence runs on autopilot.

**Hooks.** _The biggest pot you play every session. Are you training it?_ · _Good stats are not a reason to skip this drill._ · _3-bet pot, flop c-bet. Most players fold too much._

Review: [ ]

### If you cannot explain a solver nuance in a minute, leave it out of your game plan
`c-cash-6max-gp35-ignore-unexplainable-nuance-008` · intermediate · flop · 3bet-pot · ip · consensus 0.50 · sources: rio · **draft**

**Claim.** When a solver uses a special size only on a very specific sub-texture, like low paired rainbow but not low paired two-tone, and you cannot quickly see why, drop it. Stick to the simple size and move on.

**Why.** A strategy you cannot explain is one you cannot apply reliably at the table or adapt when the opponent deviates. Fine distinctions between near-identical textures are the kind of detail that matters for high-precision play against elite regulars after enormous volume, not for building a working plan. Many of these also sit in spots you reach rarely, such as being checked to on a paired board, so the EV at stake is tiny. Spend that attention on frequent spots and clear principles.

**Common mistake.** Memorizing a long list of texture-specific sizing exceptions that never get executed correctly in real time.

**Hooks.** _Can't explain the solver's play? Don't copy it._ · _Most solver nuance is noise for your game._ · _The one-minute rule for solver output._

Review: [ ]

### Drill the whole in-position flop node rather than one isolated action
`c-cash-6max-gp35-realistic-drill-all-actions-009` · intermediate · flop · 3bet-pot · ip · consensus 0.50 · sources: rio · **draft**

**Claim.** When you want to train both facing a c-bet and facing a check in 3-bet pots, set the drill to play the full flop in position without knowing what the opponent will do. You get a realistic mix of sizes and checks instead of a single filtered line.

**Why.** An isolated drill like "facing a 30% bet" is efficient when you have one narrow leak. But when the leaks span several branches, separate drills for each size and for checks multiply the setup work and make the practice feel artificial. Letting the trainer mix the actions keeps you processing the spot the way you would at the table, exposes you to the less common sizes in proportion, and is a good moment to run two tables to simulate game pace.

**Common mistake.** Only ever drilling one pre-filtered action, so the first time you face a different size is at the table.

**Hooks.** _Your drills are too narrow. Here's a better setup._ · _Train the spot the way it happens at the table._ · _One drill, every flop action._

Review: [ ]

### Keep the first decision point to one or two options so later streets stay learnable
`c-cash-6max-gp36-few-options-at-early-nodes-009` · intermediate · multi-street · 3bet-pot · any · consensus 0.50 · sources: rio · **draft**

**Claim.** Limit preflop and flop decisions to at most two options per spot. Every extra branch at an early node multiplies the number of turn and river strategies you have to know.

**Why.** A game tree fans out from each decision. If you use three flop sizes plus a check, you need four different turn plans and many more river plans, and your study time gets spread so thin that none of them is played well. One or two early options let you see every branch that follows and go deep on them. The later parts of a game plan become dramatically simpler when the early nodes were kept narrow. Running sims with only one size allowed, then two, then all, and comparing total EV is the manual way to confirm the cheap simplification.

**Common mistake.** Using four flop sizes "like the solver" and then improvising every turn because no one can study that many branches.

**Hooks.** _Every extra flop size doubles your turn homework._ · _Why the pros use fewer bet sizes than the solver._ · _Narrow the flop, master the river._

Review: [ ]

### Pay a few hundredths of a big blind for a strategy you can actually execute
`c-cash-6max-gp36-trade-ev-for-simplicity-008` · intermediate · multi-street · 3bet-pot · any · consensus 0.50 · sources: rio · **draft**

**Claim.** Choose simplified strategies that lose a tiny amount of theoretical EV in exchange for being easier to remember and to play, and pick the simplification that steers the game toward your strengths and your opponents' weak responses.

**Why.** Strong players routinely discard solver mixes in favour of one or two options at a node, because accuracy at the table is worth more than a 0.01bb edge on paper. The choice of simplification is also an exploit: a high-checking plan invites stabs and sets up check-raises, a high-betting plan tests whether opponents fold too much. While you work on a weakness, the plan can route around it. Simplification is not laziness, it is strategy design.

**Common mistake.** Trying to reproduce mixed solver frequencies in real time and making large execution errors to protect a tiny theoretical edge.

**Hooks.** _The solver mix costs you more than the simple plan._ · _Give up 0.01bb on paper, gain real money at the table._ · _Simplifying is a strategy, not a shortcut._

Review: [ ]

### Study a flop subset for patterns, not 1755 flops by heart
`c-cash-6max-tc12-study-flop-subset-for-patterns-004` · intermediate · flop · srp · btn · consensus 0.50 · sources: 2cc · **draft**

**Claim.** Do not try to memorise solver output flop by flop. Solve a representative subset of around a hundred flops, line them up side by side and extract the texture rules that predict the size and frequency.

**Why.** There are 1755 strategically distinct flops in hold'em, far too many to learn individually. But solver choices cluster strongly by texture, so a well-chosen subset reveals the same rules a full study would. Sorting the subset by chosen size or by betting frequency makes the shared features of each group jump out, and those features (high card, pairing, suitedness, connectivity) are what you can actually recognise at the table.

**Common mistake.** Opening single flops in a solver, memorising specific hand mixes, and having nothing transferable when a slightly different board appears.

**Numbers.** 1755 strategically different flops in NLHE · A subset of ~102 flops is enough to derive the main sizing patterns

**Hooks.** _There are 1755 flops. You need to study about 100._ · _How we turned a solver into three rules._ · _Stop memorising flops. Start sorting them._

Review: [ ]

### Sort an aggregate flop report by check frequency to find texture rules
`c-cash-6max-tc14-sort-aggregate-report-by-check-frequency-003` · advanced · flop · srp · btn · consensus 0.50 · sources: 2cc · **draft**

**Claim.** To learn c-bet frequencies, open a solver's aggregate report for the spot, sort all flops by checking frequency, and compare the two ends of the list. Look for shared features (suits, pairing, high card) rather than individual hands.

**Why.** Individual solves tell you about one board; the aggregate view tells you which textures drive the decision. Starting from the most-checked and least-checked flops makes the drivers obvious - at one end you see rainbow, paired and high-card boards, at the other monotone and ace-high boards. Having the preflop ranges open beside the report lets you tie each pattern to a reason, which is what makes the rule stick. The mixed-size report is fine for this purpose because you are studying frequency, not size.

**Common mistake.** Studying flops one at a time and memorising hand-by-hand actions that do not transfer to the next board.

**Hooks.** _The five-minute solver study that fixes your flop c-bets._ · _Stop solving one flop at a time._ · _Sort by checks, not by hand. Here's what you'll see._

Review: [ ]

### A solver's maximum exploit assumes you can punish every later mistake too
`c-cash-6max-tc17-max-exploit-assumes-full-knowledge-007` · advanced · flop · srp · btn · consensus 0.50 · sources: 2cc · **draft**

**Claim.** When you node-lock an opponent and read the maximum-exploit output, it c-bets 100% on 774 because it will also exploit every downstream error. Unless you know and can act on those later-street mistakes, prefer the cautious adjustment, which on this board is c-betting less than theory.

**Why.** The max-exploit line is solved against an opponent who never readjusts at any later node, and the solver sees every one of their deviations. Betting the whole range is its way of reaching those profitable spots as often as possible. A human does not have that map. The cautious exploit only attacks the one leak you have actually observed, the wider check-raise and lower fold rate, and the correct answer to that alone is a stronger, less frequent c-bet.

**Common mistake.** Seeing a 100% c-bet in a max-exploit output and range-betting a board where the real-world leak calls for a tighter range.

**Hooks.** _The solver says bet 100%. A coach says ignore it._ · _Two exploits, opposite answers. Which one is yours?_ · _Why max-exploit outputs lie to human players._

Review: [ ]


## table-selection  (13)

### Seat selection matters as much as table selection
`c-cash-6max-br1-fish-on-your-right-002` · beginner · any · consensus 0.50 · sources: br79 · **draft**

**Claim.** Sit so that the weakest player at the table acts before you, ideally directly to your right. Position on a specific opponent decides how many hands you can play against them and who gets the last bet in.

**Why.** Take two players of identical skill at a 6-max table and give one of them position on the other. The player acting last will win a substantial amount from the other over time with no skill difference at all. Now apply that to a player who already makes mistakes: with them on your right you can isolate their limps, call their weak raises, control pot size and bet when they check. With them on your left they get to act after you on every street and much of that edge evaporates.

**Common mistake.** Treating any seat at a soft table as equally good, or staying seated with the weak player on your left because moving feels like effort.

**Hooks.** _Same table, wrong seat, half the profit._ · _Who sits on your right decides your win rate._ · _The seat you choose is a decision. Treat it like one._

Review: [ ]

### Open your own table instead of joining waiting lists
`c-cash-6max-br1-start-own-tables-001` · beginner · any · consensus 0.50 · sources: br79 · **draft**

**Claim.** If you want to play against recreational players, start empty tables yourself rather than queuing for the busiest high-VPIP tables. Weak players want to play immediately and will sit at a table with one person waiting far sooner than they will join a list.

**Why.** Lobby stats describe the past. By the time you get a seat at a table showing a high VPIP, the player who created that number may already be broke and gone. Waiting lists also take away seat choice, so you cannot guarantee the weak player ends up on your right. An empty table flips the dynamic: the impatient player comes to you, you already hold a seat, and you choose whether to stay once you see who arrived. On smaller sites with few tables this is often the only reliable way to find soft games at all.

**Common mistake.** Loading every full high-VPIP table, joining five waiting lists and assuming the fish will still be there when a seat opens.

**Hooks.** _Waiting lists are where your win rate goes to die._ · _Stop chasing the fish. Let them come to you._ · _The best table in the lobby is the one you create._

Review: [ ]

### Tag weak players immediately and leave tables that have none
`c-cash-6max-br1-tag-and-cycle-tables-007` · beginner · any · consensus 0.50 · sources: br79 · **draft**

**Claim.** Mark a player as recreational the moment you see a clear sign such as an open-limp, a short or odd buy-in or a very high VPIP over even a dozen hands. Then glance at each table: if no tagged player is seated, leave and open or join another one.

**Why.** Your reason for being at any table is a specific weak player, not the table itself. Tags make that reason visible at a glance when you are playing several tables and cannot remember who is who. They also make the exit decision mechanical: no tag, no reason to stay. You will face enough regulars by accident; there is no need to volunteer for more by sitting at a table where everyone plays reasonably.

**Common mistake.** Staying at a table out of inertia after the weak player has busted, and grinding against regulars for an hour.

**Numbers.** Coach treats ~64% VPIP over 14 hands as enough to tag someone

**Hooks.** _No fish tag on the table? You should not be there._ · _One habit that fixes table selection in a single session._ · _Fourteen hands is enough to know who pays you._

Review: [ ]

### Prefer tables with the biggest losers, not just any losing player
`c-cash-6max-br3-loss-rate-table-choice-004` · beginner · any · consensus 0.50 · sources: br79 · **draft**

**Claim.** Not all weak players are equal. Someone losing at 20 big blinds per 100 gives away money ten times faster than someone losing at 2 big blinds per 100. When you can choose, leave a table of slightly-bad players for one with an 80% VPIP player, even if the current table is beatable.

**Why.** Your win rate is roughly the sum of what the other players at the table lose to you. A semi-weak player who limps a bit but also folds a lot is a small, slow source of profit. A player seeing 80-90% of flops is a large, fast one. Being able to beat a table is not the same as it being the best use of your time, so on sites with many tables keep moving until the fast losers are the ones you sit with.

**Common mistake.** Staying at a table because "these guys are kind of bad" when much worse players are available two clicks away.

**Numbers.** Loser at 20bb/100 gives money ~10x faster than loser at 2bb/100 · Target VPIP ~80-90% players over ~40% players when both are available

**Hooks.** _Two fish, same table, one is worth ten times more._ · _Beatable is not the same as best. Move tables._ · _The 80% VPIP player pays you ten times faster._

Review: [ ]

### When the fish busts, give them an orbit to reload before leaving
`c-cash-6max-br3-stay-an-orbit-after-fish-busts-014` · beginner · any · consensus 0.50 · sources: br79 · **draft**

**Claim.** After the weak player at your table loses their stack, do not leave instantly. Stay for about one orbit to see whether they rebuy. If they do, they are now likely tilted and you already have position on them; if they do not, go find another table.

**Why.** A busted recreational player who reloads is one of the best opponents available: they are frustrated, chasing losses and in the same seat where you already hold the positional edge. Leaving the moment they bust throws that away for the uncertainty of a new table. An orbit costs almost nothing in blinds and resolves the question. If the seat stays empty, the table has lost its reason and you move on.

**Common mistake.** Quitting the table the second the fish is felted, then watching them rebuy against someone else.

**Hooks.** _The fish busted. Do not leave yet._ · _A reloaded fish is a tilted fish. Stay one orbit._ · _Why the best opponent is the one who just lost a stack._

Review: [ ]

### In 6-max, a VPIP of about 35-40% or more marks the player to target
`c-cash-6max-br4-fish-vpip-threshold-003` · beginner · any · consensus 0.50 · sources: br79 · **draft**

**Claim.** Use a higher VPIP threshold to identify weak players in 6-max than in full ring. Around 30% is loose at a 9-handed table, but short-handed ranges are naturally wider, so look for roughly 35-40% and above before treating someone as the mark.

**Why.** Fewer players means everyone should play more hands, so a 30% VPIP that screams recreational at full ring is only slightly loose in 6-max. Applying the full-ring number would have you targeting competent, loose-aggressive regulars. Very short-handed, with two or three players, the numbers inflate further still, so read VPIP relative to how many players were dealt in. A player showing 80-90% at any table size, however, is unambiguous.

**Common mistake.** Tagging a 28% VPIP 6-max player as a fish and discovering an aggressive regular.

**Numbers.** Full ring fish threshold ~30% VPIP; 6-max ~35-40%+

**Hooks.** _Thirty percent VPIP is not a fish in 6-max._ · _The one HUD number you need to adjust for table size._ · _Where the fish line sits at a six-handed table._

Review: [ ]

### Sort the lobby by seated players, then VPIP, then average pot
`c-cash-6max-br4-lobby-sort-order-001` · beginner · any · consensus 0.50 · sources: br79 · **draft**

**Claim.** Set your lobby to show tables with the most seated players first, then rank by players to the flop (or VPIP) and finally by average pot, all descending. Hide full tables so you only see ones you can actually join, and lock the sort so it survives a session.

**Why.** The players column tells you what kind of table you are opening, since a 3-handed table and a 5-handed one play very differently. Flop percentage is the most direct measure of how loose the table is, and average pot catches tables where loose players are also betting big. Filtering out full tables stops you from staring at games you cannot sit in, and a locked sort avoids re-doing settings mid-session when you are already stretched across several tables.

**Common mistake.** Sorting by one column only, or scrolling an unsorted lobby and picking tables at random.

**Hooks.** _Your lobby settings are a table-selection tool. Set them once._ · _Three columns that find soft tables for you._ · _Most players never touch the lobby sort. Big mistake._

Review: [ ]

### Leave the moment the weak player leaves, especially when playing four tables or fewer
`c-cash-6max-br5-leave-tables-without-a-fish-007` · beginner · any · consensus 0.50 · sources: br79 · **draft**

**Claim.** If a table has no clear weak player, only 15/15 and 16/11 types, leave and find another one, even mid-session. Leave too if the only weak player sits on your left. Grinding a table of regulars to prove you can steal their blinds is an ego boost, not a win rate.

**Why.** You can beat tight regulars slightly by stealing blinds, but they do not give away stacks; loose passive players do. With four tables or fewer, swapping tables costs almost nothing and a table with a 75% VPIP player or open-limpers can be found in minutes. Position matters as much as presence: a weak player on your left acts after you and limits how often you can isolate them. Treat every table as a temporary seat and keep moving towards the money.

**Common mistake.** Staying at a reg-filled table because leaving feels like admitting defeat, or because you have a few big blinds of history with someone.

**Hooks.** _The fish left. Why are you still sitting there?_ · _Table of regs? Leave. Your win rate is not an ego contest._ · _One habit that costs four-tablers a ton of money._

Review: [ ]

### Do not stay heads-up against a competent player; you never have to play anyone
`c-cash-6max-br6-do-not-sit-heads-up-vs-competent-players-004` · beginner · any · consensus 0.50 · sources: br79 · **draft**

**Claim.** When you start a table or sit short-handed and the only opponent turns out to be reasonable rather than bad, leave or sit out. The purpose of short-handed play is to catch impatient weak players, not to grind a coin flip against a thinking regular. Choose who you play.

**Why.** Heads-up against a decent player your edge is small and your variance is large, while a weak player at the same table would hand you money with no risk. Nothing forces you to accept the match-up; tables fill fast, so passing on one opponent costs you a few minutes at most. Being selective about opponents is the same discipline as being selective about hands.

**Common mistake.** Treating a heads-up match as a challenge to your pride and playing a competent opponent for an hour while weak players sit at other tables.

**Hooks.** _He turned out to be decent. So we left._ · _You never have to play a good player. Ever._ · _Heads-up is for catching fish, not proving a point._

Review: [ ]

### Start your own tables: impatient weak players come to you
`c-cash-6max-br6-start-your-own-tables-011` · beginner · any · consensus 0.50 · sources: br79 · **needs-review** · review note: _Duplicate of br1-start-own-tables-001. Keep one._

**Claim.** Instead of only joining full tables, open an empty one and sit down. The players who join an empty or short table are disproportionately recreational players who do not want to wait on a list. Tables fill within minutes, so you rarely play heads-up for long, and three-handed tables are worth trying too.

**Why.** Regulars queue for the tables that already look good; weak players want to play right now and click the first open seat. By sitting at an empty table you get first pick of those players, often with position on them, and you get to play every hand against them while the table is short. The slight discomfort of a few heads-up hands is a small price for being the first seat at what becomes a soft table.

**Common mistake.** Only joining full tables and waiting lists, where the seats around the weak player are already taken by regulars.

**Hooks.** _Stop joining tables. Start them._ · _Who sits down at an empty table? Exactly who you want._ · _The table selection trick nobody at NL5 uses._

Review: [ ]

### Weekend games are considerably softer than weekday afternoons, even at micro stakes
`c-cash-6max-br6-weekends-are-softer-012` · beginner · any · consensus 0.50 · sources: br79 · **needs-review** · review note: _Trivial; not a concept._

**Claim.** If your schedule allows, play on weekends and evenings rather than weekday afternoons. The games have always been softer then and still are, at every stake including NL2-NL10.

**Why.** Weekday afternoons are when the regulars grind and the recreational players are at work. Weekends bring in players who treat poker as entertainment, often with a drink in hand, who play more hands and call more bets. Your strategy does not change, but the number of profitable spots per hour does, and that is what drives win rate.

**Common mistake.** Grinding Tuesday afternoons out of habit and concluding the games are tough.

**Hooks.** _When you play matters almost as much as how._ · _The softest games of the week are not when you think._ · _A free win rate boost: change your session time._

Review: [ ]

### The players who join your empty table are often the weakest; play every hand against them
`c-cash-6max-br8-heads-up-tables-attract-impatient-weak-players-001` · beginner · any · consensus 0.50 · sources: br79 · **needs-review** · review note: _Duplicate of br1-start-own-tables-001. Keep one._

**Claim.** Players who sit at a one-player table are usually recreational: they do not want to wait on a list and want to play right away. Heads-up against them you play every hand, and they often spew the very next hand after losing a pot. Some of the biggest pots in a session come from these short-handed spots.

**Why.** A heads-up match against a weak player is the purest form of the micro-stakes edge: no regulars in the way, position every other hand, and an opponent who plays impatiently. They 3-bet small, call wide and stack off with top pair in 3-bet pots, so when you make a hand the money goes in. The match rarely lasts long because the table fills, which also means you do not need deep heads-up expertise, just discipline and value betting.

**Common mistake.** Refusing to sit at empty tables because heads-up feels intimidating, and giving up the softest spots on the site.

**Hooks.** _Who sits at an empty table? The player you want._ · _The biggest pot of the session came from a one-player table._ · _Impatient players are profitable players._

Review: [ ]

### Leave when an active 3-bettor sits on your left and the only weak player is marginal
`c-cash-6max-br8-leave-when-a-3bettor-sits-on-your-left-012` · beginner · any · consensus 0.50 · sources: br79 · **draft**

**Claim.** Two factors together make a table not worth your time: a player with a real 3-bet percentage, say 9% over 80-plus hands, directly to your left, and no true fish, only a semi-loose passive type. Leave. If the weak player were a genuine 40-50% VPIP fish, stay and put up with the 3-bettor.

**Why.** A frequent 3-bettor on your left taxes every open and every isolation raise, which is exactly the play you make most against weak players. That tax is worth paying when a big fish is handing out stacks, but not when the only soft spot is a player who sees 28% of flops and folds a lot. Table quality is the product of how much the weak players give and how much the strong players cost you; when the second outweighs the first, move.

**Common mistake.** Staying because "there is a weak player here" without weighing how much the reg on your left is costing you every orbit.

**Numbers.** a ~9% 3-bet over ~84 hands on your left is a reason to leave if no true fish is present · stay if the weak player is a genuine ~40-50% VPIP fish

**Hooks.** _Two seats decide whether this table is worth it._ · _A 3-bettor on your left changes the whole table math._ · _We left a table with a weak player on it. Why?_

Review: [ ]


## hand-reading  (14)

### Calling a flop bet out of position with nothing is a fish tell
`c-cash-6max-br2-oop-float-tell-009` · beginner · flop · oop · consensus 0.50 · sources: br79 · **draft**

**Claim.** A player who calls a flop c-bet without a pair or a draw while out of position can be tagged as weak immediately. Floating with nothing can make sense in position, where you can bluff the turn; out of position it has no plan behind it.

**Why.** The idea behind a float is to take the pot away later when the bettor shows weakness. That only works if you act after them on the next street. A call with nothing from first to act cannot follow that plan, so it is just a loose call. Spotting it tells you two things: the opponent calls too much, and they do not think about position. Both are exploitable by value-betting them relentlessly and never bluffing them.

**Common mistake.** Assuming an opponent who peels a flop with air is a tricky player rather than a loose one.

**Hooks.** _One flop call tells you everything about this player._ · _Floating out of position is not tricky. It is a leak._ · _Tag him the moment he calls with nothing from the blinds._

Review: [ ]

### You can classify a new opponent within about ten hands
`c-cash-6max-br2-spot-strong-player-fast-001` · beginner · any · consensus 0.50 · sources: br79 · **draft**

**Claim.** A few early signals separate competent players from weak ones: competent players never open-limp, buy in for a full stack, and show VPIP and PFR close together. Half-stack buy-ins, limps from the small blind or button and a wide VPIP-to-PFR gap point to a weak player. Decide quickly and act on it.

**Why.** Waiting for a hundred hands of stats before judging an opponent wastes the time you could be spending at a better table. The signals above are not noise: no strong player limps the button, and a big gap between hands played and hands raised means a lot of passive calling. Heads-up a solid player will show something like 50% VPIP and 40% PFR, with the numbers close together. Read these cues early, then either stay and target the weak player or leave if the only opponent looks solid.

**Common mistake.** Sitting heads-up against a good player for an hour "to see how it goes" when the first ten hands already said everything.

**Numbers.** Solid heads-up stats roughly VPIP 50 / PFR 40, close together

**Hooks.** _Ten hands. That is all you need to type a player._ · _Nobody good limps the button. Nobody._ · _Three signs you are sitting with a reg, not a fish._

Review: [ ]

### Odd buy-in amounts and instant shoves mark a recreational player
`c-cash-6max-br2-stack-size-tells-002` · beginner · any · consensus 0.50 · sources: br79 · **needs-review** · review note: _Dated anecdote, weak publishable value._

**Claim.** A player who sits with a strange amount such as 62 big blinds or 78 big blinds, rather than a round max or min buy-in, is very likely playing their entire balance and is a weak player. If they also start open-shoving, treat them as a gambler and call with any reasonable hand.

**Why.** Nobody types an odd number into the buy-in box by choice; it is what is left in the account. Someone depositing their whole bankroll at a micro table is not a studied player, and the behaviour that often follows, shoving preflop, mini-raising and calling with nothing, confirms it. Recognizing this before a single hand is played lets you tag them, seat yourself correctly and widen your calling range before they bust to someone else.

**Common mistake.** Giving an unknown short stack the benefit of the doubt for an orbit while they shove into other players.

**Hooks.** _The buy-in amount tells you who they are before hand one._ · _Sixty-two big blinds is not a buy-in. It is a confession._ · _Spot the fish before the cards are dealt._

Review: [ ]

### Posting a blind out of turn, limping and odd buy-ins are all beginner tells
`c-cash-6max-br3-posting-utg-tell-016` · beginner · preflop · any · consensus 0.50 · sources: br79 · **needs-review** · review note: _Dated anecdote, weak publishable value._

**Claim.** A player who posts a blind under the gun instead of waiting one hand for the big blind is volunteering to pay twice, which only an inexperienced player does. Add it to limps and odd buy-in amounts as a quick signal to tag them before they have shown a hand.

**Why.** Every one of these actions has a free alternative that any studied player would take: wait a hand, raise instead of limping, buy in for a round full stack. Choosing the costly option reveals that the player is not thinking about expected value at all. Spotting it saves you the dozens of hands a HUD needs and lets you widen your isolation and value-betting range against them from the first orbit.

**Common mistake.** Ignoring everything that happens before the cards are dealt.

**Hooks.** _He posted under the gun. You already know everything._ · _Three tells that show up before the first card._ · _Paying the blind twice is a tell, not a mistake._

Review: [ ]

### Normal-looking stats do not mean an opponent deserves credit
`c-cash-6max-br3-tight-stats-no-credit-012` · beginner · any · consensus 0.50 · sources: br79 · **draft**

**Claim.** A player with reasonable VPIP and PFR can still make very bad plays, such as stacking off with a weak draw or a bare pair. Do not fold a strong hand simply because the HUD says the opponent is tight; judge their actual play in the hand.

**Why.** Preflop stats describe only one part of a player's game. Someone who plays 21% of hands may still have no idea how to play postflop, and at micro stakes that is common. Giving automatic credit to tight stats means folding winners to players who are not thinking at the level you assume. Read the action, the sizing and the board, and use the stats as a starting point rather than a verdict. A tight player who does one silly thing is probably a slight loser, not a reason to stay at the table, but also not a reason to fold.

**Common mistake.** Folding top pair to a raise from a 21/17 player and being shown a gutshot.

**Hooks.** _Tight stats, terrible play. It happens more than you think._ · _The HUD said reg. The hand said fish. Trust the hand._ · _Do not fold to a number on a screen._

Review: [ ]

### Loose players have an ace far more often than a normal range does
`c-cash-6max-br5-loose-players-hold-more-aces-013` · beginner · flop · srp · oop · consensus 0.50 · sources: br79 · **draft**

**Claim.** A player who enters the pot with every ace holds an ace on an ace-high flop much more often than a tight raiser would. So out of position with a medium pair on an ace-high board against a loose player, do not lead into them; check and call or fold, because they are sticky and have the ace a lot of the time.

**Why.** Range construction is about what a player actually enters pots with, not what a textbook range says. Loose players treat any ace as playable, so their range is weighted heavily towards ace-x. Leading out with a medium pair only creates headaches: they will not fold the ace, they call with worse and then stay sticky, and you end up guessing on later streets out of position. Give an unknown early position raiser some credit, keep the pot small, and let them tell you where they stand.

**Common mistake.** Donk-betting middle pair into a loose player on an ace-high flop and then facing a raise or two more streets of pressure with no plan.

**Hooks.** _Ace on the flop versus a loose player? Assume he has it._ · _The one card loose players always seem to hold._ · _Why leading middle pair into a fish backfires._

Review: [ ]

### A limp-reraise at micro stakes is a nut hand; fold without a second thought
`c-cash-6max-br6-limp-reraise-means-the-nuts-003` · beginner · preflop · limped · any · consensus 0.50 · sources: br79 · **draft**

**Claim.** When a player open-limps and then re-raises your isolation raise, treat it as aces or kings almost every time at NL2-NL10 and fold anything short of a premium. The same read applies to a river check-raise from an unknown: it is the nuts far more often than a bluff.

**Why.** The limp-reraise is a classic weak-player move to trap with a monster; the population at these stakes almost never does it as a bluff or with a medium hand. Calling with a decent but non-premium hand sets you up to lose a big pot against a range that is nearly all overpairs. The rare exception is an aggressive or tilted heads-up opponent who has shown they will spazz; against everyone else the fold is automatic and costs you nothing.

**Common mistake.** Calling a limp-reraise with ace-queen or a medium pair because the pot is already big, then stacking off to kings.

**Hooks.** _Limp, then re-raise. You already know what he has._ · _The oldest trap in micro-stakes poker still works on you._ · _One preflop pattern that means aces or kings._

Review: [ ]

### Recognize the semi-loose passive: fewer hands than a fish, but still a losing player
`c-cash-6max-br7-semi-loose-passive-player-type-008` · beginner · any · consensus 0.50 · sources: br79 · **draft**

**Claim.** Not every weak player is a 50% VPIP maniac. A semi-loose passive type plays around 28% of hands with a very low raise percentage, roughly 28/6. They bleed slower than a true fish (40-50% VPIP), but when they play they call raises with small pairs and limp broadways. A big VPIP-PFR gap is the signature of this losing type; 10-15 hands shows it.

**Why.** Table selection and isolation decisions depend on classifying opponents accurately. The true fish is your main target, but a table of regulars with one semi-loose passive player is still worth sitting at, while a table with none of either should be left. Recognizing the gap between how often someone plays and how often they raise tells you quickly that they are passive and exploitable: isolate their limps, value bet them thinner, and do not expect them to play back.

**Common mistake.** Dismissing a 28/6 as a regular because the VPIP looks moderate, and missing a steady source of value at the table.

**Numbers.** semi-loose passive: roughly 28/6 stats · true fish: ~40-50% VPIP with a big VPIP-PFR gap · 10-15 hands is enough to classify a player type

**Hooks.** _The losing player you are not tagging._ · _28/6 is not a reg. Here is what it is._ · _One gap on your HUD that spots passive players instantly._

Review: [ ]

### A true fish is 40%+ VPIP with a big VPIP-PFR gap; a small gap means a LAG instead
`c-cash-6max-br8-fish-vs-lag-vs-maniac-classification-007` · beginner · any · consensus 0.50 · sources: br79 · **draft**

**Claim.** Tag a player as a fish when they play around 40% or more of hands (at least 35%) with a large VPIP-PFR gap over ten-plus hands. A 47/37 is not a fish but a loose-aggressive player; a maniac plays 60-80% of hands and raises most of them. Passive preflop usually means passive postflop, and aggressive preflop means aggressive postflop, so the tag tells you what to expect later.

**Why.** The exploit for each type is different. Passive loose players limp and fold, call down with weak pairs and rarely bluff, so you value bet them relentlessly and never bluff them. Loose-aggressive players and maniacs raise, 3-bet and barrel, so you widen your calling and stacking ranges and let them bluff into you. Lumping a 47/37 in with a 48/21 leads to exactly the wrong adjustments. The VPIP-PFR gap is the fastest way to tell them apart.

**Common mistake.** Labelling every high-VPIP player a fish and then being surprised when the loose-aggressive one 3-bets and barrels you off hands.

**Numbers.** fish: ~40%+ VPIP (at least 35%) with a big VPIP-PFR gap, minimum ~10 hands · 47/37 or 44/33 is a LAG, not a fish; 48/21 is a classic fish · maniac: ~60-80% VPIP, raising most hands

**Hooks.** _47/37 and 48/21 look similar. They are opposite players._ · _Not every loose player is a fish. Check the gap._ · _Passive before the flop means passive after it._

Review: [ ]

### Define a bet by naming the hands that fold to it, not by how the board hits a range
`c-cash-6max-cc03-ask-what-folds-005` · beginner · flop · srp · consensus 0.50 · sources: cc · **draft**

**Claim.** "This board connects with his range" tells you nothing about what your bet does. To understand a bet, name one hand you are bluffing (a better hand that folds) and one hand you are denying equity to (a worse hand with live outs that folds). If you cannot name either, question the bet.

**Why.** A bet only changes the outcome against hands that fold, so that is the set you must think about. A 3/4-pot c-bet with ace-king on Q-T-3 rainbow folds out small pocket pairs (a bluff, since they are ahead) and also folds out junk like 6-5 with a backdoor draw and two live cards (denial). Hands like K-J that call or raise are not being denied anything; they may even outplay you later. And a hand you beat today, such as K-9, might bluff you off the pot on a later street, so being ahead of it now does not make the bet pure value. Thinking in terms of which hands fold keeps you honest about why the chips go in.

**Common mistake.** Justifying a bet with "I want to fold out X" where X is a small slice of the range, or with "the board hits him" where that says nothing about what folds.

**Example.** positions: UTG vs BB | hero: AhKd | board: Qs Tc 3h | action: UTG opens, BB calls. BB checks, UTG bets 75% pot. | decision: What is this bet doing? | answer: Bluff-denial: it folds out small pairs that are ahead (bluff) and junk with live cards (denial). Too little equity when called to be value.

**Hooks.** _'The board hits his range' is a meaningless sentence._ · _Name the hand that folds. Then you understand your bet._ · _Ace-king on Q-T-3: value bet or bluff? Neither._

Review: [ ]

### Judge ranges by concentration, not by raw combo count
`c-cash-6max-cc06-concentration-beats-combo-count-005` · intermediate · flop · 3bet-pot · any · consensus 0.50 · sources: cc · **draft**

**Claim.** What matters is the percentage of a range that is strong, not how many strong combos it contains in absolute terms. A wider range can hold more combos of a hand class and still have it less often.

**Why.** You only get dealt one hand at a time, so the relevant question is how likely you are to be holding a given class when you look down. A 3-bettor in a blind-vs-blind pot has more total combos of top pair on a queen-high flop than the caller, because they 3-bet every strong queen. But their range is also padded with suited aces, offsuit broadways and bluffs, so top pair makes up a smaller slice. Compare a range that is half nuts and half air with one that is mostly air plus a larger pile of nuts, and the first is stronger even with fewer good combos. Always convert "how many" into "how often".

**Common mistake.** Arguing "I have more Qx than villain in this 3-bet pot" and treating it as a strength argument when Qx is actually a smaller share of the wider range.

**Hooks.** _More combos of top pair, yet you hold it less often._ · _Count percentages, not combos. Here's why._ · _Would you rather have range A or range B?_

Review: [ ]

### Calling a flop bet condenses a range, and that raises its equity
`c-cash-6max-cc06-condensed-range-not-weak-001` · intermediate · flop · srp · any · consensus 0.50 · sources: cc · **draft**

**Claim.** When a player calls a bet instead of raising or folding, their range loses its very best and very worst hands at once. The top is capped, but the bottom is cut away, so the average equity of what remains goes up, not down.

**Why.** Picture a range as a team. Dropping the weakest members improves the team even if you also lose the star. A flop call does exactly that. The trash folds, a few monsters raise, and what is left is a tight block of medium-to-good hands plus draws. Against the bettor's still-wide range, that block often has as much equity as the bettor or more. Equity is not the same as EV share, though. The player with position and more nutted hands can still be the one making more money. But treating a caller as "weak because they only called" is a reading error that leads to bad barrels.

**Common mistake.** Reading a flop call as a sign of weakness and firing the turn with hands that have no business betting, because "they capped themselves".

**Hooks.** _They called. Their range just got stronger, not weaker._ · _Capped does not mean weak. Here is the difference._ · _Why a flat call can beat your range in equity_

Review: [ ]

### On low flops, connectivity to the main straight draw can outrank a higher overcard
`c-cash-6max-gp30-low-board-connectivity-beats-overcards-007` · advanced · flop · srp · oop · consensus 0.50 · sources: rio · **draft**

**Claim.** Facing a c-bet on an all-low flop, the continue line is roughly "two overcards or a combination backdoor". A hand that connects with the board's primary straight draw plus a backdoor flush draw continues even without an overcard, while a hand with a bigger high card but no connectivity can fold. Some weak pairs with no backdoor flush draw rank below those double-overcard or combo backdoor hands.

**Why.** Relative hand strength on a low board is about equity and how cleanly it is realized, not card rank. Two overcards give six outs to a pair that is often good. A hand like seven-six on a 5-4-x board has a straight draw to come plus flush possibilities, and when it hits it tends to be the best hand. A lone high card with nothing else has three outs and bad reverse implied odds. Pocket threes or seven-deuce with a pair but no backdoors have little chance to improve and are often behind already. The qualities that matter are overcards, connectivity and suits, roughly in that order, and combinations of them beat any single one.

**Common mistake.** Ranking continues by the highest card in the hand, so K-T offsuit calls and 7-6 suited folds when the solver does the opposite.

**Example.** positions: CO vs BB | hero: 7s6s | board: 5h4s2c | action: CO opens, BB calls. BB checks, CO bets 75%. | decision: Continue with no overcard? | answer: Yes. Open-ended connectivity plus a backdoor flush draw outranks a lone king-high here.

**Hooks.** _7-6 suited beats K-T here. Not what you expect._ · _On low boards, high cards are overrated._ · _The hand quality that beats an overcard on 542._

Review: [ ]

### Facing a small c-bet, the lower connector continues better than the higher one
`c-cash-6max-gp35-lower-connector-better-than-jt-015` · advanced · flop · 3bet-pot · ip · consensus 0.50 · sources: rio · **draft**

**Claim.** On a low-to-mid flop in a 3-bet pot, a hand like T9 can be a better continue or raise than JT, even though JT is higher. The lower hand turns open-ended draws on cards that favour the in-position caller, while the higher hand improves on Broadway cards that help the 3-bettor's range.

**Why.** What matters is not only how often you improve but what the improving card does to the opponent's range. A turn card that connects with your low cards is typically a brick for a 3-betting range full of high pairs and Broadway hands, so your draw is live and your aggression is credible. A Broadway turn gives you a draw while also giving the opponent top pair or a better draw, so your improvement is worth less. Rank continues by how well your outs interact with the board, not by card rank.

**Common mistake.** Preferring the "higher" hand when choosing between two marginal continues against a 3-bet-pot c-bet.

**Hooks.** _T9 beats JT here. Counterintuitive, but true._ · _Not all outs are equal. Some help your opponent._ · _Which cards do you want to turn? Think about their range._

Review: [ ]


## tools-software  (4)

### A wide gap between VPIP and PFR marks a weak, passive player
`c-cash-6max-br2-gap-vpip-pfr-013` · beginner · any · consensus 0.50 · sources: br79 · **draft**

**Claim.** When a HUD shows someone playing many hands but raising few of them, for example 50% VPIP and 10% PFR, you are looking at a passive recreational player. Someone with the two numbers close together is usually competent regardless of how loose they are.

**Why.** The gap measures how often a player enters pots by calling or limping rather than raising. Competent players enter almost every pot with a raise, so their numbers track each other. A large gap means a lot of limping and flatting, which goes hand in hand with calling down too much and rarely applying pressure. Against this type the plan is simple: wait for a strong pair or better, bet every street for value and skip the bluffs.

**Common mistake.** Judging a player only by VPIP and treating a 50/40 player and a 50/10 player the same.

**Numbers.** Close VPIP/PFR (e.g. 50/40 heads-up) = competent; wide gap = weak

**Hooks.** _Two HUD numbers that tell you who to target._ · _Fifty-ten and fifty-forty are not the same player at all._ · _The gap in the stats is where the money is._

Review: [ ]

### Tag opponents after about a dozen hands using VPIP and PFR
`c-cash-6max-br5-tag-players-fast-001` · beginner · preflop · any · consensus 0.50 · sources: br79 · **draft**

**Claim.** You do not need a big sample to label a player. VPIP and PFR settle quickly: after roughly ten to twelve hands (two orbits at 6-max) a 60%+ VPIP with a tiny PFR is a weak player, and someone who has played every hand for seven hands and min-raised from early position can already be tagged.

**Why.** Most HUD numbers need hundreds of hands, but VPIP and PFR are measured on every single hand dealt, so they converge far faster than any postflop stat. Weak players also leak information through single actions: an open-limp with junk, a min-raise from early position, posting in from a new seat. Tagging early matters because your whole table plan depends on knowing where the weak players sit, and you want them colour-coded before they bust or leave. Give the read some slack under ten hands, but do not wait for a large sample before acting on it.

**Common mistake.** Waiting for a statistically clean sample before adjusting, by which time the weak player has left the table or you have already passed on ten profitable spots.

**Numbers.** tag by ~10-12 hands (about two orbits at 6-max) · 100% VPIP over 7 hands plus a min-raise is already enough to label a weak player

**Hooks.** _Seven hands is enough to spot the weak player. Here is how._ · _You are waiting too long to tag the fish._ · _Two orbits. That is all the sample you need._

Review: [ ]

### Under ten hands, ignore VPIP and PFR; aggression factor needs around a hundred
`c-cash-6max-br8-sample-size-rules-for-hud-stats-008` · beginner · any · consensus 0.50 · sources: br79 · **draft**

**Claim.** Do not act on VPIP or PFR when the sample is under ten hands; a player can go from looking like a nit to 25/13 in one orbit. Those two stats become usable from roughly ten to fifteen hands. Postflop stats such as aggression factor need far more, around a hundred hands, before they mean anything.

**Why.** VPIP and PFR update on every hand dealt, so they stabilize quickly, but a handful of hands can still be all junk or all playable by chance. Postflop stats only update on the hands that reach a given street with a given action, so they accumulate far more slowly and a low aggression factor over 30 hands tells you almost nothing about whether a player can bluff a river. Match your confidence in a read to how many observations are behind it.

**Common mistake.** Folding to a 3-bet because a seven-hand sample shows the opponent as tight, or calling down because a tiny-sample aggression factor says they are a bluffer.

**Numbers.** VPIP/PFR: ignore under 10 hands, usable from ~10-15 · aggression factor: ~100 hands before trusting it

**Hooks.** _Seven hands said he was a nit. He was not._ · _How many hands before you can trust a HUD stat?_ · _Your aggression factor read is probably noise._

Review: [ ]

### In low-accuracy sims, trust the frequencies and ignore small EV gaps deep in the tree
`c-cash-6max-gp31-low-accuracy-sims-trust-frequency-011` · advanced · multi-street · srp · any · consensus 0.50 · sources: rio · **draft**

**Claim.** When a solver was run at low accuracy to extract frequencies quickly, treat tiny EV differences on later nodes as noise. A pure action can still show a non-zero EV loss, and the noise grows with every bet, raise and call that precedes the decision.

**Why.** Each node down the tree is solved against a slightly imprecise strategy on the previous node, so the errors compound. A spot reached by a small bet, a raise and a call might be solved with very few combos and an EV figure that is off by more than the gap between options. Frequencies are more robust than exact EVs in these conditions. If a decision shows a meaningful EV difference, check whether it is a genuine mistake or an artifact before changing your play.

**Common mistake.** Rebuilding a strategy around a half-blind EV difference reported by a sim that was never meant to be precise at that depth.

**Hooks.** _Your solver is lying about that EV. A little._ · _Deep-tree EV numbers are mostly noise._ · _Trust the frequency, not the decimal._

Review: [ ]

