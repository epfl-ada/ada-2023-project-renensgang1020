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

![Top_3 rating counts for user countries](https://github.com/epfl-ada/ada-2023-project-renensgang1020/blob/main/docs/assets/img/ratings_user_country_top_3.png)

#### **Understanding International Beer Dynamics**
In our quest to explore the international relations in the beer world, we delve into four intriguing aspects:
1. The origins of the majority of ratings for each nation's beers.
2. The global popularity of certain countries' beers.
3. The existence of a 'Beer Union' - countries mutually appreciative of each other's brews.
4. The presence of domestic beer pride - do users favor beers brewed in their home country?

#### **Data Cleaning and Preparation**
Before delving into these questions, our first step is meticulous data cleaning and preparation. By mapping user and brewery locations to our ratings dataset, we distinguish between local and international ratings, setting the stage for a nuanced analysis.

### **Local vs. International Beer Appreciation: A Closer Look**

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





