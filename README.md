# Redbus-Project
## Data Scraping with Selenium and Dynamic Filtering using Streamlit

### Objectives
1) To scrape and extract bus route details and bus availability information from the ‘Redbus’ website using selenium for at least 10 states.
2) To store the extracted data in a sql database.
3) To develop an interactive streamlit application demonstrating various filtering options for the extracted data.

### Data extraction using selenium
Data from the redbus website scrapped using selenium with the following steps:
- Dictionary (url_dic) created to map 10 states to their respective RedBus URL, serving as entry points for data scraping.
- Using selenium, automated scraping of state specific bus routes data from multiple pages and route specific bus details for both public and private buses.
- The extracted data is appended to a list of dictionaries (bus_data). 
- Finally, all the collected data saved into a CSV file (final_busdata.csv) with appropriate headers for easy analysis. 

### Data storage in a sql database
- Created a table (bus_routes) schema in Mysql workbench within the existing database “guvi” 
- Imported and loaded the extracted data into the bus_routes table.
![image](https://github.com/user-attachments/assets/2257de22-7c70-4777-95bf-bfa1cec08cbd)

  #### Data Description
    Data set ‘bus_routes’ contains detailed information about buses across 10 states with the following columns:
    - id: unique sequential value 
    - state: name of 10 different states
    - route_name: starting and reaching points of a bus 
    - route_link: url containing public and private buses information for that particular route
    - busname: name of the bus service
    - bustype: bus’s air conditioning and seating type 
    - departing_time: departure time of the bus from the starting point.
    - duration: total duration of the bus journey in hours
    - reaching_time: reaching time of the bus at the destination
    - star_rating: rating (out of 5 stars) given by the passengers
    - price: fare charged for the journey
    - seats_available: number of seats currently available for booking

### Web application using Streamlit
![image](https://github.com/user-attachments/assets/3cf1a93d-bd31-4ecf-96b3-766a427ebe5a)

- Created a user-friendly, interactive webpage using streamlit that allows users to filter and display detailed bus information efficiently. 
- Users can select their state from a dropdown list and can choose their desired bus route from another dropdown.
- Select the rating filter options, the number of seats required and adjust the ticket fare slider to fix the maximum fare range preferred.
- A list of available buses matching the selected filters is displayed for the user to choose a specific bus and click on the respective bus details button. 
- Webpage displays a table with the following information of the selected bus: bus type, departure time, travel duration, star rating and ticket fare. 

### Summary
- Leveraging Selenium, bus information for various routes across 10 states was systematically extracted from the RedBus website.
- The extracted data was stored in a structured SQL database, ensuring efficient organization, deeper understanding and accessibility for future use.
- A Streamlit-based interactive webpage was developed, offering dynamic state and route filtering options for seamless exploration of buses availability.
- This solution combines web scraping, database management, and user interface design to enable a smooth and informative browsing experience, providing a practical tool for visualizing and navigating bus route information.




