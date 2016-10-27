from django.db import models


class Master(models.Model):
    player_code = models.CharField(max_length=150, null=True, blank=True)
    birth_year = models.CharField(max_length=150, null=True, blank=True)
    birth_day = models.CharField(max_length=150, null=True, blank=True)
    birth_country = models.CharField(max_length=150, null=True, blank=True)
    birth_state = models.CharField(max_length=150, null=True, blank=True)
    birth_city = models.CharField(max_length=150, null=True, blank=True)
    death_year = models.CharField(max_length=150, null=True, blank=True)
    death_month = models.CharField(max_length=50, null=True, blank=True)
    death_day = models.CharField(max_length=150, null=True, blank=True)
    death_country = models.CharField(max_length=150, null=True, blank=True)
    death_state = models.CharField(max_length=150, null=True, blank=True)
    death_city = models.CharField(max_length=150, null=True, blank=True)
    name_first = models.CharField(max_length=150, null=True, blank=True)
    name_last = models.CharField(max_length=150, null=True, blank=True)
    name_given = models.CharField(max_length=150, null=True, blank=True)
    weight = models.CharField(max_length=150, null=True, blank=True)
    height = models.CharField(max_length=75, null=True, blank=True)
    bats = models.CharField(max_length=75, null=True, blank=True)
    throws = models.CharField(max_length=75, null=True, blank=True)
    debut = models.CharField(max_length=75, null=True, blank=True)
    final_game = models.CharField(max_length=75, null=True, blank=True)
    retro_code = models.CharField(max_length=75, null=True, blank=True)
    bbref_code = models.CharField(max_length=75, null=True, blank=True)

    def __str__(self):
        return self.name_first


class Batting(models.Model):
    player_code = models.ForeignKey(Master)
    year_code = models.CharField(max_length=150, null=True, blank=True)
    stint = models.CharField(max_length=150, null=True, blank=True)
    team_code = models.CharField(max_length=75, blank=True)
    league_code = models.CharField(max_length=75, blank=True)
    games = models.CharField(max_length=75, blank=True)
    at_bats = models.CharField(max_length=150, null=True, blank=True)
    runs = models.CharField(max_length=150, null=True, blank=True)
    hits = models.CharField(max_length=150, null=True, blank=True)
    doubles = models.CharField(max_length=150, null=True, blank=True)
    triples = models.CharField(max_length=150, null=True, blank=True)
    homeruns = models.CharField(max_length=150, null=True, blank=True)
    rbis = models.CharField(max_length=150, null=True, blank=True)
    stolen_base = models.CharField(max_length=150, null=True, blank=True)
    caught_stealing = models.CharField(max_length=150, null=True, blank=True)
    base_on_balls = models.CharField(max_length=150, null=True, blank=True)
    strikeouts = models.CharField(max_length=150, null=True, blank=True)
    intent_walk = models.CharField(max_length=150, null=True, blank=True)
    hit_by_pitch = models.CharField(max_length=150, null=True, blank=True)
    sacrifice_hits = models.CharField(max_length=150, null=True, blank=True)
    sacrifice_fly = models.CharField(max_length=150, null=True, blank=True)
    ground_double_play = models.CharField(max_length=150, null=True, blank=True)

    def on_base(self):
        num_1 = float(int(self.hits.replace('', '0')) + int(self.base_on_balls.replace('', '0')) + int(self.hit_by_pitch.replace('', '0')))
        num_2 = float(int(self.at_bats.replace('', '0')) + int(self.base_on_balls.replace('', '0')) + int(self.hit_by_pitch.replace('', '0')) + int(self.sacrifice_fly.replace('', '0')))
        return num_1 / num_2

    def __str__(self):
        return self.team_code


class Pitching(models.Model):
    player_code = models.ForeignKey(Master)
    year_code = models.CharField(max_length=150, null=True, blank=True)
    stint = models.CharField(max_length=150, null=True, blank=True)
    team_code = models.CharField(max_length=75, null=True, blank=True)
    league_code = models.CharField(max_length=75, null=True, blank=True)
    wins = models.CharField(max_length=150, null=True, blank=True)
    losses = models.CharField(max_length=150, null=True, blank=True)
    games = models.CharField(max_length=150, null=True, blank=True)
    games_started = models.CharField(max_length=150, null=True, blank=True)
    complete_games = models.CharField(max_length=150, null=True, blank=True)
    shutouts = models.CharField(max_length=150, null=True, blank=True)
    saves = models.CharField(max_length=150, null=True, blank=True)
    outs_pitched = models.CharField(max_length=150, null=True, blank=True)
    hits = models.CharField(max_length=150, null=True, blank=True)
    earned_runs = models.CharField(max_length=150, null=True, blank=True)
    homeruns = models.CharField(max_length=150, null=True, blank=True)
    walks = models.CharField(max_length=150, null=True, blank=True)
    strikeouts = models.CharField(max_length=150, null=True, blank=True)
    opponent_batting_avg = models.CharField(max_length=150, null=True, blank=True)
    earned_run_avg = models.CharField(max_length=150, null=True, blank=True)
    intentional_walks = models.CharField(max_length=150, null=True, blank=True)
    wild_pitch = models.CharField(max_length=150, null=True, blank=True)
    batter_hit_by_pitch = models.CharField(max_length=150, null=True, blank=True)
    balks = models.CharField(max_length=150, null=True, blank=True)
    batter_faced_by_pitcher = models.CharField(max_length=150, null=True, blank=True)
    games_finished = models.CharField(max_length=150, null=True, blank=True)
    runs_allowed = models.CharField(max_length=150, null=True, blank=True)
    sacrifice_opp_batter = models.CharField(max_length=150, null=True, blank=True)
    sacrifice_fly_opp_batter = models.CharField(max_length=150, null=True, blank=True)
    ground_double_play_opp_batter = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.team_code


class Fielding(models.Model):
    player_code = models.ForeignKey(Master)
    year_code = models.CharField(max_length=150, null=True, blank=True)
    stint = models.CharField(max_length=150, null=True, blank=True)
    team_code = models.CharField(max_length=150, null=True)
    league_code = models.CharField(max_length=150, null=True, blank=True)
    position = models.CharField(max_length=150, null=True, blank=True)
    games = models.CharField(max_length=150, null=True, blank=True)
    games_started = models.CharField(max_length=150, null=True, blank=True)
    time_in_field = models.CharField(max_length=150, null=True, blank=True)
    putouts = models.CharField(max_length=150, null=True, blank=True)
    assists = models.CharField(max_length=150, null=True, blank=True)
    errors = models.CharField(max_length=150, null=True, blank=True)
    double_plays = models.CharField(max_length=150, null=True, blank=True)
    passed_balls = models.CharField(max_length=150, null=True, blank=True)
    wild_pitches = models.CharField(max_length=150, null=True, blank=True)
    opp_stolen_bases = models.CharField(max_length=150, null=True, blank=True)
    opp_caught_stealing = models.CharField(max_length=150, null=True, blank=True)
    zone_rating = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.team_code
