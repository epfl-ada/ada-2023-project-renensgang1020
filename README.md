# Global Brews, Local Views: Analyzing Cross-Country Beer Preferences and Challenging Reviewer Bias

## 📓 Abstract

Embark on a frothy journey as we delve into the world of beer reviews, unearthing patterns and insights that lie beneath the surface. This project aims to tap into the keg of beer ratings, exploring the influence of personal biases and geographical loyalties. We aim to distill the essence of beer ratings, separating the heady influence of a reviewer’s inherent “niceness” from their sober assessment. We also seek to uncover whether patriotism intoxicates our taste buds, influencing users to rate their home brews higher. Our motivation is to pour clarity into the pint of beer ratings, understanding how personal and geographical factors can add unique flavors to our perception of taste. Join us as we raise a toast to data, and discover the story each beer review has to tell. Let’s embark on this hop-filled journey to decode the ale-chemy of beer ratings!

## 👩‍🔬 Research questions

### Question 1: Where are the beer nations?
1. Are there countries that receive particularly good ratings on average? How does this look in subcategories of the rating, such as taste, appearance, etc.? Which is the most beautiful beer country - based on the appearance subcategory?
2. What descriptive words are frequently used in reviews to capture the essence of beers from different nations?
3. Which type of beer performs best in which country?

### Question 2: Are beer nations brewed from a beer abundance?
1. Does a higher number of breweries and a greater diversity of beer types within a country correlate with higher overall ratings for its beers?

### Question 3: IBR - International beer relations
1. From which countries do the majority of ratings for each nation's beers originate?
2. Which country’s beers are particularly popular abroad?
4. Is there a Beer Union with countries that are mutually enthusiastic about their beer?
3. Is there a domestic beer pride? Do users rate beers brewed in their home country better or worse?

### Question 4: Are beer reviewers the biggest bias?
1. Do seasoned beer reviewers have clear patterns in their ratings, and can we distinguish between those who consistently rate high, those who consistently rate low, and those who never rate below a certain threshold (e.g., 3/5)?
2. Can we correct for these biases by decorrelating a reviewer’s “niceness” from their beer ratings?
3. Which beer nations emerge now? Do our findings from questions 1-3 change?

## 👾 Methods

### Question 1: Where are the beer nations?
1. We will calculate the average ratings and sub-ratings for each country. This will involve aggregating the data by country and computing descriptive statistics such as mean, median, and standard deviation.
2. We will perform frequency analysis of keywords on the reviews to identify the most frequently occurring words for each country. This will involve tokenizing the reviews, removing stop words, and counting word frequencies.
3. We will group the data by beer type and country to identify which type of beer performs best in each country. This will involve computing average ratings for each beer type within each country.
   
### Question 2: Are beer nations brewed from a beer abundance?
1. We will compute the correlation between the number of breweries, the variety of beer types, and the overall rating of beers in each country. This will involve aggregating the data by country and calculating statistical merits like Pearson's correlation coefficient.

### Question 3: IBR - International beer relations
1. We will analyze the source of ratings for each country's beers. This will involve grouping the data by country and reviewer location.
2. We will identify countries that are particularly popular abroad by calculating the average rating given by foreign reviewers.
3. We will investigate if there is a bias in ratings by comparing the average ratings given to domestic beers by local reviewers with those given by foreign reviewers.
4. We will use network analysis to identify beer nation friends, with countries as nodes and edges representing the strength of beer rating relationships between them, based on the consistency and positivity of reviews they exchange. This approach will visually highlight pairs or groups of countries with strong mutual appreciation for each other's beers.

### Question 4: Are beer reviewers the biggest bias?
1. We will identify patterns in beer reviewers' ratings. This will involve computing descriptive statistics for each reviewer's ratings and identifying those who consistently rate high, low, or never below a certain threshold.
2. We will attempt to correct for these biases by decorrelating a reviewer's "niceness" from their beer ratings. This will involve computing for example the standard deviation of each reviewer's ratings and adjusting their ratings accordingly.
3. After these adjustments, we will recompute the 'beer nations' using our methods mentioned above to reflect a less biased perspective of international beer preferences.

#### Data related considerations
- We will tackle the question by choosing the appropriate dataset which contains the beer reviews and user information. Our goal is to analyze patterns and tendencies in reviewers, so we can first start by looking at the distribution of the overall scores per user. Only users with a high number of reviews are considered for statistical significance.
- In the initial assessment, we compare a small group of reviewers through boxplots illustrating the distribution of their overall ratings. We also examine the count of low ratings based on a predetermined threshold. We notice that the ratings are not normally distributed thus making metrics such as the t-test unsuitable.
- Moving forward, our next step involves identifying “too nice users” using the user’s overall rating time series to determine whether it is stationary (in case of high ratings mean and low variance) using the Augmented Dickey-Fuller (ADF) test.
- Sentimental information can be extracted from the reviewer’s text. We use BERT Multilingual Sentimental Analysis pre-trained model to evaluate the textual reviews. The distribution of overall ratings and sentimental analysis scores, assuming similar scales for both, is then compared using the chi-square test to assess similarity.
- A mathematical metric is proposed to provide an “honest score” in case of significant differences between the aforementioned distributions. This will involve creating a new metric that takes into account both the overall ratings and the sentiment analysis scores, and adjusts the ratings accordingly. This new metric will be used to recompute the beer nations.


## ⏲ Proposed timeline
 - Week 9: due on 17 November
	 - [x] Delivery P2
 - Week 10: due on 24 November
	 - [ ] Start and finish work on H2
	 - [ ] Begin working on P3: research question 1
 - Week 11: due on 1 December
	 - [ ] finish P3 research question 1
	 - [ ] begin P3 research question 2
  	 - [ ] begin P3 research question 4	
	 - [ ] Delivery H2
 - Week 12: due on 8 December
	 - [ ] finish P3 research question 2
  	 - [ ] finish P3 research question 4
	 - [ ] begin P3 research question 3
 - Week 13: due on 15 December
	 - [ ] finish P3 research question 3
  	 - [ ] re-assess data using possible objectivity correction
	 - [ ] combine all results in data story
 - Week 14: due on 22 December 
	 - [ ] Fine-tuning of P3
	 - [ ] Delivery P3

## 🤪 Organization within the team
> A list of internal milestones up until project Milestone P3.

- Christopher
   	- [x] Investigate Q3, editing and additions to README
- Eymeric
	- [x] Investigate Q2 (and Q1), data assessment
- Konstantin
	- [x] Creation of the P2 README.md: Writing of abstract, research questions and methods
	- [ ] Data analysis of Q1
- Nina
- Parsa
	- [x] Investigate Q4, data assessment

## ❓ Questions for TAs

- Feedback on timeline feasibility, is our pacing for the project realistic?
- Are there any specific programming libraries you recommend for our methods?
- Are there any ethical considerations or data privacy concerns we should be aware of while conducting our analysis, especially when dealing with user reviews and ratings?
