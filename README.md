## First deploy?

Deploy docker stack:
    docker stack deploy --compose-file docker-compose.yml my_stack


Maybe you want to init the db first. To do that, atach to the idp_2020 docker container and run these steps:
1. Open python by running this command:
    python
2. Import db module from the application:
    from internet_banking import db
3. Create the empty database:
    db.create_all()


