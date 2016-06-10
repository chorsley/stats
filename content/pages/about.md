type: about
template: about
title:  About the scores
slug: about

In our tables, a scoring system is used to illustrate a country’s performance. The score is a value between 0 and 100, where a lower score means a worse performance; that is, a greater number of affected devices and a higher level of risk or infection.

## Summary:
* Higher scores mean better performance
* 0 is worst. Strictly, it will be worst performance on that risk by a country or ASN (As there is no theoretical maximum on number of affected devices, there is no “ultimate” worst value, so we set 0 to be worst performer for now – in future this may be set to some reference point)
* 100 is best. This means 0 affected devices which is best possible outcome
* Score is order preserving: if one place performs worse on counts (has more affected devices), it will perform worse on the score (have a lower score).

## Why scores (vs raw numbers of affected devices)
The reason for this scoring system versus just using the raw number of affected devices is that:

* Higher scores are better which is easy to understand. For numbers of affected machines it is the opposite, which can be confusing.
* “Normalized” to be between 0-100 provides ease of understanding and comparability
 * Having a clear range makes it easy to see a country’s relative performance. For example, knowing one country has 50 affected machines would not mean much - if some countries have 1m, then that would be very good, whereas if no country has more than 100 it would seem just OK. A clear range obviates the need for this context.

## Calculating the score
The score is defined as follows:

Score for a country (on a given risk) = 100 x [ ln(max devices) - ln(devices) ] / ln(max devices)

* We take a logarithm of the numbers of affected devices. We do this because the distribution of these numbers is very broad, with a lot of small values and some very large ones. If you do simple division you “bunch” up low numbers to very high scores (lots of places are near 100). Logging helps to “spread” scores out.
* Invert scores: subtract the score from the max number of devices: ln(max devices) - ln(devices)
* Get the score between 0 and 1 by dividing by ln(max devices)
* Multiply by a 100 to get a score within the range 0-100
