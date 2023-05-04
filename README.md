# DE-ZOOMCAMP-PROJECT
## Project Title: "Building a Data Pipeline Analysis of MotoGP Racing Data"
![MOTOGP](https://github.com/Manny-97/DE-ZOOMCAMP-PROJECT/blob/5ce7e982141457968f9350ac37f2aad5dc29a22d/images/rossi1.png)
## Objective

Project description
In this project, we will scrape data from the MotoGP website and perform data engineering tasks to clean and prepare the data for analysis. The data will include race results over the years. Once the data is cleaned and prepared, we will perform exploratory data analysis and visualization to gain insights into the data.

## Architecture

![Project pipeline](https://d2908q01vomqb2.cloudfront.net/b6692ea5df920cad691c20319a6fffd7a4a766b8/2020/09/21/serverless-analytics-pipeline-2-840x630.jpg)

## Problem statement
Motorsports have a massive global following, and MotoGP is one of the most popular motorsport events worldwide. MotoGP race results are crucial data for fans, teams, and sponsors as they help to evaluate a rider's performance and make informed decisions about future strategies.

Currently, the data for MotoGP race results are scattered across different sources and formats, which makes it difficult to get meaningful insights. There is a need to set up a data pipeline to collect, process, and store the race results data in a structured format to facilitate analysis and reporting.

Moreover, there is a need to create a dashboard that presents the top-performing riders and bike manufacturers by country and circuit, as well as a summary of past race results. The dashboard will provide insights into the trends and patterns of MotoGP race results, helping teams, sponsors, and fans make informed decisions.


## Main objective
To address the problem, we propose setting up a data pipeline that collects and processes MotoGP race results data from different sources and stores it in a centralized Redshift database. We will use tools like Python and BeautifulSoup to scrape data from the MotoGP website and load it into the database.

Next, we will transform and aggregate the data using DBT to create models that answer questions such as "What are the top performing riders/teams in the current season by country and circuit?" and "Which bike manufacturer has the highest win rate by season and ride class?"

Finally, we will create a dashboard using Looker that presents the results in an easy-to-understand format. The dashboard will provide a summary of past race results and insights into the top-performing riders and bike manufacturers by country and circuit. This dashboard will be accessible to stakeholders like teams, sponsors, and fans, who can use it to make informed decisions about their future strategies.


## Dataset description
![Table](https://github.com/Manny-97/DE-ZOOMCAMP-PROJECT/blob/396add24aaa033b62f4cb90528663ca805b5c0a6/images/redshift.png)
1. `name`: This column represents the name of the rider who won the Grand Prix race.

2. `season`: This column represents the season or year in which the race took place.

3. `country`: This column represents the country in which the race was held.

4. `circuit`: This column represents the name of the circuit where the race was held.

5. `constructor`: This column represents the name of the bike manufacturer that the rider used to win the race.

6. `ride_class`: This column represents the classification of the race.

The dataset provides information about the winners of the races, including their name, the year the race was held, the country where the race was held, the circuit where the race was held, the manufacturer of the motorcycle used, and the classification of the race. The data can be used to analyze the performance of riders, the success of bike manufacturers, the popularity of circuits, and the differences in performance between different classification of races.

## Proposal

## Dashboard
![A Simple Dashboard](https://github.com/Manny-97/DE-ZOOMCAMP-PROJECT/blob/726a4e61a9d7dc30f4ec4209386b3ef768632458/images/Motogp_Report.png)
![Greatest Riders](https://github.com/Manny-97/DE-ZOOMCAMP-PROJECT/blob/5c8ecaac575afab0db4b96cd99bd647180e9826e/images/Motogp_Goats.png)

## Inference

![Valentino Rossi](https://github.com/Manny-97/DE-ZOOMCAMP-PROJECT/blob/06109ba453390ff30e997f38d17b49a434929e1d/images/valentino_rossi.webp)

![Marc Marquez](https://github.com/Manny-97/DE-ZOOMCAMP-PROJECT/blob/5ce7e982141457968f9350ac37f2aad5dc29a22d/images/marquez.jpg)


### Technologies
- Language: Python
- Cloud: AWS
- Containerization: Docker
- Infrastructure as a code (IaaC): Terraform
- Workflow orchestration: Prefect (ingestion pipeline and transformation pipeline)
- Data Warehouse: Amazon Redshift
- Data Lake: S3
- Batch processing/Transformations: dbt cloud
- Dashboard: Looker Studio
- Stream processing: Kafka


## Acknowledgments

Embarking on any journey can be a daunting task, but as the saying goes, "part of the journey is the end." Reflecting on this phrase, I cannot express enough how truly grateful I am for the unwavering support and guidance of this exceptional group of individuals. Their commitment to helping me grasp the intricacies of data and analytics engineering has been nothing short of remarkable. I am indebted to them for the time, effort, and expertise they have generously invested in me, paving the way for a successful journey.

* [Alexey Grigorev](https://www.linkedin.com/in/agrigorev/)
* [Ankush Khanna](https://www.linkedin.com/in/ankushkhanna2/)
* [Sejal Vaidya](https://www.linkedin.com/in/vaidyasejal/)
* [Victoria Perez Mola](https://www.linkedin.com/in/victoriaperezmola/)
* [Olamide Adesoba](https://www.linkedin.com/in/adesoba-olamide-gmnse-787193169/)
* [Irem Ertürk](https://www.linkedin.com/in/iremerturk/)
* []()
* []()
* **Adebisi, Adefunke, and Adedoja, you are my inspiration.**

## Contact

* [Muhammed Jimoh](https://www.linkedin.com/in/muhammed-jimoh-45120a14a/)

Project Link: [Capstone Project](https://github.com/Manny-97/DE-ZOOMCAMP-PROJECT)
