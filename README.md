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

<img width="480" alt="image" src="https://github.com/tvamshi8/credit-scoring-and-segmentation/assets/153074595/806e5146-af06-4b83-a3c3-320f397986e8">
<img width="448" alt="image" src="https://github.com/tvamshi8/credit-scoring-and-segmentation/assets/153074595/5c1508d3-dfc1-49bc-b430-6d95ef328e02">


Now let’s have a look at the descriptive statistics of the data:

<img width="472" alt="image" src="https://github.com/tvamshi8/credit-scoring-and-segmentation/assets/153074595/1c015b2b-972a-40e6-9f2f-ad4bcf1efccb">

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







