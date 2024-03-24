# credit-scoring-and-segmentation
Credit Scoring and Segmentation: Overview
The process of calculating credit scores and segmenting customers based on their credit scores involves several steps. Firstly, relevant data about borrowers, such as payment history, credit utilization, credit history, and credit mix, is collected and organized. Then, using complex algorithms and statistical models, the collected data is analyzed to generate credit scores for each borrower.

These credit scores are numerical representations of the borrower’s creditworthiness and indicate the likelihood of default or timely repayment. Once the credit scores are calculated, customers are segmented into different risk categories or credit tiers based on predefined thresholds.

This segmentation helps financial institutions assess the credit risk associated with each customer and make informed decisions regarding loan approvals, interest rates, and credit limits. By categorizing customers into segments, financial institutions can better manage their lending portfolios and effectively mitigate the risk of potential defaults. The data set is uploaded in the repository.

Below is the description of all the features in the data:

Age: This feature represents the age of the individual.
Gender: This feature captures the gender of the individual.
Marital Status: This feature denotes the marital status of the individual.
Education Level: This feature represents the highest level of education attained by the individual.
Employment Status: This feature indicates the current employment status of the individual.
Credit Utilization Ratio: This feature reflects the ratio of credit used by the individual compared to their total available credit limit.
Payment History: It represents the monthly net payment behaviour of each customer, taking into account factors such as on-time payments, late payments, missed payments, and defaults.
Number of Credit Accounts: It represents the count of active credit accounts the person holds.
Loan Amount: It indicates the monetary value of the loan.
Interest Rate: This feature represents the interest rate associated with the loan.
Loan Term: This feature denotes the duration or term of the loan.
Type of Loan: It includes categories like “Personal Loan,” “Auto Loan,” or potentially other types of loans.

Now let’s have a look at column insights before moving forward:

<class 'pandas.core.frame.DataFrame'>

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1000 entries, 0 to 999
Data columns (total 12 columns):
 #   Column                     Non-Null Count  Dtype  
---  ------                     --------------  -----  
 0   Age                        1000 non-null   int64  
 1   Gender                     1000 non-null   object 
 2   Marital Status             1000 non-null   object 
 3   Education Level            1000 non-null   object 
 4   Employment Status          1000 non-null   object 
 5   Credit Utilization Ratio   1000 non-null   float64
 6   Payment History            1000 non-null   float64
 7   Number of Credit Accounts  1000 non-null   int64  
 8   Loan Amount                1000 non-null   int64  
 9   Interest Rate              1000 non-null   float64
 10  Loan Term                  1000 non-null   int64  
 11  Type of Loan               1000 non-null   object 
dtypes: float64(3), int64(4), object(5)

Now let’s have a look at the descriptive statistics of the data:

Age  Credit Utilization Ratio  Payment History  \
count  1000.000000               1000.000000      1000.000000   
mean     42.702000                  0.509950      1452.814000   
std      13.266771                  0.291057       827.934146   
min      20.000000                  0.000000         0.000000   
25%      31.000000                  0.250000       763.750000   
50%      42.000000                  0.530000      1428.000000   
75%      54.000000                  0.750000      2142.000000   
max      65.000000                  1.000000      2857.000000   

       Number of Credit Accounts   Loan Amount  Interest Rate    Loan Term  
count                1000.000000  1.000000e+03    1000.000000  1000.000000  
mean                    5.580000  2.471401e+06      10.686600    37.128000  
std                     2.933634  1.387047e+06       5.479058    17.436274  
min                     1.000000  1.080000e+05       1.010000    12.000000  
25%                     3.000000  1.298000e+06       6.022500    24.000000  
50%                     6.000000  2.437500e+06      10.705000    36.000000  
75%                     8.000000  3.653250e+06      15.440000    48.000000  
max                    10.000000  4.996000e+06      19.990000    60.000000  

Now let’s have a look at the distribution of the credit utilization ratio in the data:

![image](https://github.com/tvamshi8/credit-scoring-and-segmentation/assets/153074595/6227db40-5ef9-46ad-aca7-28d742cc3b65)

Now let’s have a look at the distribution of the loan amount in the data:

![image](https://github.com/tvamshi8/credit-scoring-and-segmentation/assets/153074595/59e08915-ee8b-4f26-868d-e4b7f00bf6b3)

Now let’s have a look at the correlation in the data:

![image](https://github.com/tvamshi8/credit-scoring-and-segmentation/assets/153074595/c1ef74cc-3f3a-43fa-94df-9658a6da442a)

Calculating Credit Scores
The dataset doesn’t have any feature representing the credit scores of individuals. To calculate the credit scores, we need to use an appropriate technique. There are several widely used techniques for calculating credit scores, each with its own calculation process. One example is the FICO score, a commonly used credit scoring model in the industry.

Below is how we can implement the FICO score method to calculate credit scores:


   Age  Gender Marital Status  Education Level  Employment Status  \
0   60    Male        Married                3                  1   
1   25    Male        Married                1                  0   
2   30  Female         Single                3                  1   
3   58  Female        Married                4                  0   
4   32    Male        Married                2                  2   

   Credit Utilization Ratio  Payment History  Number of Credit Accounts  \
0                      0.22           2685.0                          2   
1                      0.20           2371.0                          9   
2                      0.22           2771.0                          6   
3                      0.12           1371.0                          2   
4                      0.99            828.0                          2   

   Loan Amount  Interest Rate  Loan Term   Type of Loan  Credit Score  
0      4675000           2.65         48  Personal Loan       940.516  
1      3619000           5.19         60      Auto Loan       831.360  
2       957000           2.76         12      Auto Loan       971.216  
3      4731000           6.57         60      Auto Loan       480.586  
4      3289000           6.28         36  Personal Loan       290.797 

Segmentation Based on Credit Scores
Now, let’s use the KMeans clustering algorithm to segment customers based on their credit scores:

![image](https://github.com/tvamshi8/credit-scoring-and-segmentation/assets/153074595/1a541e6a-e646-4298-80e9-c0b85f791d27)

Now let’s name the segments based on the above clusters and have a look at the segments again:

![image](https://github.com/tvamshi8/credit-scoring-and-segmentation/assets/153074595/03d0106d-400e-47d4-b1a4-a137edfbdb29)

Summary:
Credit scoring and segmentation refer to the process of evaluating the creditworthiness of individuals or businesses and dividing them into distinct groups based on their credit profiles. It aims to assess the likelihood of borrowers repaying their debts and helps financial institutions make informed decisions regarding lending and managing credit risk.







