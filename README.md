# Ale Analysis: Unearthing the Bitter Truth of Beer Bias and the Quest for Objectivity

## 📓 Abstract
> A 150 word description of the project idea and goals. What’s the motivation behind your project? What story would you like to tell, and why?

Embark on a frothy journey as we delve into the world of beer reviews, unearthing patterns and insights that lie beneath the surface. This project aims to tap into the keg of beer ratings, exploring the influence of personal biases and geographical loyalties. We aim to distill the essence of beer ratings, separating the heady influence of a reviewer’s inherent “niceness” from their sober assessment. We also seek to uncover whether patriotism intoxicates our taste buds, influencing users to rate their home brews higher. Our motivation is to pour clarity into the pint of beer ratings, understanding how personal and geographical factors can add unique flavors to our perception of taste. Join us as we raise a toast to data, and discover the story each beer review has to tell. Let’s embark on this hop-filled journey to decode the ale-chemy of beer ratings!

## 👩‍🔬 Research questions
> A list of research questions you would like to address during the project.

### Question 1: Where are the beer nations?
1. Are there countries that receive particularly good ratings on average? How does this look in subcategories of the rating, such as taste, appearance, etc.? Which country is the most beautiful beer country?
2. What words best describe the beer nations based on the textual reviews?
3. Which type of beer performs best in which country?

### Question 2: Are beer nations brewed from a beer abundance?
1. Is there a correlation between the number of breweries in a country, the variety of beer types it produces, and the overall rating of its beers?

### Question 3: IBR - International beer relations
1. Where do the ratings for each country’s beers come from?
2. Which countries are particularly popular abroad?
4. Is there a Beer Union with countries that are mutually enthusiastic about their beer?
3. Is there a domestic beer pride? Do users rate beers in their home country better/worse?

### Question 4: Are beer reviewers the biggest bias?
1. Do seasoned beer reviewers have clear patterns in their ratings, and can we distinguish between those who consistently rate high, those who consistently rate low, and those who never rate below a certain threshold (e.g., 3/5)?
2. Can we correct for these biases by decorrelating a reviewer’s “niceness” from their beer ratings?
3. What beer nations emerge now?

## 💾 Proposed additional datasets
> List the additional dataset(s) you want to use (if any), and some ideas on how you expect to get, manage, process, and enrich it/them. Show us that you’ve read the docs and some examples, and that you have a clear idea on what to expect. Discuss data size and format if relevant. It is your responsibility to check that what you propose is feasible.

## 👾 Methods
### Question 1: Where are the beer nations?
1. We will calculate the average ratings and sub-ratings for each country. This will involve aggregating the data by country and computing descriptive statistics such as mean, median, and standard deviation.
2. We will perform text analysis on the reviews to identify the most frequently occurring words for each country. This will involve tokenizing the reviews, removing stop words, and counting word frequencies.
3. We will group the data by beer type and country to identify which type of beer performs best in each country. This will involve computing average ratings for each beer type within each country.

### Question 2: Are beer nations brewed from a beer abundance?
1. We will compute the correlation between the number of breweries, the variety of beer types, and the overall rating of beers in each country. This will involve aggregating the data by country and calculating statistical merits like Pearson's correlation coefficient.

#### Question 3: IBR - International beer relations
1. We will analyze the source of ratings for each country's beers. This will involve grouping the data by country and reviewer location.
2. We will identify countries that are particularly popular abroad by calculating the average rating given by foreign reviewers.
3. We will examine whether users rate beers from their home country higher or lower by comparing the average ratings given by domestic and foreign reviewers.
4. We will identify "beer nation friends" by looking for pairs or groups of countries where reviewers consistently rate each other's beers highly.

#### Question 4: Are beer reviewers the biggest bias?
1. We will identify patterns in beer reviewers' ratings. This will involve computing descriptive statistics for each reviewer's ratings and identifying those who consistently rate high, low, or never below a certain threshold.
2. We will attempt to correct for these biases by decorrelating a reviewer's "niceness" from their beer ratings. This will involve computing for example the standard deviation of each reviewer's ratings and adjusting their ratings accordingly.
3. We will recompute the beer nations based on these adjusted ratings.


## ⏲ Proposed timeline

 - Week 9: due on 17 November
	 - [ ] Delivery P2
 - Week 10: due on 24 November
	 - [ ] Start and finish work on H2
	 - [ ] Begin working on P3: research question 1
 - Week 11: due on 1 December
	 - [ ] finish P3 research question 1
	 - [ ] begin P3 research question 2
	 - [ ] Delivery H2
 - Week 12: due on 8 December
	 - [ ] finish P3 research question 2
	 - [ ] begin P3 research question 3
 - Week 13: due on 15 December
	 - [ ] finish P3 research question 3
	 - [ ] combine all results in data story
 - Week 14: due on 22 December 
	 - [ ] Fine-tuning of P3
	 - [ ] Delivery P3

## 🤪 Organization within the team
> A list of internal milestones up until project Milestone P3.

## ❓ Questions for TAs
> Add here any questions you have for us related to the proposed project.