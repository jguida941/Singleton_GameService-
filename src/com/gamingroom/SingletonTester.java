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
		GameService service1 = GameService.getInstance();
		GameService service2 = GameService.getInstance();

		//FIXED: Shows that both referancs point to same object in memory
		System.out.println("service1 hashcode: " + service1.hashCode());
		System.out.println("service2 hashcode: " + service2.hashCode());
		System.out.println("service1 and service2 point to the same instance? " + (service1 == service2));
		
		
		//FIXED: THis is a clean print using just one referance 
	
		System.out.println("service (via service1) hashcode: " + service1.hashCode());
	}
}