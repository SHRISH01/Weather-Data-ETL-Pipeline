<h1>Weather Data ETL Pipeline</h1>

<p>Welcome to the <strong>Weather Data ETL Pipeline</strong>! This project demonstrates an ETL (Extract, Transform, Load) pipeline built with Python, using data extracted from the OpenWeather API, transformed for analytics, and loaded into AWS S3 in JSON format. This repository is ideal for anyone interested in working with real-time weather data and handling ETL processes in cloud storage.</p>

<hr>

<h2>Project Overview</h2>
<p>This ETL pipeline performs the following steps:</p>
<ol>
  <li><strong>Extract:</strong> Retrieves weather data from the OpenWeather API.</li>
  <li><strong>Transform:</strong> Cleanses and formats the data using Python.</li>
  <li><strong>Load:</strong> Uploads the transformed data to an AWS S3 bucket in JSON format.</li>
</ol>
<p>This pipeline can be scheduled regularly, making it suitable for use cases like weather forecasting, climate analysis, and environmental monitoring.</p>

<hr>

<h2>Features</h2>
<ul>
  <li><strong>Real-Time Weather Data:</strong> Fetches current weather data directly from OpenWeather API.</li>
  <li><strong>Data Transformation:</strong> Data is processed in Python to ensure consistency and readiness for analytics.</li>
  <li><strong>AWS S3 Storage:</strong> Stores the transformed data in S3 for scalable, cloud-based access.</li>
</ul>

<hr>

<h2>Table of Contents</h2>
<ol>
  <li><a href="#requirements">Requirements</a></li>
  <li><a href="#installation">Installation</a></li>
  <li><a href="#configuration">Configuration</a></li>
  <li><a href="#usage">Usage</a></li>
  <li><a href="#project-structure">Project Structure</a></li>
  <li><a href="#data-example">Data Example</a></li>
  <li><a href="#future-enhancements">Future Enhancements</a></li>
  <li><a href="#license">License</a></li>
</ol>

<hr>

<h2 id="requirements">Requirements</h2>
<p>To run this ETL pipeline, you need:</p>
<ul>
  <li><strong>Python 3.8+</strong></li>
  <li><strong>AWS CLI</strong> (configured with access keys for S3)</li>
  <li><strong>AWS S3 Bucket</strong> (configured and ready for data storage)</li>
  <li><strong>OpenWeather API Key</strong></li>
</ul>

<hr>

<h2 id="installation">Installation</h2>
<p>Clone the repository and install the required packages:</p>
<pre><code>git clone https://github.com/yourusername/weather-data-etl.git
cd weather-data-etl
pip install -r requirements.txt
</code></pre>

<hr>

<h2 id="configuration">Configuration</h2>
<ol>
  <li><strong>OpenWeather API Key:</strong> Register on <a href="https://openweathermap.org/api">OpenWeather</a> and obtain an API key.</li>
  <li><strong>AWS Configuration:</strong> Ensure your AWS CLI is configured with credentials:
    <pre><code>aws configure</code></pre>
  </li>
  <li><strong>Environment Variables:</strong> Create a <code>.env</code> file in the project root and add the following:
    <pre><code>OPENWEATHER_API_KEY=your_openweather_api_key
S3_BUCKET_NAME=your_s3_bucket_name
</code></pre>
  </li>
</ol>

<hr>

<h2 id="usage">Usage</h2>
<p>Run the ETL pipeline using:</p>
<pre><code>python etl_pipeline.py</code></pre>
<p>This script:</p>
<ol>
  <li>Fetches data from OpenWeather API.</li>
  <li>Transforms the data (filtering and formatting).</li>
  <li>Loads the data into the specified AWS S3 bucket in JSON format.</li>
</ol>

<hr>

<h2 id="project-structure">Project Structure</h2>
<pre><code>weather-data-etl/
├── data/
├── etl_pipeline.py         # Main ETL script
├── requirements.txt
├── README.md
└── .env                    # Environment variables
</code></pre>
<ul>
  <li><strong>data/</strong>: Folder for local storage (optional).</li>
  <li><strong>etl_pipeline.py</strong>: Main ETL script that orchestrates data extraction, transformation, and loading.</li>
</ul>

<hr>

<h2 id="data-example">Data Example</h2>
<p>Sample JSON format of weather data stored in S3:</p>
<pre><code>{
  "city": "San Francisco",
  "temperature": 15.2,
  "humidity": 82,
  "pressure": 1012,
  "wind_speed": 4.5,
  "weather_description": "Cloudy",
  "timestamp": "2024-11-13T12:00:00Z"
}
</code></pre>

<hr>

<h2 id="future-enhancements">Future Enhancements</h2>
<ul>
  <li><strong>Data Scheduling:</strong> Set up a scheduler (e.g., Apache Airflow) to automate regular data ingestion.</li>
  <li><strong>Data Analysis:</strong> Add an analytics module to provide insights directly from the S3 data.</li>
  <li><strong>Database Storage:</strong> Integrate with a database for long-term storage and querying.</li>
</ul>

<hr>

<h2 id="license">License</h2>
<p>This project is licensed under the Apache License 2.0.</p>

<hr>

<p><strong>Happy Coding!</strong> 🌦️</p>
