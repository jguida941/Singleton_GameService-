package com.gamingroom;

/**
 * A class to test a singleton's behavior
 * 
 * @author justin.guida@snhu.edu
 */
public class SingletonTester {

	public void testSingleton() {
		
		System.out.println("\nAbout to test the singleton...");
		
		//FIXME: obtain local reference to the singleton instance
		//FIXED: Referance to the singleton instance 
	

		//FIXED: Local referance to the singleton instance
		GameService service = GameService.getInstance();
		// Display the result this should be the same instance
        System.out.println("Testing singleton instance again: " + service);
		System.out.println("GameService instance hash: " + System.identityHashCode(service));
    }
}
