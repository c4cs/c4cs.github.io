FROM ubuntu:18.10

RUN apt-get update && apt-get install -y git ruby ruby-dev build-essential patch zlib1g-dev liblzma-dev nodejs
RUN gem install jekyll bundler

COPY Gemfile* /tmp/
WORKDIR /tmp
RUN bundle install

WORKDIR /site

EXPOSE 4000

CMD ["bundle", "exec", "jekyll", "serve", "--force-polling", "-H", "0.0.0.0", "-P", "4000"]
