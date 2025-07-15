package com.gamingroom;

import java.util.ArrayList;
import java.util.List;

/**
 * A singleton service for the game engine
 * Has unique id for the game, team and player
 * @author justin.guida@snhu.edu
 */

public class GameService {
	private static GameService instance = null;
	//list of games
	private static List<Game> games = new ArrayList<Game>();

	//private constructor to prevent instantiation from outside the class
	private long nextGameId = 1;
	private long nextTeamId = 1;
	private long nextPlayerId = 1;
	//private constructor to prevent instantiation from outside the class
	private GameService() {}

	public long getNextPlayerId() {
		return nextPlayerId++;
	}
	
	public long getNextTeamId() {
		return nextTeamId++;
	}
	
	/**
	 * Singleton Pattern Explanation:
	 * ------------------------------
	 * The Singleton Pattern ensures that only one instance of the GameService class
	 * exists in memory. This is done by:
	 *  - Making the constructor private
	 *  - Creating a private static instance of the class
	 *  - Providing a public static method (getInstance) to return the sole instance
	 * 
	 * In this application, GameService acts as the central controller for game
	 * management. It is shared across all game-related operations, so only one
	 * global instance is needed. This ensures memory efficiency and consistency
	 * across all game actions (adding, retrieving, or checking for duplicates).
	 */
	
	//Public accessor to retrieve the singleton instance.
	//This method ensures the instance is created only when needed, lazy instantiation
	public static GameService getInstance() {
		if (instance == null) {
			instance = new GameService();
			System.out.println(">>> Singleton GameService instance CREATED");
		}
		return instance;
	}

	/**
	 * Iterator Pattern Simple Explanation:
	 * --------------------------------------
	 * We're simply looping through the list of games "one by one" using a for-each loop.
	 * That loop uses Java's built-in iterator in the background.
	 * 
	 * We use the iterator to check for duplicates or find a game by name or ID. 
	 * It's simple and allows for no repeats, so in this case gameID and gameName are unique and there are no duplicates.
	 * This is also used in password validation, where the password is checked against a list of passwords to ensure it is unique.
	 */

	/**
	 * Construct a new game instance
	 * 
	 * @param name the unique name of the game
	 * @return the game instance (new or existing)
	 */
	public Game addGame(String name) {

		// a local game instance
		Game game = null;

		/*
		 * 1. for loop iterates through Game g in games list
		 * 2. if statement checks if g.getName is equal to name passed in
		 * 3. return the game if found on list, null if not found
		 */

		// Checks for duplicates for game name
		for (Game g : games) {
			if (g.getName().equals(name)) {
				return g;
			}
		}

		/* 
		 * if game not found, create a new game instance, nextGameId incremented by 1. 
		 * 1. checking if game is null
		 * 2. if it is null, create a new game instance, nextGameId is incremented by 1. 
		 * 3. add the new game to the games list.
		 * 4. return the new game if added, or existing one if found
		 */

		if (game == null) {
			game = new Game(nextGameId++, name);
			games.add(game);
		}
		return game;
	}

	/** 
	 * Returns the game instance at the specified index.
	 * <p>
	 * Scope is package/local for testing purposes.
	 * </p>
	 * @param index index position in the list to return
	 * @return requested game instance
	 */
	Game getGame(int index) {
		return games.get(index);
	}

	/** FIXES:
	 * Returns the game instance with the specified id.
	 * 
	 * @param id unique identifier of game to search for
	 * @return requested game instance
	 */
	public Game getGame(long id) {
		Game game = null;

		// Iterate through the games list to find a game with the same id
		for (Game g : games) {
			if (g.getId() == id) {
				return g;
			}
		}

		return game;
	}

	/**
	 * Returns the game instance with the specified name.
	 * 
	 * @param name unique name of game to search for
	 * @return requested game instance
	 */
	public Game getGame(String name) {
		Game game = null;

		for (Game g : games) {
			if (g.getName().equals(name)) {
				return g;
			}
		}
		return game;
	}

	/**
	 * Returns the number of games currently active
	 * @return the number of games currently active
	 */
	public int getGameCount() {
		return games.size();
	}
}