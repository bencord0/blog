docker-compose up -d
docker-compose exec blog bash -c \
  'git clone https://github.com/bencord0/blogposts; sleep 5; \
   blog manage migrate && blog manage import_entries /blogposts'
docker-compose logs -f
docker-compose down