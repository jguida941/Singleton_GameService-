package com.gamingroom;
import java.util.ArrayList; //imported for  list of players
import java.util.List; //imported for list of players

/**
 * A team class that inherits from Entity
 * </p>
 * @author justin.guida@snhu.edu
 *
 */

public class Team extends Entity {

	//made private for encapsulation best practice 
	private List<Player> players = new ArrayList<>(); // holds the players on the team
	
	public Team(long id, String name) {
		super(id, name); // call the Entity constructor
	}

	/**
	 * Checks if a player with the same name already exist
	 * If found, returns the existing player.
	 * If not, Requests a unique ID from the singleton GameService.
	 * creates a new player, adds it to the players list
	 * returns the new Player
	 */
	public Player addPlayer(String name) {
		for (Player player : players) {
			if (player.getName().equalsIgnoreCase(name)) {
				return player;
			}
		}
		//allows for only one player with the same name
		Player player = new Player(GameService.getInstance().getNextPlayerId(), name);
		players.add(player);
		return player;
	}

	//get the players on the team
	public List<Player> getPlayers() {
		return players;
	}

	@Override//override the toString method to return the team name and id
	public String toString() {
		//implentation to teams, ids, names, and players
		StringBuilder sb = new StringBuilder();
		sb.append("Team [id=").append(getId()).append(", name=").append(getName()).append("]");

		if (!players.isEmpty()) {
			sb.append("\n  Players:");
			for (Player player : players) {
				sb.append("\n    ").append(player); // uses Player.toString()
			}
		}

		return sb.toString();
	}
}
