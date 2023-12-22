# Global Brews, Local Views: Decoding the World's Beer Preferences

## 🍻 **Introduction**

In an era where globalization blends tastes and traditions, beer remains a distinctive symbol of cultural identity and preference. "Global Brews, Local Views" is a deep dive into the effervescent world of beer reviews, where each sip and each rating tells a story not just about the beer, but also about the reviewer. This project is a journey into understanding how personal biases, cultural backgrounds, and national pride shape our perceptions and ratings of beers from around the globe.

## 🌍 **The Essence of Our Exploration**

Our mission is to uncork the hidden dynamics in beer ratings, analyzing how a reviewer's personal preferences, their nationality, and their beer review history might skew their ratings. We're not just studying beers; we're exploring how people's backgrounds and biases influence their taste.

## 🔍 **Structure and Scope of the Journal**

1. **Unveiling Beer Nations**: We will start by mapping out the beer landscape, identifying countries with high average ratings, and understanding how different aspects like taste and appearance contribute to these ratings. This section will also explore if there's a correlation between a country's beer diversity and its ratings.

2. **International Beer Relations (IBR)**: Here, we will examine the global influence of beers. Which countries' beers are most celebrated abroad? Is there evidence of mutual beer admiration between certain nations? This section aims to unravel the diplomatic ties in the beer world.

3. **Bias in Beer Reviews**: The final section will delve into the psychology of beer reviewers. Are some reviewers consistently more generous or harsh? We will attempt to adjust for these biases and re-evaluate our earlier findings to see if the landscape of beer nations shifts.

## 📝 **Progress and Reflections**: 
This journal will document our progress, challenges, and discoveries. It will be a living record of our exploration into the world of beer ratings, reflecting not only what we learn about beer but also about human nature. Each section will be underpinned by rigorous data analysis. We'll use statistical tools to dissect and interpret the data, ensuring our insights are as robust as they are intriguing.

So, let's raise our glasses to a journey of discovery, where data meets draughts, and insights flow as freely as ale. Welcome to "Global Brews, Local Views"! 🍺

## Question 1: Where are the Beer Nations?

### 📚 **Understanding the Data**

#### **The Source**
Our journey into the world of beer ratings begins with the data sourced from RateBeer, an American website celebrated for its comprehensive and accurate information on beer. RateBeer has established itself as a pivotal online community for craft beer enthusiasts, focusing on beer education and unbiased ratings.

#### **Rating Dynamics**
On RateBeer, users can rate beers across four key aspects: appearance, aroma, palate, and taste. Additionally, they can provide textual reviews to share their nuanced opinions. Crucially, users can also disclose their country of origin, offering us a valuable dimension for analysis.

### 🌾 **Sifting Through the Data**

#### **User Participation**
A preliminary glance reveals a range of user engagement levels. Many users leave only one or a handful of ratings. For our analysis, particularly in identifying favorite beer styles per country, these sporadic ratings offer limited insight.

#### **Threshold for Inclusion**
To ensure meaningful and reliable conclusions, we adopt a dual threshold approach. Users with fewer than eight ratings and countries represented by fewer than ten users are filtered out. This balance between data abundance and quality is crucial for our analysis.

### 🌍 **Examining the Remaining Countries**

#### **Diverse Participation**
Post-filtration, we're left with a globally diverse set of countries, each with a significant user base contributing to the beer ratings. This allows us to delve into the data with confidence, knowing that our insights will be representative of a broader spectrum of beer enthusiasts.

#### **Upcoming Analyses**
Our next steps involve deep dives into understanding the favorite beer styles in these countries, exploring regional preferences, and uncovering global trends. We aim to paint a picture not just of the beers themselves, but of the cultural and personal preferences that shape the world's beer landscape.

### 🍺 **A Toast to Data-Driven Insights**
This initial stage sets the groundwork for our exploration into the "Beer Nations." It's a celebration of diversity, both in beer styles and in the global community of those who love them. Let's raise our glasses to the insights awaiting us in the pages ahead!


## Question 2: IBR - International Beer Relations

### 🌐 **Exploring the Geography of Beer**

#### **Understanding International Beer Dynamics**
In our quest to explore the international relations in the beer world, we delve into four intriguing aspects:
1. The origins of the majority of ratings for each nation's beers.
2. The global popularity of certain countries' beers.
3. The existence of a 'Beer Union' - countries mutually appreciative of each other's brews.
4. The presence of domestic beer pride - do users favor beers brewed in their home country?

#### **Data Cleaning and Preparation**
Before delving into these questions, our first step is meticulous data cleaning and preparation. By mapping user and brewery locations to our ratings dataset, we distinguish between local and international ratings, setting the stage for a nuanced analysis.

### **Local vs. International Beer Appreciation: A Closer Look**

![Top_3 rating counts for user countries](https://github.com/epfl-ada/ada-2023-project-renensgang1020/blob/main/docs/assets/img/ratings_user_country_top_3.png)

#### **The American Influence in Beer Ratings**
A striking aspect of our data analysis reveals the substantial influence of the United States in the beer rating world. This dominance is twofold:
- **Domestic Ratings**: American users lead in reviewing beers produced within the United States, with an astonishing 472,769 ratings.
- **International Focus**: Interestingly, American users are also prolific in rating international beers. A notable example is Belgian beers, which received 51,241 ratings from U.S. users.

#### **Top Rating Dynamics**
The analysis uncovers the top types of beer ratings based on their volume, illustrating a clear trend in user preferences and access:
- **U.S. Dominance in Domestic Reviews**: The majority of reviews are from U.S. users rating U.S. beers, indicating a strong domestic market.
- **Cross-Cultural Appreciation**: Belgian beers are highly rated by U.S. users, second only to their domestic ratings, suggesting a keen American interest in Belgian brews.
- **Canadian and UK Loyalties**: Canadian users predominantly rate Canadian beers (46,059 ratings), and UK users show a similar trend with 32,263 ratings for UK beers.

#### **Understanding Review Patterns**
This pattern where most reviews for each brewery come from users in the same country aligns with expectations - domestic users typically have greater access to their local brews. However, the dataset shows a significant skew towards U.S. users, reflected in the volume of their reviews, both domestic and international.

#### **Implications of Data Skew**
Such a skew suggests that the dataset may not fully represent global beer preferences but is heavily influenced by American users' activity on the review website. For instance, while there are more reviews of Belgian beers by U.S. users than by Belgians themselves, this likely reflects the higher number of American users on the platform rather than a definitive statement about the popularity of Belgian beers in the U.S.

#### **Mapping Beer Diplomacy**
By visualizing these international beer relations, we shed light on how beer appreciation transcends borders. The web of ratings paints a picture of global beer diplomacy.
![map](https://github.com/epfl-ada/ada-2023-project-renensgang1020/blob/main/docs/assets/img/map.png)

### 🍻 **Which Country’s Beers Win Hearts Worldwide?**
Our analysis uncovers that Belgium, the US, and the UK lead in terms of international review counts. However, when we consider the proportion of international reviews, non-English speaking countries surprisingly emerge as significant players in the global beer scene.

#### **A Deeper Dive into Popularity**
We also examine the average ratings of beers on an international scale. This approach reveals countries like Malaysia and Tanzania receiving high international acclaim, suggesting a niche but significant global presence.

### 🌐 **Uncovering the Beer Union**
To probe the existence of a 'Beer Union', we utilize network analysis. This method illustrates the beer rating relationships between countries. Interestingly, the data reveals isolated instances of mutual beer appreciation rather than a broad 'Beer Union'. The United States, due to the data skew, appears as a central node in this network.

### 🏆 **Domestic Beer Pride: A Statistical Analysis**
Lastly, we address the bias towards domestic beers. Our statistical analysis, including a Welch's t-test, indicates a marginal but statistically significant preference for domestic beers. The domestic ratings slightly edge out the international ones, affirming the subtle influence of national pride in beer ratings.

#### **Visual and Statistical Tools**
In our endeavor to understand this domestic preference, we employ a combination of histograms, Q-Q plots, and t-tests. These tools collectively strengthen our conclusion about the domestic rating bias.

## Question: 3 Are beer reviewers the biggest bias?

#### 📚***Lets take a closer look at the ratings data*** 

To gain an initial advantage, we begin by identifying the top 10 users boasting the highest volume of reviews, and proceed to visualize the distribution of their ratings. This preliminary examination serves as a swift and essential sanity check, offering valuable insights into the diverse rating patterns exhibited by these influential contributors. By delving into the nuances of their rating distributions, we lay the foundation for a more comprehensive analysis, aiming to unravel noteworthy trends and variations that may shape our understanding of user preferences and experiences.



![q3_boxplt](https://github.com/epfl-ada/ada-2023-project-renensgang1020/blob/main/docs/assets/img/q3_boxplt.png)


#### ***How are we going to identify nice users ?*** 

We establish the criteria for categorizing users as 'nice users,' defined as individuals who consistently provide ratings above a specified threshold. The process involves the following steps:
Rating Threshold Definition: Initially, we set a rating threshold (3/5), considering ratings above this threshold as 'good.'
Counting 'Bad' Ratings: Subsequently, we tally the number of 'bad' ratings (those falling below the defined threshold) for each user. We compute the ratio of 'bad' ratings to the total number of ratings per user.
Percentage Threshold Application: If the computed ratio is below a predetermined percentage threshold (set at 15%), the user qualifies as a potential 'nice user.'
Consistency Check - ADF Test: To further ascertain if the user consistently provides good ratings, we conduct an Augmented Dickey-Fuller (ADF) test on the user's rating data. The Null Hypothesis of the ADF test posits that the time series is non-stationary. Consequently, a sufficiently small P-value leads to the rejection of the null hypothesis.
Nice User Identification: Users meeting the criteria in steps 3 and 4 are identified as nice users.
This comprehensive approach ensures a rigorous evaluation of users based on both their rating patterns and the statistical properties of their rating time series, contributing to the identification of consistently positive contributors to the platform. The above analysis results in a total of 1419 nice users. 


### ***Sentimental analysis on text reviews is a viable solution***
he extraction of sentimental information from reviewer texts is achieved through a meticulous process, calibrated to a scale comparable to the user ratings assigned to the beers. To demonstrate the viability of this methodology, we have opted to analyze the reviews of a single user, with the understanding that the approach is scalable to the entire dataset.
In this endeavor, we employ the BERT Multilingual Sentiment Analysis pretrained model. This robust model has undergone training on Wikipedia pages across 104 languages, ensuring a broad linguistic coverage. The selection of this model is deliberate, driven by the objective of encompassing diverse languages within the dataset. For further details on BERT Multilingual Sentiment Analysis, refer to: BERT Multilingual Sentiment Analysis.
Coincidentally, the sentimental scale utilized by this classifier ranges from 0 to 5, mirroring the scale of beer ratings. It is noteworthy that, while both scales share the same range, the sentimental classification is categorical in nature. This alignment facilitates a seamless comparison between the sentiments derived from the reviews and the numerical beer ratings, enhancing the interpretability of the analysis. The proof of concept, focusing on a single user, serves as a compelling illustration of the method's potential, which can be effortlessly extended to encompass the entirety of the dataset
As a preliminary sanity check, we initiate the analysis by selecting a compact subset comprising the initial five users from the collected nice users in the previous step. This judicious choice allows us to focus on a manageable sample size for thorough examination. By scrutinizing the sentiment analysis results of these users, we aim to ensure the reliability and coherence of the derived sentimental information. This preliminary step lays the groundwork for a more extensive evaluation of the entire 'nice_users' list, affirming the robustness of our approach in identifying consistently positive contributors based on both user ratings and sentiment analysis of their reviews.
The resulting distributions can be seen below: 

![q_3violon1](https://github.com/epfl-ada/ada-2023-project-renensgang1020/blob/main/docs/assets/img/q_3violon1.png)


### 📝***Lets Correcting reviewers niceness by a balancing formula***
The introduction of the interpolated rating (ir) as a balancing metric serves as a pivotal step in reconciling the potential biases inherent in reviewer assessments. This metric, encapsulated by the formula :
**ir =rating⋅(1−α)+sentiment_rating⋅α**
This elegantly blends the numerical ratings provided by users with the sentiment analysis scores derived from their textual reviews.
The choice of the balancing coefficient αα is pivotal in fine-tuning the interpolation process. When the distributions of ratings and sentiment_rating closely align, α assumes a neutral value of 0.5. This signifies a balanced contribution of both numerical scores and sentiment analysis to the interpolated rating.
In cases where a reviewer exhibits a tendency to overrate, as evidenced by disparities in the distributions of ratings and sentiment_rating, α takes a value greater than 0.5. Conversely, if a reviewer tends to underrate based on distribution differences, α is set to a value less than 0.5.
This nuanced approach allows for a dynamic adjustment, enabling the calibration of the interpolated rating to the unique reviewing tendencies of each user. By incorporating sentiment analysis alongside numerical ratings, this metric provides a more comprehensive and balanced evaluation of the user's overall sentiment towards the beers they review.
The final comparison of the initial ratings, sentimental analysis score on the text, and the interpolated rating  can be found below:

![q_3violon2](https://github.com/epfl-ada/ada-2023-project-renensgang1020/blob/main/docs/assets/img/q_3violon2.png)


### 🌐***How does the interpolated ratings effect the beer nations***

Unfortunately, the extension of this balancing metric to the entire dataset was impeded by constraints on computational resources. Consequently, we were unable to replicate the analysis conducted in the initial step, hindering our ability to observe the impact of the balanced ratings on the results and draw comparisons with the initial findings. Despite this constraint, the localized application of the balancing metric to a subset or specific user categories could still yield valuable insights and provide a foundation for future analyses..

