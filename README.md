This project is a multivariate retention rate predictor. It predicts if the podcast will retain viewers.
This project can be thought as a performance assesment for podcasts to improve viewer retention.
I used docker to create a postgresSQL database to house and transform the predictive data.
Alembic is used the log changes to the database schema and make it easy to revert changes.
Streamlit is implemeted to give users a little bit of an interactive feel. I also used Render to deploy the service.
The model is trained so the user can drop in data and get back predictions from the deployed serivce.
