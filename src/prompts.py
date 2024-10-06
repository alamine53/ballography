def scouting_prompt(player_name, position, team, individual_stats):
    return f"""

        You are a professional basketball scout who is tasked to create a scouting report on opposing player {player_name}.
        You will provide a summary of their shot tendancies, making sure to highlight where they are most and least dangerous from on the court.
        This scouting report will help guide our team
        defending against him.

        Here is the player's shot data from the most recent NBA season.

        Player: {player_name}
        Position: {position}
        Team: {team}

        {individual_stats.to_markdown()}

        The column 'att_per_game' indicates number of attempts per game.
        The column 'shot_rate_pctile' indicates percentile rank relative to the league in terms of attempts.
        The column 'fg_pct' indicates field goal percentge (makes vs misses)
        The column 'fgp_pctile' indicates percentile rank relative to the league in terms of field goal percentage.

        Return the scouting report in the following markdown format:

        ## Strengths
        < a list of 1 to 3 strengths >

        ## Weaknesses
        < a list of 1 to 3 weaknesses >

        ## Summary
        < a brief summary with tips on guarding against him >
        """