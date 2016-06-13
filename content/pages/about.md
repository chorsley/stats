type: about
template: page
title:  About
slug: about

#About this website 

_**Demo**: This platform is a demo of version 2 of the CyberGreen metrics. As of now, the data and heat map simply illustrate the number (count) of infections and vulnerable devices. Our metrics are currently in development and undergoing review. Cybergreen metrics-based measurement and visualization will be finalized in December 2016._

_**Feedback**: Your feedback is valuable to us. If you have any questions, comments or suggestions about this demo, please [let us know](https://www.cybergreen.net/contacti/)_

<a id="score"></a>
#About the score

In our tables, a scoring system is used to illustrate a country’s performance. The score is a value between 0 and 100, where a higher score means a worse performance; that is, a greater number of affected devices and a higher level of risk or infection.

## Summary:

* Higher scores mean worse performance
* 100.0 is worst. Strictly, it will be worst performance on that risk by a country or ASN. As there is no theoretical maximum on number of affected devices, there is no “ultimate” worst value, so we set 100 to be worst performer – in future, this may change to be be set to some reference point.
* 0 is best. This means 0 affected devices which is the best possible outcome.
* Score is order preserving: if one place performs worse on counts (has more affected devices), it will perform worse on the score (have a higher score).

## Why scores (vs raw numbers of affected devices)

The reason for this scoring system versus just using the raw number of affected devices is that:

* Scores are "normalized" to be between 0-100 which assists in ease of understanding and comparability
 * Having a clear range makes it easy to see a country’s relative performance. For example, knowing one country has 50 affected machines would not mean much - if some countries have 1m, then that would be very good, whereas if no country has more than 100 it would seem just OK. A clear range obviates the need for this context.

## Calculating the score

The score is defined as follows:

Score for a country (on a given risk) = 100 x ln(devices) / ln(max devices)

* We take a logarithm of the numbers of affected devices. We do this because the distribution of these numbers is very broad, with a lot of small values and some very large ones. If you do simple division you “bunch” up low numbers to very high scores (lots of places are near 100). Logging helps to “spread” scores out.
* Get the score between 0 and 1 by dividing by ln(max devices)
* Multiply by a 100 to get a score within the range 0-100

