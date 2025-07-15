package com.gamingroom;
//need array list to hold the games and utillist to hold the games
import java.util.ArrayList;
import java.util.List;


/**
 * A Game has one playable game session.
 * It Inherits from Entity, so it has an ID and name.
 * Holds a list of Team objects.
 * 
 * <p>
 * No setters are provided. All objects
 * are created with unique IDs.
 * This is done by GameService to avoid duplication.
 * </p>
 * 
 * @author justin.guida@snhu.edu
 */
public class Game extends Entity { //need to extend the Entity class
	
	//need to create a list to hold teams
	private List<Team> teams = new ArrayList<Team>();
	
	//game constructor
	public Game(long id, String name) {
		super(id, name); // call the Entity constructor
	}
	

/**
 * 
 * <p>
 * UMD/Entity requires id and name
 * All entitities game team and player must folllow this format
 * To prevent duplicates we call GameService to allocate the IDs for the game, team and player
 * </p>
 *
 *
 */


	//add team with a unique name, must call GameService.getInstance.getNextTeamId()
	public Team addTeam(String name) {
		for (Team team : teams) { 
			if (team.getName().equalsIgnoreCase(name)) {  //ignore case if the team name is already in the list
				return team; 
			}
		}
		
		
		//create t with a unique id
		Team team = new Team(GameService.getInstance().getNextTeamId(), name); // create a new team
		teams.add(team); 
		return team; 
	}

	//get the teams in the game
	public List<Team> getTeams() {
		return teams;
	}

// I need to override the toString method to return the game name and id
@Override
public String toString() {
	//implentation to add players to print statement
	StringBuilder sb = new StringBuilder();
	sb.append("Game [id=").append(getId()).append(", name=").append(getName()).append("]");
	if (!teams.isEmpty()) {
		sb.append("\n  Teams:");
		for (Team team : teams) {
			sb.append("\n    ").append(team);
		}
	}

	return sb.toString();
}
}