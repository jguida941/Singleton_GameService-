package com.gamingroom;

/**
 * Abstract base class for common game entities like Game and Player.
 * 
 * <p>This class provides a shared structure (ID and name) and behavior (toString)
 * for all game-related objects. It also uses getClass().getSimpleName() to ensure
 * the correct subclass name is included in output.</p>
 */

public abstract class Entity {
    
    //This is the unique id for the entity
    private long id;
    //This is the Display name of the entity
    private String name;

    //constructor for Entity based of UML diagram
    public Entity(long id, String name) {
        this.id = id; 
        this.name = name; 
    }

    //getters for id
    public long getId() {
        return id;
    }
    
    //getter for the name 
    public String getName() {
        return name;
    }

    /**
     * Constructor for Entity based on UML design.
     *
     * @param id    The unique ID of the entity
     * @param name  The name of the entity
     */

    //returns a formatted string with the class name, id, and name
    @Override//override the toString method, example for the game could be Game [id=1, name=Game 1]
    public String toString() {
        return getClass().getSimpleName() + " [id=" + id + ", name=" + name + "]";
    }
}
 