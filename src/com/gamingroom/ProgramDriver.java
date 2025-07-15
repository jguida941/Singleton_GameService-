package com.gamingroom;

/**
 * Application start-up program
 * 
 * @author justin.guida@snhu.edu
 */
public class ProgramDriver {
	
	/**
	 * The one-and-only main() method
	 * 
	 * @param args command line arguments
	 */
	public static void main(String[] args) {
		
		
		//FIXED: Referance to the singleton instance 
		GameService service = GameService.getInstance(); // replace null with GameService.getInstance();
		
		System.out.println("\nAbout to test initializing game data...");
		
		// initialize with some game data
		Game game1 = service.addGame("Game #1");
		System.out.println(game1);
		Game game2 = service.addGame("Game #2");
		System.out.println(game2);
		
		Team team1 = game1.addTeam("Team Alpha"); // teams to test the singleton
		Player player1 = team1.addPlayer("Justin"); // players to test the singleton
		System.out.println(team1);
		System.out.println(player1);
		
		Team team2 = game1.addTeam("Team Beta"); // team 2 to test the singleton
		Player player2 = team2.addPlayer("John"); // player 2 to test the singleton
		System.out.println(team2);
		System.out.println(player2);
		
		// use another class to prove there is only one instance
		SingletonTester tester = new SingletonTester();
		tester.testSingleton();
	}
}
