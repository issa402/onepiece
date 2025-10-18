/*
🏴‍☠️ JAVA ENTERPRISE MASTERY - COMPLETE HANDS-ON TUTORIAL
═══════════════════════════════════════════════════════════════════════════════

🎯 WHAT YOU'LL LEARN (WITH REAL CODE EXAMPLES):
This isn't just a list of topics - it's a complete step-by-step tutorial that teaches
you Java enterprise development from the ground up with working code examples!

📚 HOW THIS TUTORIAL WORKS:
✅ CLEAR EXPLANATIONS - What each concept is and why it exists
✅ WORKING CODE EXAMPLES - Real code you can run and modify
✅ STEP-BY-STEP BREAKDOWNS - Line-by-line explanation of what code does
✅ PRACTICAL USE CASES - When and why to use each concept
✅ COMMON MISTAKES - What beginners do wrong and how to avoid it
✅ PRACTICE EXERCISES - Hands-on tasks to reinforce learning

� WHAT WE'LL BUILD TOGETHER:
A complete One Piece Character Trading System that demonstrates every concept
with real, working code that you can understand, modify, and extend!

� LEARNING APPROACH:
Instead of just listing "Collections Framework - ArrayList, HashMap"
We'll teach: "What are Collections? Why do we need them? Here's how ArrayList works
with code examples. Here's when to use HashMap vs ArrayList. Here are common mistakes."

🚀 BY THE END YOU'LL KNOW:
- How to write professional Java code like Netflix engineers
- When and why to use each Java feature (not just what they are)
- How to build enterprise applications that scale to millions of users
- How to avoid common mistakes that crash production systems
- How to get hired at FAANG companies with Java skills

Let's start learning Java the RIGHT way - with understanding, not memorization!
*/

// ═══════════════════════════════════════════════════════════════════════════════
// LESSON 1: JAVA FUNDAMENTALS - OBJECT-ORIENTED PROGRAMMING (OOP)
// ═══════════════════════════════════════════════════════════════════════════════

/*
🎯 WHAT IS OBJECT-ORIENTED PROGRAMMING?

OOP is a way of organizing code around "objects" instead of functions.
Think of it like this:
- Instead of having separate functions for "createCharacter", "updateCharacter", "deleteCharacter"
- We create a "Character" object that knows how to create, update, and delete itself

WHY DO WE USE OOP?
✅ ORGANIZATION - Code is easier to understand and maintain
✅ REUSABILITY - We can reuse objects in different parts of our application
✅ SCALABILITY - Large applications (like Netflix) are easier to manage
✅ TEAMWORK - Different developers can work on different objects

THE 4 PILLARS OF OOP:
1. ENCAPSULATION - Hide internal details, expose only what's needed
2. INHERITANCE - Create new classes based on existing ones
3. POLYMORPHISM - Same method name, different behavior
4. ABSTRACTION - Focus on what an object does, not how it does it

Let's learn each one with real code examples!
*/

// ENCAPSULATION EXAMPLE - Character Class
/*
🔍 WHAT IS ENCAPSULATION?
Encapsulation means "hiding the internal details and exposing only what's necessary"

REAL-WORLD ANALOGY:
When you drive a car, you use the steering wheel, pedals, and gear shift.
You don't need to know how the engine works internally.
The car "encapsulates" the complex engine details and gives you simple controls.

IN JAVA:
- We make fields private (hidden)
- We provide public methods (getters/setters) to access them
- This protects our data from being corrupted by outside code
*/

public class Character {
    // PRIVATE FIELDS - These are hidden from outside code
    // This is ENCAPSULATION in action!
    private String name;           // Only this class can directly access name
    private long bounty;          // Only this class can directly access bounty
    private String crew;          // Only this class can directly access crew
    private boolean isAlive;      // Only this class can directly access isAlive

    // CONSTRUCTOR - How we create new Character objects
    /*
    🔍 WHAT IS A CONSTRUCTOR?
    A constructor is a special method that runs when we create a new object.
    It's like a "factory" that builds our object with the data we provide.

    WHY DO WE NEED IT?
    - Ensures every Character has required information (name, bounty, crew)
    - Prevents creating invalid characters (like a character with no name)
    - Sets up the object in a valid state from the beginning
    */
    public Character(String name, long bounty, String crew) {
        // INPUT VALIDATION - Prevent bad data from entering our system
        if (name == null || name.trim().isEmpty()) {
            throw new IllegalArgumentException("Character name cannot be empty!");
        }
        if (bounty < 0) {
            throw new IllegalArgumentException("Bounty cannot be negative!");
        }
        if (crew == null || crew.trim().isEmpty()) {
            throw new IllegalArgumentException("Character must belong to a crew!");
        }

        // ASSIGN VALUES - Set up our object's internal state
        this.name = name.trim();      // Remove extra spaces
        this.bounty = bounty;
        this.crew = crew.trim();
        this.isAlive = true;          // New characters start alive

        // LOG CREATION - Good practice for debugging
        System.out.println("✅ Created character: " + name + " with bounty: " + bounty);
    }

    // GETTER METHODS - Safe way to access private fields
    /*
    🔍 WHY DO WE NEED GETTERS?
    Since our fields are private, outside code can't access them directly.
    Getters provide a controlled way to read the data.

    BENEFITS:
    - We can add validation or formatting
    - We can log when data is accessed
    - We can change internal implementation without breaking outside code
    */
    public String getName() {
        return name;
    }

    public long getBounty() {
        return bounty;
    }

    public String getCrew() {
        return crew;
    }

    public boolean isAlive() {
        return isAlive;
    }

    // SETTER METHODS - Safe way to modify private fields
    /*
    🔍 WHY DO WE NEED SETTERS?
    Setters provide a controlled way to change object data.
    We can add validation, logging, and business rules.
    */
    public void setBounty(long newBounty) {
        if (newBounty < 0) {
            throw new IllegalArgumentException("Bounty cannot be negative!");
        }

        long oldBounty = this.bounty;
        this.bounty = newBounty;

        // LOG THE CHANGE - Important for tracking bounty updates
        System.out.println("💰 " + name + "'s bounty updated: " + oldBounty + " → " + newBounty);
    }

    public void setCrew(String newCrew) {
        if (newCrew == null || newCrew.trim().isEmpty()) {
            throw new IllegalArgumentException("Crew cannot be empty!");
        }

        String oldCrew = this.crew;
        this.crew = newCrew.trim();

        System.out.println("🏴‍☠️ " + name + " joined new crew: " + oldCrew + " → " + newCrew);
    }

    // BUSINESS METHODS - What this object can DO
    /*
    🔍 WHAT ARE BUSINESS METHODS?
    These are methods that represent actions the object can perform.
    They contain the "business logic" - the rules of our application.
    */
    public void defeat() {
        if (!isAlive) {
            System.out.println("💀 " + name + " is already defeated!");
            return;
        }

        this.isAlive = false;
        System.out.println("⚔️ " + name + " has been defeated!");
    }

    public void revive() {
        if (isAlive) {
            System.out.println("✨ " + name + " is already alive!");
            return;
        }

        this.isAlive = true;
        System.out.println("🌟 " + name + " has been revived!");
    }

    public boolean canFight(Character opponent) {
        if (!this.isAlive) {
            System.out.println("💀 " + this.name + " cannot fight - they are defeated!");
            return false;
        }
        if (!opponent.isAlive()) {
            System.out.println("💀 " + opponent.getName() + " cannot fight - they are defeated!");
            return false;
        }
        if (this.crew.equals(opponent.getCrew())) {
            System.out.println("🤝 " + this.name + " and " + opponent.getName() + " are crewmates!");
            return false;
        }
        return true;
    }

    // toString METHOD - How to display this object as text
    /*
    🔍 WHAT IS toString()?
    This method defines how our object appears when printed or converted to text.
    It's automatically called when you use System.out.println(character).
    */
    @Override
    public String toString() {
        String status = isAlive ? "Alive" : "Defeated";
        return String.format("Character{name='%s', bounty=%d, crew='%s', status='%s'}",
                           name, bounty, crew, status);
    }
}

// ═══════════════════════════════════════════════════════════════════════════════
// LESSON 2: INHERITANCE - CREATING SPECIALIZED CLASSES
// ═══════════════════════════════════════════════════════════════════════════════

/*
🎯 WHAT IS INHERITANCE?

Inheritance lets us create new classes based on existing ones.
The new class gets all the features of the original class, plus new ones.

REAL-WORLD ANALOGY:
Think of a "Vehicle" class with wheels, engine, and ability to move.
Then we create "Car" and "Motorcycle" classes that inherit from Vehicle.
- Car gets wheels, engine, move() PLUS 4 doors, trunk
- Motorcycle gets wheels, engine, move() PLUS 2 wheels, no doors

WHY USE INHERITANCE?
✅ CODE REUSE - Don't repeat common code
✅ ORGANIZATION - Group related classes together
✅ POLYMORPHISM - Treat different objects the same way
✅ MAINTENANCE - Change common behavior in one place

JAVA INHERITANCE KEYWORDS:
- extends = "this class inherits from that class"
- super = "call the parent class method/constructor"
- @Override = "this method replaces the parent's version"
*/

// PARENT CLASS - DevilFruitUser (inherits from Character)
/*
🔍 WHY CREATE DevilFruitUser CLASS?
Some characters have Devil Fruit powers, others don't.
Instead of adding Devil Fruit fields to ALL characters,
we create a specialized class for Devil Fruit users.

INHERITANCE HIERARCHY:
Character (basic character features)
    ↓
DevilFruitUser (character + devil fruit powers)
    ↓
LogiaUser, ParameciaUser, ZoanUser (specific devil fruit types)
*/



public class DevilFruitUser extends Character {
    // NEW FIELDS - Only Devil Fruit users have these
    private String devilFruitName;
    private String devilFruitType;  // Logia, Paramecia, Zoan
    private boolean canSwim;        // Devil Fruit users can't swim!

    // CONSTRUCTOR - Must call parent constructor first
    /*
    🔍 WHY USE super()?
    The parent class (Character) has required fields (name, bounty, crew).
    We must initialize the parent first, then add our new features.

    super() calls the parent class constructor.
    It MUST be the first line in our constructor.
    */
    public DevilFruitUser(String name, long bounty, String crew,
                         String devilFruitName, String devilFruitType) {
        // CALL PARENT CONSTRUCTOR FIRST - This is REQUIRED!
        super(name, bounty, crew);

        // VALIDATE DEVIL FRUIT DATA
        if (devilFruitName == null || devilFruitName.trim().isEmpty()) {
            throw new IllegalArgumentException("Devil Fruit name cannot be empty!");
        }
        if (devilFruitType == null || devilFruitType.trim().isEmpty()) {
            throw new IllegalArgumentException("Devil Fruit type cannot be empty!");
        }

        // INITIALIZE NEW FIELDS
        this.devilFruitName = devilFruitName.trim();
        this.devilFruitType = devilFruitType.trim();
        this.canSwim = false;  // Devil Fruit users lose ability to swim

        System.out.println("🍎 " + name + " ate the " + devilFruitName + " (" + devilFruitType + ")");
    }

    // NEW GETTER METHODS - For Devil Fruit specific data
    public String getDevilFruitName() {
        return devilFruitName;
    }

    public String getDevilFruitType() {
        return devilFruitType;
    }

    public boolean canSwim() {
        return canSwim;
    }

    // NEW BUSINESS METHODS - Devil Fruit specific abilities
    public void useDevilFruitPower() {
        if (!isAlive()) {
            System.out.println("💀 " + getName() + " cannot use powers - they are defeated!");
            return;
        }

        System.out.println("✨ " + getName() + " uses " + devilFruitName + " power!");
        // Subclasses will override this with specific power effects
    }

    public void touchSeawater() {
        if (!isAlive()) {
            System.out.println("💀 " + getName() + " is already defeated!");
            return;
        }

        System.out.println("🌊 " + getName() + " touched seawater and became weak!");
        System.out.println("😵 Devil Fruit users are weakened by seawater!");
        // In a real game, this might reduce their power temporarily
    }

    // OVERRIDE PARENT METHOD - Customize behavior for Devil Fruit users
    /*
    🔍 WHAT IS @Override?
    This annotation tells Java we're replacing a method from the parent class.
    It helps catch errors - if the parent doesn't have this method, Java will complain.

    WHY OVERRIDE toString()?
    We want to show Devil Fruit information when printing DevilFruitUser objects.
    */
    @Override
    public String toString() {
        // CALL PARENT VERSION FIRST - Get basic character info
        String parentInfo = super.toString();

        // ADD DEVIL FRUIT INFO
        return parentInfo.replace("}",
            String.format(", devilFruit='%s (%s)', canSwim=%b}",
                         devilFruitName, devilFruitType, canSwim));
    }
}

// SPECIALIZED DEVIL FRUIT CLASS - Logia Type
/*
🔍 WHY CREATE LogiaUser CLASS?
Logia Devil Fruits have unique abilities (turn into elements, intangible).
Instead of putting Logia-specific code in DevilFruitUser,
we create a specialized class just for Logia users.

This demonstrates INHERITANCE CHAIN:
Character → DevilFruitUser → LogiaUser
*/
public class LogiaUser extends DevilFruitUser {
    private String element;  // Fire, Ice, Light, etc.
    private boolean isIntangible;

    public LogiaUser(String name, long bounty, String crew,
                    String devilFruitName, String element) {
        // CALL PARENT CONSTRUCTOR - DevilFruitUser constructor
        super(name, bounty, crew, devilFruitName, "Logia");

        this.element = element;
        this.isIntangible = false;  // Start in normal form

        System.out.println("🔥 " + name + " can transform into " + element + "!");
    }

    // LOGIA-SPECIFIC METHODS
    public void transformIntoElement() {
        if (!isAlive()) {
            System.out.println("💀 " + getName() + " cannot transform - they are defeated!");
            return;
        }

        isIntangible = true;
        System.out.println("✨ " + getName() + " transformed into " + element + "!");
        System.out.println("👻 " + getName() + " is now intangible!");
    }

    public void returnToNormalForm() {
        isIntangible = false;
        System.out.println("🧍 " + getName() + " returned to normal form.");
    }

    // OVERRIDE DEVIL FRUIT POWER - Logia-specific implementation
    @Override
    public void useDevilFruitPower() {
        if (!isAlive()) {
            System.out.println("💀 " + getName() + " cannot use powers - they are defeated!");
            return;
        }

        System.out.println("🔥 " + getName() + " unleashes " + element + " power!");

        // Different effects based on element
        switch (element.toLowerCase()) {
            case "fire":
                System.out.println("🔥 Burning flames engulf the battlefield!");
                break;
            case "ice":
                System.out.println("❄️ Everything freezes solid!");
                break;
            case "light":
                System.out.println("✨ Blinding light fills the area!");
                break;
            default:
                System.out.println("💥 " + element + " energy explodes everywhere!");
        }
    }

    public String getElement() {
        return element;
    }

    public boolean isIntangible() {
        return isIntangible;
    }
}

// ═══════════════════════════════════════════════════════════════════════════════
// LESSON 3: COLLECTIONS FRAMEWORK - STORING AND MANAGING DATA
// ═══════════════════════════════════════════════════════════════════════════════

/*
🎯 WHAT ARE COLLECTIONS?

Collections are containers that hold multiple objects.
Think of them like different types of storage boxes:
- ArrayList = Expandable array (like a list that can grow)
- HashMap = Key-value pairs (like a dictionary)
- HashSet = Unique items only (no duplicates)

WHY DO WE NEED COLLECTIONS?
✅ DYNAMIC SIZE - Can grow and shrink as needed
✅ BUILT-IN METHODS - Add, remove, search, sort automatically
✅ TYPE SAFETY - Can specify what type of objects to store
✅ PERFORMANCE - Optimized for different use cases

REAL-WORLD ANALOGY:
- ArrayList = Shopping list (ordered, can have duplicates)
- HashMap = Phone book (name → phone number)
- HashSet = Guest list (each person appears only once)

Let's learn each collection with practical examples!
*/

import java.util.*;

// COLLECTIONS DEMONSTRATION CLASS
public class OnePieceCrewManager {

    // ARRAYLIST EXAMPLE - Ordered list of crew members
    /*
    🔍 WHAT IS ARRAYLIST?
    ArrayList is like a resizable array. It maintains insertion order
    and allows duplicate elements.

    WHEN TO USE ARRAYLIST:
    ✅ When you need ordered data
    ✅ When you access elements by index (position)
    ✅ When duplicates are allowed
    ✅ When you frequently add/remove from the end

    COMMON MISTAKES:
    ❌ Using ArrayList when you need fast lookups (use HashMap instead)
    ❌ Not specifying the type: ArrayList list = new ArrayList(); (use generics!)
    ❌ Using ArrayList for fixed-size data (use arrays instead)
    */
    private ArrayList<Character> crewMembers;

    // HASHMAP EXAMPLE - Character name to bounty mapping
    /*
    🔍 WHAT IS HASHMAP?
    HashMap stores key-value pairs. It's like a dictionary where you
    look up values using keys.

    WHEN TO USE HASHMAP:
    ✅ When you need fast lookups by key
    ✅ When you have key-value relationships
    ✅ When order doesn't matter
    ✅ When you need O(1) average lookup time

    COMMON MISTAKES:
    ❌ Using HashMap when order matters (use LinkedHashMap)
    ❌ Using mutable objects as keys
    ❌ Not handling null keys/values properly
    */
    private HashMap<String, Long> bountyMap;

    // HASHSET EXAMPLE - Unique crew names
    /*
    🔍 WHAT IS HASHSET?
    HashSet stores unique elements only. No duplicates allowed.

    WHEN TO USE HASHSET:
    ✅ When you need to ensure uniqueness
    ✅ When you need fast contains() checks
    ✅ When order doesn't matter
    ✅ When you want to remove duplicates from data

    COMMON MISTAKES:
    ❌ Expecting elements to be in insertion order
    ❌ Using HashSet when you need indexed access
    ❌ Not implementing equals() and hashCode() for custom objects
    */
    private HashSet<String> uniqueCrews;

    // CONSTRUCTOR - Initialize all collections
    public OnePieceCrewManager() {
        // INITIALIZE COLLECTIONS - Always do this!
        crewMembers = new ArrayList<>();     // Empty list, will grow as needed
        bountyMap = new HashMap<>();         // Empty map, will grow as needed
        uniqueCrews = new HashSet<>();       // Empty set, will grow as needed

        System.out.println("🏴‍☠️ Crew Manager initialized!");
        System.out.println("📋 Ready to manage crew members, bounties, and crews!");
    }

    // ARRAYLIST METHODS - How to work with lists
    /*
    🔍 ARRAYLIST COMMON OPERATIONS:
    - add() = Add element to end
    - add(index, element) = Insert at specific position
    - get(index) = Get element at position
    - set(index, element) = Replace element at position
    - remove(index) = Remove element at position
    - size() = Get number of elements
    - contains() = Check if element exists
    - indexOf() = Find position of element
    */

    public void addCrewMember(Character character) {
        // INPUT VALIDATION - Always check for null!
        if (character == null) {
            System.out.println("❌ Cannot add null character!");
            return;
        }

        // CHECK FOR DUPLICATES - Prevent adding same character twice
        if (crewMembers.contains(character)) {
            System.out.println("⚠️ " + character.getName() + " is already in the crew!");
            return;
        }

        // ADD TO ARRAYLIST - This automatically grows the list
        crewMembers.add(character);

        // ADD TO HASHMAP - Store name → bounty mapping
        bountyMap.put(character.getName(), character.getBounty());

        // ADD TO HASHSET - Track unique crew names
        uniqueCrews.add(character.getCrew());

        System.out.println("✅ Added " + character.getName() + " to crew!");
        System.out.println("📊 Total crew members: " + crewMembers.size());
    }

    public Character getCrewMember(int index) {
        // BOUNDS CHECKING - Prevent IndexOutOfBoundsException
        if (index < 0 || index >= crewMembers.size()) {
            System.out.println("❌ Invalid index: " + index +
                             " (valid range: 0-" + (crewMembers.size() - 1) + ")");
            return null;
        }

        // GET ELEMENT BY INDEX - O(1) operation for ArrayList
        Character character = crewMembers.get(index);
        System.out.println("👤 Retrieved: " + character.getName() + " at position " + index);
        return character;
    }

    public void removeCrewMember(String name) {
        // FIND CHARACTER BY NAME - Linear search through list
        Character toRemove = null;
        int indexToRemove = -1;

        for (int i = 0; i < crewMembers.size(); i++) {
            Character character = crewMembers.get(i);
            if (character.getName().equals(name)) {
                toRemove = character;
                indexToRemove = i;
                break;  // Found it, stop searching
            }
        }

        // CHECK IF FOUND
        if (toRemove == null) {
            System.out.println("❌ Character not found: " + name);
            return;
        }

        // REMOVE FROM ALL COLLECTIONS
        crewMembers.remove(indexToRemove);  // Remove from ArrayList
        bountyMap.remove(name);             // Remove from HashMap
        // Note: We don't remove from uniqueCrews because other characters might be from same crew

        System.out.println("🗑️ Removed " + name + " from crew!");
        System.out.println("📊 Remaining crew members: " + crewMembers.size());
    }

    // HASHMAP METHODS - How to work with key-value pairs
    /*
    🔍 HASHMAP COMMON OPERATIONS:
    - put(key, value) = Add or update key-value pair
    - get(key) = Get value for key
    - containsKey(key) = Check if key exists
    - containsValue(value) = Check if value exists
    - remove(key) = Remove key-value pair
    - keySet() = Get all keys
    - values() = Get all values
    - entrySet() = Get all key-value pairs
    */

    public Long getBounty(String characterName) {
        // GET VALUE BY KEY - O(1) average time complexity
        Long bounty = bountyMap.get(characterName);

        if (bounty == null) {
            System.out.println("❌ No bounty found for: " + characterName);
            return null;
        }

        System.out.println("💰 " + characterName + "'s bounty: " + bounty);
        return bounty;
    }

    public void updateBounty(String characterName, long newBounty) {
        // CHECK IF CHARACTER EXISTS
        if (!bountyMap.containsKey(characterName)) {
            System.out.println("❌ Character not found: " + characterName);
            return;
        }

        // GET OLD BOUNTY
        Long oldBounty = bountyMap.get(characterName);

        // UPDATE BOUNTY IN HASHMAP
        bountyMap.put(characterName, newBounty);

        // ALSO UPDATE IN ARRAYLIST - Find and update the Character object
        for (Character character : crewMembers) {
            if (character.getName().equals(characterName)) {
                character.setBounty(newBounty);
                break;
            }
        }

        System.out.println("💰 Updated " + characterName + "'s bounty: " +
                          oldBounty + " → " + newBounty);
    }

    public void showAllBounties() {
        System.out.println("\n💰 ALL BOUNTIES:");
        System.out.println("================");

        // ITERATE THROUGH HASHMAP - Using entrySet()
        for (Map.Entry<String, Long> entry : bountyMap.entrySet()) {
            String name = entry.getKey();
            Long bounty = entry.getValue();
            System.out.println(name + ": " + bounty + " berries");
        }

        System.out.println("Total characters: " + bountyMap.size());
    }

    // HASHSET METHODS - Working with unique collections
    public void showUniqueCrews() {
        System.out.println("\n🏴‍☠️ UNIQUE CREWS:");
        System.out.println("==================");

        // ITERATE THROUGH HASHSET - No guaranteed order
        for (String crew : uniqueCrews) {
            System.out.println("- " + crew);
        }

        System.out.println("Total unique crews: " + uniqueCrews.size());
    }

    // ADVANCED COLLECTION OPERATIONS
    public void findHighestBounty() {
        if (bountyMap.isEmpty()) {
            System.out.println("❌ No bounties to compare!");
            return;
        }

        String highestBountyCharacter = null;
        long highestBounty = 0;

        // FIND MAXIMUM VALUE - Iterate through all entries
        for (Map.Entry<String, Long> entry : bountyMap.entrySet()) {
            if (entry.getValue() > highestBounty) {
                highestBounty = entry.getValue();
                highestBountyCharacter = entry.getKey();
            }
        }

        System.out.println("👑 Highest bounty: " + highestBountyCharacter +
                          " with " + highestBounty + " berries!");
    }

    public void sortCrewMembersByBounty() {
        if (crewMembers.isEmpty()) {
            System.out.println("❌ No crew members to sort!");
            return;
        }

        System.out.println("\n📊 CREW MEMBERS SORTED BY BOUNTY:");
        System.out.println("==================================");

        // CREATE A COPY TO SORT - Don't modify original list
        ArrayList<Character> sortedMembers = new ArrayList<>(crewMembers);

        // SORT USING COMPARATOR - Custom sorting logic
        sortedMembers.sort((character1, character2) -> {
            // Compare bounties in descending order (highest first)
            return Long.compare(character2.getBounty(), character1.getBounty());
        });

        // DISPLAY SORTED RESULTS
        for (int i = 0; i < sortedMembers.size(); i++) {
            Character character = sortedMembers.get(i);
            System.out.println((i + 1) + ". " + character.getName() +
                             " - " + character.getBounty() + " berries");
        }
    }
}

// ═══════════════════════════════════════════════════════════════════════════════
// LESSON 4: PUTTING IT ALL TOGETHER - PRACTICAL DEMONSTRATION
// ═══════════════════════════════════════════════════════════════════════════════

/*
🎯 PRACTICAL EXAMPLE - HOW TO USE EVERYTHING WE'VE LEARNED

Now let's see how all these concepts work together in a real program.
This demonstrates:
✅ Object creation and encapsulation
✅ Inheritance and polymorphism
✅ Collections for data management
✅ Error handling and validation
✅ Real-world programming patterns

This is the kind of code you'd write in a professional Java application!
*/

public class OnePieceTradingSystemDemo {

    public static void main(String[] args) {
        System.out.println("🏴‍☠️ ONE PIECE TRADING SYSTEM DEMO");
        System.out.println("===================================\n");

        // STEP 1: CREATE CREW MANAGER
        OnePieceCrewManager crewManager = new OnePieceCrewManager();

        // STEP 2: CREATE DIFFERENT TYPES OF CHARACTERS
        System.out.println("\n🎭 CREATING CHARACTERS:");
        System.out.println("=======================");

        // Regular character
        Character zoro = new Character("Roronoa Zoro", 320000000L, "Straw Hat Pirates");

        // Devil Fruit user
        DevilFruitUser robin = new DevilFruitUser("Nico Robin", 130000000L,
                                                 "Straw Hat Pirates",
                                                 "Hana Hana no Mi", "Paramecia");

        // Logia user
        LogiaUser ace = new LogiaUser("Portgas D. Ace", 550000000L,
                                     "Whitebeard Pirates",
                                     "Mera Mera no Mi", "Fire");

        // STEP 3: ADD CHARACTERS TO CREW MANAGER
        System.out.println("\n👥 ADDING TO CREW:");
        System.out.println("==================");

        crewManager.addCrewMember(zoro);
        crewManager.addCrewMember(robin);
        crewManager.addCrewMember(ace);

        // STEP 4: DEMONSTRATE POLYMORPHISM
        System.out.println("\n✨ DEMONSTRATING POLYMORPHISM:");
        System.out.println("==============================");

        // Same method call, different behavior based on object type
        robin.useDevilFruitPower();  // Paramecia power
        ace.useDevilFruitPower();    // Logia power (overridden method)

        // STEP 5: DEMONSTRATE COLLECTIONS
        System.out.println("\n📊 COLLECTION OPERATIONS:");
        System.out.println("=========================");

        crewManager.showAllBounties();
        crewManager.showUniqueCrews();
        crewManager.findHighestBounty();
        crewManager.sortCrewMembersByBounty();

        // STEP 6: DEMONSTRATE ERROR HANDLING
        System.out.println("\n🛡️ ERROR HANDLING EXAMPLES:");
        System.out.println("============================");

        // Try to add null character
        crewManager.addCrewMember(null);

        // Try to get invalid index
        crewManager.getCrewMember(999);

        // Try to get bounty for non-existent character
        crewManager.getBounty("Fake Character");

        // STEP 7: DEMONSTRATE INHERITANCE CHAIN
        System.out.println("\n🔗 INHERITANCE DEMONSTRATION:");
        System.out.println("==============================");

        // Show how LogiaUser inherits from DevilFruitUser inherits from Character
        System.out.println("Ace's information:");
        System.out.println("- Name (from Character): " + ace.getName());
        System.out.println("- Devil Fruit (from DevilFruitUser): " + ace.getDevilFruitName());
        System.out.println("- Element (from LogiaUser): " + ace.getElement());

        // STEP 8: DEMONSTRATE LOGIA SPECIAL ABILITIES
        System.out.println("\n🔥 LOGIA SPECIAL ABILITIES:");
        System.out.println("===========================");

        ace.transformIntoElement();
        System.out.println("Is Ace intangible? " + ace.isIntangible());
        ace.returnToNormalForm();
        System.out.println("Is Ace intangible? " + ace.isIntangible());

        System.out.println("\n🎉 DEMO COMPLETE!");
        System.out.println("You've seen OOP, Inheritance, Collections, and Error Handling in action!");
    }
}

// ═══════════════════════════════════════════════════════════════════════════════
// COMMON MISTAKES AND HOW TO AVOID THEM
// ═══════════════════════════════════════════════════════════════════════════════

/*
🚨 COMMON JAVA MISTAKES BEGINNERS MAKE:

1. NULL POINTER EXCEPTIONS
❌ WRONG: character.getName() without checking if character is null
✅ RIGHT: if (character != null) { character.getName(); }

2. NOT INITIALIZING COLLECTIONS
❌ WRONG: ArrayList<String> list; list.add("item"); // NullPointerException!
✅ RIGHT: ArrayList<String> list = new ArrayList<>(); list.add("item");

3. USING == INSTEAD OF .equals() FOR STRINGS
❌ WRONG: if (name == "Luffy") // This compares memory addresses!
✅ RIGHT: if (name.equals("Luffy")) // This compares actual content

4. NOT OVERRIDING equals() AND hashCode()
❌ WRONG: Using custom objects in HashMap without proper equals/hashCode
✅ RIGHT: Always override both methods together

5. MODIFYING COLLECTIONS WHILE ITERATING
❌ WRONG: for (Character c : list) { if (condition) list.remove(c); }
✅ RIGHT: Use Iterator.remove() or collect items to remove separately

6. NOT HANDLING EXCEPTIONS
❌ WRONG: Ignoring potential exceptions
✅ RIGHT: Use try-catch blocks or declare throws

7. MEMORY LEAKS WITH COLLECTIONS
❌ WRONG: Adding objects to static collections and never removing them
✅ RIGHT: Clean up collections when objects are no longer needed

8. USING WRONG COLLECTION TYPE
❌ WRONG: Using ArrayList when you need fast lookups
✅ RIGHT: Use HashMap for key-value lookups, HashSet for uniqueness

9. NOT VALIDATING INPUT
❌ WRONG: Assuming input is always valid
✅ RIGHT: Always validate parameters and handle edge cases

10. POOR ENCAPSULATION
❌ WRONG: Making all fields public
✅ RIGHT: Use private fields with public getters/setters
*/

// ═══════════════════════════════════════════════════════════════════════════════
// PRACTICE EXERCISES - TRY THESE YOURSELF!
// ═══════════════════════════════════════════════════════════════════════════════

/*
🎯 PRACTICE EXERCISES:

EXERCISE 1: CREATE A CREW CLASS
- Create a Crew class with name, captain, and list of members
- Add methods to add/remove members, change captain
- Override toString() to display crew information

EXERCISE 2: IMPLEMENT PARAMECIA DEVIL FRUIT USER
- Create ParameciaUser class that extends DevilFruitUser
- Add unique abilities like body modification or object manipulation
- Override useDevilFruitPower() with Paramecia-specific effects

EXERCISE 3: CREATE A BATTLE SYSTEM
- Create a Battle class that manages fights between characters
- Implement turn-based combat with different attack types
- Use polymorphism to handle different character types

EXERCISE 4: IMPLEMENT CREW STATISTICS
- Add methods to calculate average bounty, total bounty
- Find crew members by bounty range
- Group characters by devil fruit type

EXERCISE 5: CREATE A TRADING SYSTEM
- Implement character trading between crews
- Add validation for trade rules (can't trade defeated characters)
- Track trade history using collections

EXERCISE 6: ADD PERSISTENCE
- Save crew data to a file
- Load crew data from a file
- Handle file I/O exceptions properly

EXERCISE 7: IMPLEMENT SEARCH FUNCTIONALITY
- Search characters by name (partial matches)
- Filter characters by crew, bounty range, devil fruit type
- Sort results by different criteria

EXERCISE 8: CREATE A TOURNAMENT SYSTEM
- Organize characters into tournament brackets
- Simulate battles and track winners
- Display tournament results

SOLUTIONS HINTS:
- Use appropriate collections for each data structure
- Apply inheritance where it makes sense
- Always validate input and handle errors
- Use polymorphism to avoid type checking
- Follow encapsulation principles
- Write clear, readable code with good naming

TRY IMPLEMENTING THESE EXERCISES TO REINFORCE YOUR LEARNING!
*/

// ═══════════════════════════════════════════════════════════════════════════════
// WHAT'S NEXT? ADVANCED JAVA TOPICS
// ═══════════════════════════════════════════════════════════════════════════════

/*
🚀 CONGRATULATIONS! YOU'VE LEARNED JAVA FUNDAMENTALS!

You now understand:
✅ Object-Oriented Programming (Encapsulation, Inheritance, Polymorphism)
✅ Collections Framework (ArrayList, HashMap, HashSet)
✅ Error handling and input validation
✅ Professional coding practices

NEXT TOPICS TO LEARN:
1. Exception Handling (try-catch, custom exceptions)
2. Generics (type safety, wildcards)
3. Lambda Expressions and Stream API
4. Multithreading and Concurrency
5. File I/O and Serialization
6. Design Patterns
7. Spring Framework
8. Database Integration (JPA/Hibernate)

KEEP PRACTICING:
- Build more complex projects
- Read other people's code
- Contribute to open source projects
- Practice coding interview questions
- Learn enterprise frameworks like Spring Boot

YOU'RE ON YOUR WAY TO BECOMING A PROFESSIONAL JAVA DEVELOPER! 🎉
*/

// TODO 2: SPRING CORE CONFIGURATION (FAANG PATTERN)
// ═══════════════════════════════════════════════════════════
/*
🎯 YOUR TASK: Create enterprise Spring Core configuration

SPRING CORE FUNDAMENTALS:
- IoC Container and Dependency Injection
- Bean lifecycle and scopes
- AOP for cross-cutting concerns
- Configuration approaches (Java config preferred)
*/

package com.onepiece.trading;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.netflix.eureka.EnableEurekaClient;
import org.springframework.data.jpa.repository.config.EnableJpaRepositories;
import org.springframework.transaction.annotation.EnableTransactionManagement;

/**
 * 🏴‍☠️ One Piece Trading Platform - Java Spring Boot Version
 * 
 * This is how Netflix, Amazon, and Google structure their Java applications:
 * - @SpringBootApplication: Auto-configuration and component scanning
 * - @EnableEurekaClient: Service discovery (Netflix pattern)
 * - @EnableJpaRepositories: Database access layer
 * - @EnableTransactionManagement: ACID transactions for trading
 */
@SpringBootApplication
@EnableEurekaClient  // Netflix service discovery
@EnableJpaRepositories
@EnableTransactionManagement
public class OnePieceTradingApplication {
    
    public static void main(String[] args) {
        SpringApplication.run(OnePieceTradingApplication.class, args);
        System.out.println("🏴‍☠️ One Piece Trading Platform Started!");
        System.out.println("🚀 Enterprise Java Backend Running on Spring Boot");
        System.out.println("📚 Comprehensive Java + Maven + Spring Core Implementation");
    }
}

// TODO 1.5: SPRING CORE CONFIGURATION (ENTERPRISE PATTERN)
// ═══════════════════════════════════════════════════════════
/*
🎯 YOUR TASK: Create enterprise Spring Core configuration

SPRING CORE FUNDAMENTALS IMPLEMENTATION:
- IoC Container and Dependency Injection
- Bean lifecycle and scopes
- AOP for cross-cutting concerns
- Configuration approaches (Java config preferred)
*/

package com.onepiece.trading.config;

import org.springframework.context.annotation.*;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.boot.autoconfigure.condition.ConditionalOnProperty;
import org.springframework.cache.CacheManager;
import org.springframework.cache.annotation.EnableCaching;
import org.springframework.scheduling.annotation.EnableAsync;
import org.springframework.scheduling.concurrent.ThreadPoolTaskExecutor;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.aop.framework.ProxyFactoryBean;
import org.springframework.aop.support.NameMatchMethodPointcut;

import java.util.concurrent.Executor;

/**
 * 🏴‍☠️ Enterprise Spring Core Configuration
 *
 * This demonstrates FAANG-level Spring Core patterns:
 * - Advanced bean configuration and lifecycle management
 * - Conditional bean creation based on properties/profiles
 * - Multiple bean instances with qualifiers
 * - Custom scopes and proxy configurations
 */
@Configuration
@EnableCaching
@EnableAsync
@EnableTransactionManagement
@Profile("!test")
public class CoreConfiguration {

    // Bean with custom lifecycle callbacks
    @Bean(initMethod = "initialize", destroyMethod = "cleanup")
    @Scope("singleton")
    public PriceCalculationEngine priceCalculationEngine() {
        PriceCalculationEngine engine = new PriceCalculationEngine();
        engine.setAlgorithm("ADVANCED_VOLATILITY");
        return engine;
    }

    // Conditional bean creation (Netflix pattern)
    @Bean
    @ConditionalOnProperty(name = "onepiece.caching.enabled", havingValue = "true", matchIfMissing = true)
    public CacheManager redisCacheManager() {
        return new RedisCacheManager();
    }

    // Primary bean when multiple candidates exist
    @Bean
    @Primary
    public NotificationService primaryNotificationService() {
        return new EmailNotificationService();
    }

    // Qualified bean for specific use cases
    @Bean
    @Qualifier("sms")
    public NotificationService smsNotificationService() {
        return new SmsNotificationService();
    }

    // Qualified bean for push notifications
    @Bean
    @Qualifier("push")
    public NotificationService pushNotificationService() {
        return new PushNotificationService();
    }

    // Custom thread pool for async operations (Uber pattern)
    @Bean("tradingExecutor")
    public Executor tradingTaskExecutor() {
        ThreadPoolTaskExecutor executor = new ThreadPoolTaskExecutor();
        executor.setCorePoolSize(5);
        executor.setMaxPoolSize(20);
        executor.setQueueCapacity(100);
        executor.setThreadNamePrefix("Trading-");
        executor.setWaitForTasksToCompleteOnShutdown(true);
        executor.setAwaitTerminationSeconds(30);
        return executor;
    }

    // Profile-specific configuration
    @Bean
    @Profile("development")
    public DatabaseInitializer devDatabaseInitializer() {
        return new DevDatabaseInitializer();
    }

    @Bean
    @Profile("production")
    public DatabaseInitializer prodDatabaseInitializer() {
        return new ProdDatabaseInitializer();
    }
}

// ASPECT-ORIENTED PROGRAMMING (AOP) IMPLEMENTATION
@Aspect
@Component
public class TradingAspect {

    private static final Logger logger = LoggerFactory.getLogger(TradingAspect.class);

    // Before advice - executed before method (LinkedIn pattern)
    @Before("execution(* com.onepiece.trading.service.TradingService.executeTrade(..))")
    public void beforeTrade(JoinPoint joinPoint) {
        Object[] args = joinPoint.getArgs();
        logger.info("🏴‍☠️ Starting trade execution: {} with args: {}",
                   joinPoint.getSignature().getName(), args);
    }

    // Around advice - complete method interception (Netflix monitoring pattern)
    @Around("@annotation(com.onepiece.trading.annotation.Monitored)")
    public Object monitorPerformance(ProceedingJoinPoint joinPoint) throws Throwable {
        long startTime = System.currentTimeMillis();
        String methodName = joinPoint.getSignature().getName();

        try {
            logger.debug("⚡ Starting method: {}", methodName);
            Object result = joinPoint.proceed();
            long endTime = System.currentTimeMillis();
            long executionTime = endTime - startTime;

            logger.info("✅ Method {} executed successfully in {}ms", methodName, executionTime);

            // Record metrics (Prometheus/Micrometer integration)
            recordMethodMetrics(methodName, executionTime, "SUCCESS");

            return result;
        } catch (Exception e) {
            long endTime = System.currentTimeMillis();
            long executionTime = endTime - startTime;

            logger.error("❌ Method {} failed after {}ms: {}", methodName, executionTime, e.getMessage());
            recordMethodMetrics(methodName, executionTime, "ERROR");
            throw e;
        }
    }

    // After returning advice - executed after successful method completion
    @AfterReturning(pointcut = "execution(* com.onepiece.trading.service.*.*(..))", returning = "result")
    public void afterSuccessfulExecution(JoinPoint joinPoint, Object result) {
        logger.debug("🎉 Method {} completed with result: {}",
                    joinPoint.getSignature().getName(), result);
    }

    // After throwing advice - exception handling (Google error tracking pattern)
    @AfterThrowing(pointcut = "execution(* com.onepiece.trading.service.*.*(..))", throwing = "exception")
    public void afterThrowingException(JoinPoint joinPoint, Exception exception) {
        logger.error("💥 Method {} threw exception: {}",
                    joinPoint.getSignature().getName(), exception.getMessage(), exception);

        // Send to error tracking service (Sentry, Rollbar, etc.)
        sendToErrorTracking(joinPoint, exception);
    }

    private void recordMethodMetrics(String methodName, long executionTime, String status) {
        // Implementation for metrics recording
        // This would integrate with Micrometer/Prometheus
    }

    private void sendToErrorTracking(JoinPoint joinPoint, Exception exception) {
        // Implementation for error tracking
        // This would integrate with Sentry, Rollbar, or similar
    }
}

// TODO 3: SPRING BOOT ENTERPRISE FEATURES (COMPLETE IMPLEMENTATION)
// ═══════════════════════════════════════════════════════════
/*
🎯 YOUR TASK: Implement complete Spring Boot enterprise features

SPRING BOOT ENTERPRISE STACK:
- Auto-configuration and starters
- Actuator for monitoring and management
- Security with JWT authentication
- JPA/Hibernate with advanced features
- Kafka for event-driven architecture
- Microservices with service discovery
- Performance optimization and caching
- Reactive programming with WebFlux
*/

package com.onepiece.trading.controller;

import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;
import org.springframework.http.HttpStatus;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.validation.annotation.Validated;
import org.springframework.cache.annotation.Cacheable;
import org.springframework.cache.annotation.CacheEvict;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Sort;

import javax.validation.Valid;
import javax.validation.constraints.Min;
import javax.validation.constraints.Max;
import java.util.List;
import java.util.stream.Collectors;

/**
 * 🏴‍☠️ Enterprise Character Trading Controller
 *
 * This demonstrates complete Spring Boot enterprise patterns:
 * - RESTful API design with proper HTTP methods
 * - Validation and error handling
 * - Security with role-based access control
 * - Caching for performance optimization
 * - Pagination and sorting for large datasets
 * - Comprehensive logging and monitoring
 */
@RestController
@RequestMapping("/api/v1/characters")
@Validated
@Slf4j
@CrossOrigin(origins = "http://localhost:3000") // React frontend
public class CharacterController {

    private final CharacterService characterService;
    private final TradingService tradingService;
    private final NotificationService notificationService;

    // Constructor injection (Spring Boot best practice)
    public CharacterController(CharacterService characterService,
                             TradingService tradingService,
                             NotificationService notificationService) {
        this.characterService = characterService;
        this.tradingService = tradingService;
        this.notificationService = notificationService;
    }

    /**
     * Get all characters with pagination, sorting, and filtering
     * Demonstrates: Pagination, caching, validation, query parameters
     */
    @GetMapping
    @Cacheable(value = "characters", key = "'page:' + #page + ':size:' + #size + ':crew:' + #crew",
               unless = "#result.isEmpty()")
    public ResponseEntity<PagedResponse<CharacterDto>> getAllCharacters(
            @RequestParam(defaultValue = "0") @Min(0) int page,
            @RequestParam(defaultValue = "20") @Min(1) @Max(100) int size,
            @RequestParam(required = false) String crew,
            @RequestParam(required = false) @Min(0) Long minBounty,
            @RequestParam(defaultValue = "bounty") String sortBy,
            @RequestParam(defaultValue = "desc") String sortDir) {

        log.info("🔍 Fetching characters - page: {}, size: {}, crew: {}, minBounty: {}",
                page, size, crew, minBounty);

        // Create search criteria
        CharacterSearchCriteria criteria = CharacterSearchCriteria.builder()
            .crew(crew)
            .minBounty(minBounty)
            .build();

        // Create pageable with sorting
        Sort sort = Sort.by(sortDir.equalsIgnoreCase("desc") ?
                           Sort.Direction.DESC : Sort.Direction.ASC, sortBy);
        Pageable pageable = PageRequest.of(page, size, sort);

        // Fetch characters
        Page<Character> charactersPage = characterService.findAll(criteria, pageable);

        // Convert to DTOs
        List<CharacterDto> characterDtos = charactersPage.getContent().stream()
            .map(this::convertToDto)
            .collect(Collectors.toList());

        // Build response
        PagedResponse<CharacterDto> response = PagedResponse.<CharacterDto>builder()
            .content(characterDtos)
            .page(charactersPage.getNumber())
            .size(charactersPage.getSize())
            .totalElements(charactersPage.getTotalElements())
            .totalPages(charactersPage.getTotalPages())
            .first(charactersPage.isFirst())
            .last(charactersPage.isLast())
            .build();

        log.info("✅ Retrieved {} characters out of {} total",
                characterDtos.size(), charactersPage.getTotalElements());

        return ResponseEntity.ok(response);
    }

    /**
     * Get character by ID
     * Demonstrates: Path variables, caching, error handling
     */
    @GetMapping("/{id}")
    @Cacheable(value = "character", key = "#id")
    public ResponseEntity<CharacterDto> getCharacter(@PathVariable @Min(1) Long id) {
        log.info("🔍 Fetching character with id: {}", id);

        Optional<Character> character = characterService.findById(id);

        if (character.isPresent()) {
            CharacterDto dto = convertToDto(character.get());
            log.info("✅ Found character: {}", dto.getName());
            return ResponseEntity.ok(dto);
        } else {
            log.warn("❌ Character not found with id: {}", id);
            return ResponseEntity.notFound().build();
        }
    }

    /**
     * Create new character
     * Demonstrates: POST method, validation, security, cache eviction
     */
    @PostMapping
    @PreAuthorize("hasRole('ADMIN')")
    @CacheEvict(value = "characters", allEntries = true)
    public ResponseEntity<CharacterDto> createCharacter(
            @Valid @RequestBody CreateCharacterRequest request,
            Authentication authentication) {

        log.info("🆕 Creating new character: {} by user: {}",
                request.getName(), authentication.getName());

        try {
            Character character = Character.builder()
                .name(request.getName())
                .bounty(request.getBounty())
                .type(request.getType())
                .crew(request.getCrewId() != null ?
                      crewService.findById(request.getCrewId()).orElse(null) : null)
                .createdBy(authentication.getName())
                .build();

            Character savedCharacter = characterService.save(character);
            CharacterDto dto = convertToDto(savedCharacter);

            // Send notification
            notificationService.notifyCharacterCreated(savedCharacter);

            log.info("✅ Character created successfully: {} with id: {}",
                    dto.getName(), dto.getId());

            return ResponseEntity.status(HttpStatus.CREATED).body(dto);

        } catch (ValidationException e) {
            log.error("❌ Validation error creating character: {}", e.getMessage());
            return ResponseEntity.badRequest().build();
        } catch (Exception e) {
            log.error("❌ Error creating character: {}", e.getMessage(), e);
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
        }
    }

    /**
     * Execute character trade
     * Demonstrates: Complex business logic, transactions, security, async processing
     */
    @PostMapping("/{characterId}/trade")
    @PreAuthorize("hasRole('TRADER')")
    public ResponseEntity<TradeResult> tradeCharacter(
            @PathVariable @Min(1) Long characterId,
            @Valid @RequestBody TradeRequest request,
            Authentication authentication) {

        log.info("💰 Trade request for character {} by user {} - Price: {}",
                characterId, authentication.getName(), request.getPrice());

        try {
            // Validate character exists
            Character character = characterService.findById(characterId)
                .orElseThrow(() -> new CharacterNotFoundException("Character not found: " + characterId));

            // Execute trade
            TradeResult result = tradingService.executeTrade(
                characterId,
                request,
                authentication.getName()
            );

            if (result.isSuccessful()) {
                log.info("✅ Trade executed successfully: {} - New balance: {}",
                        result.getTradeId(), result.getNewBalance());

                // Clear relevant caches
                cacheManager.getCache("character").evict(characterId);
                cacheManager.getCache("characters").clear();

                return ResponseEntity.ok(result);
            } else {
                log.warn("❌ Trade failed: {}", result.getMessage());
                return ResponseEntity.badRequest().body(result);
            }

        } catch (CharacterNotFoundException e) {
            log.error("❌ Character not found for trade: {}", characterId);
            return ResponseEntity.notFound().build();
        } catch (InsufficientFundsException e) {
            log.warn("❌ Insufficient funds for trade: {}", e.getMessage());
            TradeResult errorResult = TradeResult.builder()
                .status("FAILED")
                .message("Insufficient funds for this trade")
                .build();
            return ResponseEntity.badRequest().body(errorResult);
        } catch (Exception e) {
            log.error("❌ Unexpected error during trade: {}", e.getMessage(), e);
            TradeResult errorResult = TradeResult.builder()
                .status("ERROR")
                .message("An unexpected error occurred. Please try again.")
                .build();
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(errorResult);
        }
    }

    /**
     * Get character trading history
     * Demonstrates: Complex queries, pagination, security
     */
    @GetMapping("/{characterId}/trades")
    @PreAuthorize("hasRole('USER')")
    public ResponseEntity<PagedResponse<TradeDto>> getCharacterTrades(
            @PathVariable @Min(1) Long characterId,
            @RequestParam(defaultValue = "0") @Min(0) int page,
            @RequestParam(defaultValue = "10") @Min(1) @Max(50) int size) {

        log.info("📊 Fetching trade history for character: {}", characterId);

        Pageable pageable = PageRequest.of(page, size, Sort.by("executedAt").descending());
        Page<Trade> tradesPage = tradingService.getCharacterTrades(characterId, pageable);

        List<TradeDto> tradeDtos = tradesPage.getContent().stream()
            .map(this::convertToTradeDto)
            .collect(Collectors.toList());

        PagedResponse<TradeDto> response = PagedResponse.<TradeDto>builder()
            .content(tradeDtos)
            .page(tradesPage.getNumber())
            .size(tradesPage.getSize())
            .totalElements(tradesPage.getTotalElements())
            .totalPages(tradesPage.getTotalPages())
            .build();

        log.info("✅ Retrieved {} trades for character {}", tradeDtos.size(), characterId);

        return ResponseEntity.ok(response);
    }

    // Helper methods for DTO conversion
    private CharacterDto convertToDto(Character character) {
        return CharacterDto.builder()
            .id(character.getId())
            .name(character.getName())
            .bounty(character.getBounty())
            .type(character.getType())
            .crewName(character.getCrew() != null ? character.getCrew().getName() : null)
            .marketValue(character.getMarketValue())
            .createdAt(character.getCreatedAt())
            .updatedAt(character.getUpdatedAt())
            .build();
    }

    private TradeDto convertToTradeDto(Trade trade) {
        return TradeDto.builder()
            .id(trade.getId())
            .buyerId(trade.getBuyerId())
            .sellerId(trade.getSellerId())
            .characterId(trade.getCharacterId())
            .price(trade.getPrice())
            .status(trade.getStatus())
            .executedAt(trade.getExecutedAt())
            .build();
    }
}

// TODO 2: ENTITY MODELS (JPA/HIBERNATE - GOOGLE PATTERN)
// ═══════════════════════════════════════════════════════════
/*
🎯 YOUR TASK: Create JPA entities like Google's enterprise systems

GOOGLE'S DATA LAYER APPROACH:
- JPA entities for object-relational mapping
- Hibernate for database operations
- Validation annotations for data integrity
- Audit trails for enterprise compliance

CHARACTER ENTITY (MAPS TO YOUR DATABASE):
*/

package com.onepiece.trading.entity;

import javax.persistence.*;
import javax.validation.constraints.*;
import java.math.BigDecimal;
import java.time.LocalDateTime;
import java.util.List;

/**
 * 🏴‍☠️ Character Entity - Enterprise JPA Model
 * 
 * This maps to your existing character table but with enterprise features:
 * - JPA annotations for ORM mapping
 * - Validation constraints for data integrity
 * - Audit fields for compliance
 * - Relationships for complex queries
 */
@Entity
@Table(name = "characters", indexes = {
    @Index(name = "idx_character_name", columnList = "name"),
    @Index(name = "idx_character_crew", columnList = "crew"),
    @Index(name = "idx_character_price", columnList = "current_price")
})
public class Character {
    
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    @NotBlank(message = "Character name is required")
    @Size(min = 2, max = 100, message = "Name must be between 2 and 100 characters")
    @Column(nullable = false, unique = true)
    private String name;
    
    @NotBlank(message = "Crew is required")
    @Column(nullable = false)
    private String crew;
    
    @NotNull(message = "Current price is required")
    @DecimalMin(value = "0.0", inclusive = false, message = "Price must be positive")
    @Column(name = "current_price", precision = 10, scale = 2)
    private BigDecimal currentPrice;
    
    @Column(name = "devil_fruit")
    private String devilFruit;
    
    @Column(name = "bounty", precision = 15, scale = 0)
    private BigDecimal bounty;
    
    @Enumerated(EnumType.STRING)
    @Column(nullable = false)
    private CharacterRarity rarity;
    
    @Column(name = "image_url")
    private String imageUrl;
    
    @Column(columnDefinition = "TEXT")
    private String description;
    
    // Audit fields (Enterprise requirement)
    @Column(name = "created_at", nullable = false, updatable = false)
    private LocalDateTime createdAt;
    
    @Column(name = "updated_at")
    private LocalDateTime updatedAt;
    
    @Column(name = "created_by")
    private String createdBy;
    
    // Relationships (Enterprise data modeling)
    @OneToMany(mappedBy = "character", cascade = CascadeType.ALL, fetch = FetchType.LAZY)
    private List<Trade> trades;
    
    @OneToMany(mappedBy = "character", cascade = CascadeType.ALL, fetch = FetchType.LAZY)
    private List<PriceHistory> priceHistory;
    
    // Constructors
    public Character() {}
    
    public Character(String name, String crew, BigDecimal currentPrice, CharacterRarity rarity) {
        this.name = name;
        this.crew = crew;
        this.currentPrice = currentPrice;
        this.rarity = rarity;
        this.createdAt = LocalDateTime.now();
        this.updatedAt = LocalDateTime.now();
    }
    
    // JPA Lifecycle callbacks (Enterprise audit trail)
    @PrePersist
    protected void onCreate() {
        createdAt = LocalDateTime.now();
        updatedAt = LocalDateTime.now();
    }
    
    @PreUpdate
    protected void onUpdate() {
        updatedAt = LocalDateTime.now();
    }
    
    // Getters and Setters (Enterprise bean pattern)
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    
    public String getCrew() { return crew; }
    public void setCrew(String crew) { this.crew = crew; }
    
    public BigDecimal getCurrentPrice() { return currentPrice; }
    public void setCurrentPrice(BigDecimal currentPrice) { this.currentPrice = currentPrice; }
    
    public String getDevilFruit() { return devilFruit; }
    public void setDevilFruit(String devilFruit) { this.devilFruit = devilFruit; }
    
    public BigDecimal getBounty() { return bounty; }
    public void setBounty(BigDecimal bounty) { this.bounty = bounty; }
    
    public CharacterRarity getRarity() { return rarity; }
    public void setRarity(CharacterRarity rarity) { this.rarity = rarity; }
    
    public String getImageUrl() { return imageUrl; }
    public void setImageUrl(String imageUrl) { this.imageUrl = imageUrl; }
    
    public String getDescription() { return description; }
    public void setDescription(String description) { this.description = description; }
    
    public LocalDateTime getCreatedAt() { return createdAt; }
    public LocalDateTime getUpdatedAt() { return updatedAt; }
    
    public String getCreatedBy() { return createdBy; }
    public void setCreatedBy(String createdBy) { this.createdBy = createdBy; }
    
    public List<Trade> getTrades() { return trades; }
    public void setTrades(List<Trade> trades) { this.trades = trades; }
    
    public List<PriceHistory> getPriceHistory() { return priceHistory; }
    public void setPriceHistory(List<PriceHistory> priceHistory) { this.priceHistory = priceHistory; }
    
    // Enterprise toString method
    @Override
    public String toString() {
        return String.format("Character{id=%d, name='%s', crew='%s', price=%s, rarity=%s}", 
                           id, name, crew, currentPrice, rarity);
    }
}

// Character Rarity Enum (Enterprise type safety)
enum CharacterRarity {
    COMMON("Common", 1.0),
    UNCOMMON("Uncommon", 1.5),
    RARE("Rare", 2.0),
    EPIC("Epic", 3.0),
    LEGENDARY("Legendary", 5.0),
    MYTHICAL("Mythical", 10.0);
    
    private final String displayName;
    private final double multiplier;
    
    CharacterRarity(String displayName, double multiplier) {
        this.displayName = displayName;
        this.multiplier = multiplier;
    }
    
    public String getDisplayName() { return displayName; }
    public double getMultiplier() { return multiplier; }
}

// TODO 3: REPOSITORY LAYER (SPRING DATA JPA - AMAZON PATTERN)
// ═══════════════════════════════════════════════════════════
/*
🎯 YOUR TASK: Create repository layer like Amazon's data access

AMAZON'S REPOSITORY PATTERN:
- Spring Data JPA for automatic query generation
- Custom queries for complex business logic
- Pagination and sorting for large datasets
- Caching for performance optimization

CHARACTER REPOSITORY:
*/

package com.onepiece.trading.repository;

import com.onepiece.trading.entity.Character;
import com.onepiece.trading.entity.CharacterRarity;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.cache.annotation.Cacheable;
import org.springframework.stereotype.Repository;

import java.math.BigDecimal;
import java.util.List;
import java.util.Optional;

/**
 * 🏴‍☠️ Character Repository - Enterprise Data Access Layer
 * 
 * This is how Amazon structures their data access:
 * - JpaRepository for CRUD operations
 * - Custom queries for business logic
 * - Caching for performance
 * - Pagination for large datasets
 */
@Repository
public interface CharacterRepository extends JpaRepository<Character, Long> {
    
    // Spring Data JPA automatic query generation
    Optional<Character> findByName(String name);
    
    List<Character> findByCrew(String crew);
    
    List<Character> findByRarity(CharacterRarity rarity);
    
    Page<Character> findByCrewContainingIgnoreCase(String crew, Pageable pageable);
    
    // Custom queries for complex business logic (Amazon pattern)
    @Query("SELECT c FROM Character c WHERE c.currentPrice BETWEEN :minPrice AND :maxPrice")
    List<Character> findByPriceRange(@Param("minPrice") BigDecimal minPrice, 
                                   @Param("maxPrice") BigDecimal maxPrice);
    
    @Query("SELECT c FROM Character c WHERE c.bounty > :minBounty ORDER BY c.bounty DESC")
    List<Character> findHighBountyCharacters(@Param("minBounty") BigDecimal minBounty);
    
    @Query("SELECT c FROM Character c WHERE c.devilFruit IS NOT NULL")
    List<Character> findDevilFruitUsers();
    
    // Native SQL for complex analytics (Enterprise reporting)
    @Query(value = "SELECT crew, COUNT(*) as character_count, AVG(current_price) as avg_price " +
                   "FROM characters GROUP BY crew ORDER BY character_count DESC", 
           nativeQuery = true)
    List<Object[]> getCrewStatistics();
    
    // Cached queries for performance (Netflix pattern)
    @Cacheable("popularCharacters")
    @Query("SELECT c FROM Character c JOIN c.trades t GROUP BY c ORDER BY COUNT(t) DESC")
    List<Character> findMostTradedCharacters(Pageable pageable);
    
    // Search functionality (Google-style search)
    @Query("SELECT c FROM Character c WHERE " +
           "LOWER(c.name) LIKE LOWER(CONCAT('%', :searchTerm, '%')) OR " +
           "LOWER(c.crew) LIKE LOWER(CONCAT('%', :searchTerm, '%')) OR " +
           "LOWER(c.devilFruit) LIKE LOWER(CONCAT('%', :searchTerm, '%'))")
    Page<Character> searchCharacters(@Param("searchTerm") String searchTerm, Pageable pageable);
    
    // Business logic queries
    @Query("SELECT COUNT(c) FROM Character c WHERE c.rarity = :rarity")
    long countByRarity(@Param("rarity") CharacterRarity rarity);
    
    @Query("SELECT c FROM Character c WHERE c.currentPrice = " +
           "(SELECT MAX(c2.currentPrice) FROM Character c2)")
    Optional<Character> findMostExpensiveCharacter();
    
    @Query("SELECT c FROM Character c WHERE c.bounty = " +
           "(SELECT MAX(c2.bounty) FROM Character c2 WHERE c2.bounty IS NOT NULL)")
    Optional<Character> findHighestBountyCharacter();
}

// TODO 4: SERVICE LAYER (BUSINESS LOGIC - LINKEDIN PATTERN)
// ═══════════════════════════════════════════════════════════
/*
🎯 YOUR TASK: Create service layer like LinkedIn's business logic

LINKEDIN'S SERVICE PATTERN:
- @Service annotation for business logic
- @Transactional for data consistency
- DTO pattern for data transfer
- Exception handling for error management
- Validation for business rules

CHARACTER SERVICE:
*/

package com.onepiece.trading.service;

import com.onepiece.trading.entity.Character;
import com.onepiece.trading.entity.CharacterRarity;
import com.onepiece.trading.repository.CharacterRepository;
import com.onepiece.trading.dto.CharacterDTO;
import com.onepiece.trading.dto.CharacterCreateDTO;
import com.onepiece.trading.dto.CharacterUpdateDTO;
import com.onepiece.trading.exception.CharacterNotFoundException;
import com.onepiece.trading.exception.DuplicateCharacterException;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.cache.annotation.CacheEvict;
import org.springframework.cache.annotation.Cacheable;

import java.math.BigDecimal;
import java.util.List;
import java.util.stream.Collectors;

/**
 * 🏴‍☠️ Character Service - Enterprise Business Logic Layer
 * 
 * This is how LinkedIn structures their business logic:
 * - @Service for business operations
 * - @Transactional for data consistency
 * - DTO pattern for clean API contracts
 * - Exception handling for error management
 */
@Service
@Transactional
public class CharacterService {
    
    private final CharacterRepository characterRepository;
    
    @Autowired
    public CharacterService(CharacterRepository characterRepository) {
        this.characterRepository = characterRepository;
    }
    
    // READ OPERATIONS (with caching like Netflix)
    @Cacheable("characters")
    @Transactional(readOnly = true)
    public List<CharacterDTO> getAllCharacters() {
        return characterRepository.findAll()
                .stream()
                .map(this::convertToDTO)
                .collect(Collectors.toList());
    }
    
    @Cacheable("character")
    @Transactional(readOnly = true)
    public CharacterDTO getCharacterById(Long id) {
        Character character = characterRepository.findById(id)
                .orElseThrow(() -> new CharacterNotFoundException("Character not found with id: " + id));
        return convertToDTO(character);
    }
    
    @Transactional(readOnly = true)
    public CharacterDTO getCharacterByName(String name) {
        Character character = characterRepository.findByName(name)
                .orElseThrow(() -> new CharacterNotFoundException("Character not found with name: " + name));
        return convertToDTO(character);
    }
    
    @Transactional(readOnly = true)
    public Page<CharacterDTO> searchCharacters(String searchTerm, Pageable pageable) {
        return characterRepository.searchCharacters(searchTerm, pageable)
                .map(this::convertToDTO);
    }
    
    @Transactional(readOnly = true)
    public List<CharacterDTO> getCharactersByCrew(String crew) {
        return characterRepository.findByCrew(crew)
                .stream()
                .map(this::convertToDTO)
                .collect(Collectors.toList());
    }
    
    @Transactional(readOnly = true)
    public List<CharacterDTO> getCharactersByPriceRange(BigDecimal minPrice, BigDecimal maxPrice) {
        return characterRepository.findByPriceRange(minPrice, maxPrice)
                .stream()
                .map(this::convertToDTO)
                .collect(Collectors.toList());
    }
    
    // WRITE OPERATIONS (with cache invalidation)
    @CacheEvict(value = {"characters", "popularCharacters"}, allEntries = true)
    public CharacterDTO createCharacter(CharacterCreateDTO createDTO) {
        // Business validation
        if (characterRepository.findByName(createDTO.getName()).isPresent()) {
            throw new DuplicateCharacterException("Character already exists with name: " + createDTO.getName());
        }
        
        // Create entity from DTO
        Character character = new Character(
            createDTO.getName(),
            createDTO.getCrew(),
            createDTO.getCurrentPrice(),
            createDTO.getRarity()
        );
        
        character.setDevilFruit(createDTO.getDevilFruit());
        character.setBounty(createDTO.getBounty());
        character.setImageUrl(createDTO.getImageUrl());
        character.setDescription(createDTO.getDescription());
        character.setCreatedBy("SYSTEM"); // In real app, get from security context
        
        Character savedCharacter = characterRepository.save(character);
        return convertToDTO(savedCharacter);
    }
    
    @CacheEvict(value = {"character", "characters", "popularCharacters"}, allEntries = true)
    public CharacterDTO updateCharacter(Long id, CharacterUpdateDTO updateDTO) {
        Character character = characterRepository.findById(id)
                .orElseThrow(() -> new CharacterNotFoundException("Character not found with id: " + id));
        
        // Update fields if provided
        if (updateDTO.getCurrentPrice() != null) {
            character.setCurrentPrice(updateDTO.getCurrentPrice());
        }
        if (updateDTO.getDevilFruit() != null) {
            character.setDevilFruit(updateDTO.getDevilFruit());
        }
        if (updateDTO.getBounty() != null) {
            character.setBounty(updateDTO.getBounty());
        }
        if (updateDTO.getImageUrl() != null) {
            character.setImageUrl(updateDTO.getImageUrl());
        }
        if (updateDTO.getDescription() != null) {
            character.setDescription(updateDTO.getDescription());
        }
        
        Character updatedCharacter = characterRepository.save(character);
        return convertToDTO(updatedCharacter);
    }
    
    @CacheEvict(value = {"character", "characters", "popularCharacters"}, allEntries = true)
    public void deleteCharacter(Long id) {
        if (!characterRepository.existsById(id)) {
            throw new CharacterNotFoundException("Character not found with id: " + id);
        }
        characterRepository.deleteById(id);
    }
    
    // BUSINESS LOGIC METHODS
    @Transactional(readOnly = true)
    public List<CharacterDTO> getMostTradedCharacters(int limit) {
        Pageable pageable = Pageable.ofSize(limit);
        return characterRepository.findMostTradedCharacters(pageable)
                .stream()
                .map(this::convertToDTO)
                .collect(Collectors.toList());
    }
    
    @Transactional(readOnly = true)
    public CharacterDTO getMostExpensiveCharacter() {
        Character character = characterRepository.findMostExpensiveCharacter()
                .orElseThrow(() -> new CharacterNotFoundException("No characters found"));
        return convertToDTO(character);
    }
    
    // DTO CONVERSION (Enterprise pattern)
    private CharacterDTO convertToDTO(Character character) {
        CharacterDTO dto = new CharacterDTO();
        dto.setId(character.getId());
        dto.setName(character.getName());
        dto.setCrew(character.getCrew());
        dto.setCurrentPrice(character.getCurrentPrice());
        dto.setDevilFruit(character.getDevilFruit());
        dto.setBounty(character.getBounty());
        dto.setRarity(character.getRarity());
        dto.setImageUrl(character.getImageUrl());
        dto.setDescription(character.getDescription());
        dto.setCreatedAt(character.getCreatedAt());
        dto.setUpdatedAt(character.getUpdatedAt());
        return dto;
    }
}

/*
═══════════════════════════════════════════════════════════════════════════════
🎯 WHAT'S NEXT? YOUR JAVA SPRING BOOT IMPLEMENTATION
═══════════════════════════════════════════════════════════════════════════════

🏴‍☠️ CONGRATULATIONS! You now understand enterprise Java like big tech!

📚 WHAT YOU JUST LEARNED:
✅ Spring Boot application structure (Netflix pattern)
✅ JPA/Hibernate entity modeling (Google approach)
✅ Repository pattern with Spring Data (Amazon style)
✅ Service layer with business logic (LinkedIn pattern)
✅ Enterprise design patterns and best practices
✅ Caching strategies for performance
✅ Transaction management for data consistency
✅ Exception handling and validation

🎯 HOW THIS CONNECTS TO YOUR ONE PIECE PROJECT:
├── REPLACES: Your Node.js character service with Java
├── SCALES: To enterprise level like Netflix/Amazon
├── INTEGRATES: With your existing MySQL database
├── PROVIDES: Enterprise-grade features and patterns
└── DEMONSTRATES: Why big tech chooses Java for core services

🎯 BIG TECH ENTERPRISE FEATURES YOU NOW HAVE:
✅ JPA/Hibernate ORM (like Google's data layer)
✅ Spring Data repositories (like Amazon's data access)
✅ Service layer architecture (like LinkedIn's business logic)
✅ Caching with Spring Cache (like Netflix's performance)
✅ Transaction management (like enterprise banking systems)
✅ Validation and exception handling (like production systems)

🔥 NEXT STEPS:
1. Create the REST controller layer (API endpoints)
2. Add Spring Security (authentication/authorization)
3. Implement microservices communication
4. Add monitoring and metrics
5. Deploy with Docker and Kubernetes

🎯 CAREER IMPACT:
With these Java Spring Boot skills, you're now qualified for:
- Senior Java Developer: $120K - $180K
- Enterprise Architect: $150K - $220K
- Big Tech Backend Engineer: $180K - $300K

🚀 You now understand why Netflix, Amazon, and Google use Java! ⚔️
*/

// TODO 5: REST CONTROLLER LAYER (NETFLIX API PATTERN)
// ═══════════════════════════════════════════════════════════
/*
🎯 YOUR TASK: Create REST controllers like Netflix's API layer

NETFLIX'S REST API APPROACH:
- @RestController for RESTful endpoints
- @RequestMapping for URL routing
- @Valid for request validation
- ResponseEntity for HTTP responses
- Exception handling with @ControllerAdvice

CHARACTER REST CONTROLLER:
*/

package com.onepiece.trading.controller;

import com.onepiece.trading.dto.CharacterDTO;
import com.onepiece.trading.dto.CharacterCreateDTO;
import com.onepiece.trading.dto.CharacterUpdateDTO;
import com.onepiece.trading.service.CharacterService;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import javax.validation.Valid;
import java.math.BigDecimal;
import java.util.List;

/**
 * 🏴‍☠️ Character REST Controller - Netflix-style API Layer
 *
 * This is how Netflix structures their REST APIs:
 * - RESTful endpoints with proper HTTP methods
 * - Request/Response DTOs for clean contracts
 * - Validation and error handling
 * - Pagination for large datasets
 */
@RestController
@RequestMapping("/api/v1/characters")
@CrossOrigin(origins = "*") // Allow frontend connections
public class CharacterController {

    private final CharacterService characterService;

    @Autowired
    public CharacterController(CharacterService characterService) {
        this.characterService = characterService;
    }

    // GET /api/v1/characters - Get all characters
    @GetMapping
    public ResponseEntity<List<CharacterDTO>> getAllCharacters() {
        List<CharacterDTO> characters = characterService.getAllCharacters();
        return ResponseEntity.ok(characters);
    }

    // GET /api/v1/characters/{id} - Get character by ID
    @GetMapping("/{id}")
    public ResponseEntity<CharacterDTO> getCharacterById(@PathVariable Long id) {
        CharacterDTO character = characterService.getCharacterById(id);
        return ResponseEntity.ok(character);
    }

    // GET /api/v1/characters/name/{name} - Get character by name
    @GetMapping("/name/{name}")
    public ResponseEntity<CharacterDTO> getCharacterByName(@PathVariable String name) {
        CharacterDTO character = characterService.getCharacterByName(name);
        return ResponseEntity.ok(character);
    }

    // GET /api/v1/characters/search - Search characters
    @GetMapping("/search")
    public ResponseEntity<Page<CharacterDTO>> searchCharacters(
            @RequestParam String q,
            Pageable pageable) {
        Page<CharacterDTO> characters = characterService.searchCharacters(q, pageable);
        return ResponseEntity.ok(characters);
    }

    // GET /api/v1/characters/crew/{crew} - Get characters by crew
    @GetMapping("/crew/{crew}")
    public ResponseEntity<List<CharacterDTO>> getCharactersByCrew(@PathVariable String crew) {
        List<CharacterDTO> characters = characterService.getCharactersByCrew(crew);
        return ResponseEntity.ok(characters);
    }

    // GET /api/v1/characters/price-range - Get characters by price range
    @GetMapping("/price-range")
    public ResponseEntity<List<CharacterDTO>> getCharactersByPriceRange(
            @RequestParam BigDecimal minPrice,
            @RequestParam BigDecimal maxPrice) {
        List<CharacterDTO> characters = characterService.getCharactersByPriceRange(minPrice, maxPrice);
        return ResponseEntity.ok(characters);
    }

    // GET /api/v1/characters/most-traded - Get most traded characters
    @GetMapping("/most-traded")
    public ResponseEntity<List<CharacterDTO>> getMostTradedCharacters(
            @RequestParam(defaultValue = "10") int limit) {
        List<CharacterDTO> characters = characterService.getMostTradedCharacters(limit);
        return ResponseEntity.ok(characters);
    }

    // GET /api/v1/characters/most-expensive - Get most expensive character
    @GetMapping("/most-expensive")
    public ResponseEntity<CharacterDTO> getMostExpensiveCharacter() {
        CharacterDTO character = characterService.getMostExpensiveCharacter();
        return ResponseEntity.ok(character);
    }

    // POST /api/v1/characters - Create new character
    @PostMapping
    public ResponseEntity<CharacterDTO> createCharacter(@Valid @RequestBody CharacterCreateDTO createDTO) {
        CharacterDTO character = characterService.createCharacter(createDTO);
        return ResponseEntity.status(HttpStatus.CREATED).body(character);
    }

    // PUT /api/v1/characters/{id} - Update character
    @PutMapping("/{id}")
    public ResponseEntity<CharacterDTO> updateCharacter(
            @PathVariable Long id,
            @Valid @RequestBody CharacterUpdateDTO updateDTO) {
        CharacterDTO character = characterService.updateCharacter(id, updateDTO);
        return ResponseEntity.ok(character);
    }

    // DELETE /api/v1/characters/{id} - Delete character
    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteCharacter(@PathVariable Long id) {
        characterService.deleteCharacter(id);
        return ResponseEntity.noContent().build();
    }
}

// TODO 6: DTO CLASSES (ENTERPRISE DATA TRANSFER PATTERN)
// ═══════════════════════════════════════════════════════════
/*
🎯 YOUR TASK: Create DTOs like enterprise applications

ENTERPRISE DTO PATTERN:
- Separate DTOs for different operations
- Validation annotations for data integrity
- Clean separation between API and domain models
- Immutable objects where possible

CHARACTER DTOs:
*/

package com.onepiece.trading.dto;

import com.onepiece.trading.entity.CharacterRarity;
import javax.validation.constraints.*;
import java.math.BigDecimal;
import java.time.LocalDateTime;

/**
 * 🏴‍☠️ Character DTO - Data Transfer Object for API responses
 */
public class CharacterDTO {
    private Long id;
    private String name;
    private String crew;
    private BigDecimal currentPrice;
    private String devilFruit;
    private BigDecimal bounty;
    private CharacterRarity rarity;
    private String imageUrl;
    private String description;
    private LocalDateTime createdAt;
    private LocalDateTime updatedAt;

    // Constructors, getters, and setters
    public CharacterDTO() {}

    // Getters and Setters
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }

    public String getName() { return name; }
    public void setName(String name) { this.name = name; }

    public String getCrew() { return crew; }
    public void setCrew(String crew) { this.crew = crew; }

    public BigDecimal getCurrentPrice() { return currentPrice; }
    public void setCurrentPrice(BigDecimal currentPrice) { this.currentPrice = currentPrice; }

    public String getDevilFruit() { return devilFruit; }
    public void setDevilFruit(String devilFruit) { this.devilFruit = devilFruit; }

    public BigDecimal getBounty() { return bounty; }
    public void setBounty(BigDecimal bounty) { this.bounty = bounty; }

    public CharacterRarity getRarity() { return rarity; }
    public void setRarity(CharacterRarity rarity) { this.rarity = rarity; }

    public String getImageUrl() { return imageUrl; }
    public void setImageUrl(String imageUrl) { this.imageUrl = imageUrl; }

    public String getDescription() { return description; }
    public void setDescription(String description) { this.description = description; }

    public LocalDateTime getCreatedAt() { return createdAt; }
    public void setCreatedAt(LocalDateTime createdAt) { this.createdAt = createdAt; }

    public LocalDateTime getUpdatedAt() { return updatedAt; }
    public void setUpdatedAt(LocalDateTime updatedAt) { this.updatedAt = updatedAt; }
}

/**
 * 🏴‍☠️ Character Create DTO - For creating new characters
 */
class CharacterCreateDTO {
    @NotBlank(message = "Character name is required")
    @Size(min = 2, max = 100, message = "Name must be between 2 and 100 characters")
    private String name;

    @NotBlank(message = "Crew is required")
    private String crew;

    @NotNull(message = "Current price is required")
    @DecimalMin(value = "0.0", inclusive = false, message = "Price must be positive")
    private BigDecimal currentPrice;

    @NotNull(message = "Rarity is required")
    private CharacterRarity rarity;

    private String devilFruit;
    private BigDecimal bounty;
    private String imageUrl;
    private String description;

    // Constructors, getters, and setters
    public CharacterCreateDTO() {}

    public String getName() { return name; }
    public void setName(String name) { this.name = name; }

    public String getCrew() { return crew; }
    public void setCrew(String crew) { this.crew = crew; }

    public BigDecimal getCurrentPrice() { return currentPrice; }
    public void setCurrentPrice(BigDecimal currentPrice) { this.currentPrice = currentPrice; }

    public CharacterRarity getRarity() { return rarity; }
    public void setRarity(CharacterRarity rarity) { this.rarity = rarity; }

    public String getDevilFruit() { return devilFruit; }
    public void setDevilFruit(String devilFruit) { this.devilFruit = devilFruit; }

    public BigDecimal getBounty() { return bounty; }
    public void setBounty(BigDecimal bounty) { this.bounty = bounty; }

    public String getImageUrl() { return imageUrl; }
    public void setImageUrl(String imageUrl) { this.imageUrl = imageUrl; }

    public String getDescription() { return description; }
    public void setDescription(String description) { this.description = description; }
}

/**
 * 🏴‍☠️ Character Update DTO - For updating existing characters
 */
class CharacterUpdateDTO {
    @DecimalMin(value = "0.0", inclusive = false, message = "Price must be positive")
    private BigDecimal currentPrice;

    private String devilFruit;
    private BigDecimal bounty;
    private String imageUrl;
    private String description;

    // Constructors, getters, and setters
    public CharacterUpdateDTO() {}

    public BigDecimal getCurrentPrice() { return currentPrice; }
    public void setCurrentPrice(BigDecimal currentPrice) { this.currentPrice = currentPrice; }

    public String getDevilFruit() { return devilFruit; }
    public void setDevilFruit(String devilFruit) { this.devilFruit = devilFruit; }

    public BigDecimal getBounty() { return bounty; }
    public void setBounty(BigDecimal bounty) { this.bounty = bounty; }

    public String getImageUrl() { return imageUrl; }
    public void setImageUrl(String imageUrl) { this.imageUrl = imageUrl; }

    public String getDescription() { return description; }
    public void setDescription(String description) { this.description = description; }
}

/*
================================================================================
🎓 ADVANCED JAVA ENTERPRISE DEVELOPMENT TUTORIAL
================================================================================

This comprehensive tutorial covers 8 essential topics for enterprise Java development:
1. Exception Handling (try-catch, custom exceptions)
2. Generics (type safety, wildcards)
3. Lambda Expressions and Stream API
4. Multithreading and Concurrency
5. File I/O and Serialization
6. Design Patterns
7. Spring Framework
8. Database Integration (JPA/Hibernate)

All examples use the One Piece Trading Platform as the context.
================================================================================
*/

/*
================================================================================
TOPIC 1: EXCEPTION HANDLING
================================================================================

Exception handling is critical in enterprise applications to:
- Handle errors gracefully without crashing the application
- Provide meaningful error messages to users
- Log errors for debugging and monitoring
- Maintain data integrity during failures
- Implement retry logic and fallback mechanisms

EXCEPTION HIERARCHY:
- Throwable (root)
  - Error (system errors, don't catch these)
  - Exception
    - RuntimeException (unchecked exceptions)
    - Checked Exceptions (must be caught or declared)

BEST PRACTICES:
1. Use specific exceptions, not generic Exception
2. Create custom exceptions for business logic errors
3. Always clean up resources (use try-with-resources)
4. Log exceptions with context information
5. Don't swallow exceptions silently
6. Use exception chaining to preserve stack traces
================================================================================
*/

// Custom Exception Classes for One Piece Trading Platform

/**
 * Base exception for all trading platform errors
 * This follows the pattern used by big tech companies to create
 * a hierarchy of custom exceptions
 */
class TradingPlatformException extends Exception {
    private final String errorCode;
    private final long timestamp;

    public TradingPlatformException(String message, String errorCode) {
        super(message);
        this.errorCode = errorCode;
        this.timestamp = System.currentTimeMillis();
    }

    public TradingPlatformException(String message, String errorCode, Throwable cause) {
        super(message, cause);
        this.errorCode = errorCode;
        this.timestamp = System.currentTimeMillis();
    }

    public String getErrorCode() { return errorCode; }
    public long getTimestamp() { return timestamp; }

    @Override
    public String toString() {
        return String.format("[%s] %s (Code: %s, Time: %d)",
            getClass().getSimpleName(), getMessage(), errorCode, timestamp);
    }
}

/**
 * Thrown when a user has insufficient funds for a transaction
 */
class InsufficientFundsException extends TradingPlatformException {
    private final double required;
    private final double available;

    public InsufficientFundsException(double required, double available) {
        super(String.format("Insufficient funds. Required: %.2f Berry, Available: %.2f Berry",
            required, available), "INSUFFICIENT_FUNDS");
        this.required = required;
        this.available = available;
    }

    public double getRequired() { return required; }
    public double getAvailable() { return available; }
}

/**
 * Thrown when a Devil Fruit is not found in the system
 */
class DevilFruitNotFoundException extends TradingPlatformException {
    private final String fruitName;

    public DevilFruitNotFoundException(String fruitName) {
        super("Devil Fruit not found: " + fruitName, "FRUIT_NOT_FOUND");
        this.fruitName = fruitName;
    }

    public String getFruitName() { return fruitName; }
}

/**
 * Thrown when a user tries to buy a fruit they already own
 */
class DuplicatePurchaseException extends TradingPlatformException {
    private final String fruitName;

    public DuplicatePurchaseException(String fruitName) {
        super("You already own this Devil Fruit: " + fruitName, "DUPLICATE_PURCHASE");
        this.fruitName = fruitName;
    }

    public String getFruitName() { return fruitName; }
}

/**
 * Thrown when database operations fail
 */
class DatabaseException extends TradingPlatformException {
    public DatabaseException(String message, Throwable cause) {
        super(message, "DATABASE_ERROR", cause);
    }
}

/**
 * Thrown when external API calls fail
 */
class ExternalServiceException extends TradingPlatformException {
    private final String serviceName;

    public ExternalServiceException(String serviceName, String message, Throwable cause) {
        super(String.format("External service '%s' failed: %s", serviceName, message),
            "EXTERNAL_SERVICE_ERROR", cause);
        this.serviceName = serviceName;
    }

    public String getServiceName() { return serviceName; }
}

/**
 * Enterprise-grade Trading Service with comprehensive exception handling
 */
class EnterpriseTradeService {
    private static final int MAX_RETRY_ATTEMPTS = 3;
    private static final long RETRY_DELAY_MS = 1000;

    /**
     * Process a trade with comprehensive error handling
     * This demonstrates enterprise patterns:
     * - Input validation
     * - Business logic validation
     * - Transaction management
     * - Retry logic
     * - Detailed logging
     */
    public TradeResult processTrade(String userId, String fruitName, double price) {
        TradeResult result = new TradeResult();

        try {
            // Step 1: Validate inputs
            validateTradeInputs(userId, fruitName, price);

            // Step 2: Check user balance
            double userBalance = getUserBalance(userId);
            if (userBalance < price) {
                throw new InsufficientFundsException(price, userBalance);
            }

            // Step 3: Check if fruit exists
            if (!devilFruitExists(fruitName)) {
                throw new DevilFruitNotFoundException(fruitName);
            }

            // Step 4: Check for duplicate purchase
            if (userOwnsDevilFruit(userId, fruitName)) {
                throw new DuplicatePurchaseException(fruitName);
            }

            // Step 5: Execute trade with retry logic
            executeTradeWithRetry(userId, fruitName, price);

            result.setSuccess(true);
            result.setMessage("Trade completed successfully!");
            result.setTransactionId(generateTransactionId());

        } catch (InsufficientFundsException e) {
            // Handle insufficient funds - user-friendly message
            result.setSuccess(false);
            result.setMessage(e.getMessage());
            result.setErrorCode(e.getErrorCode());
            logError("Insufficient funds for trade", e);

        } catch (DevilFruitNotFoundException e) {
            // Handle fruit not found
            result.setSuccess(false);
            result.setMessage(e.getMessage());
            result.setErrorCode(e.getErrorCode());
            logError("Devil Fruit not found", e);

        } catch (DuplicatePurchaseException e) {
            // Handle duplicate purchase
            result.setSuccess(false);
            result.setMessage(e.getMessage());
            result.setErrorCode(e.getErrorCode());
            logWarning("Duplicate purchase attempt", e);

        } catch (DatabaseException e) {
            // Handle database errors - critical
            result.setSuccess(false);
            result.setMessage("System error. Please try again later.");
            result.setErrorCode(e.getErrorCode());
            logCritical("Database error during trade", e);

        } catch (TradingPlatformException e) {
            // Handle other platform exceptions
            result.setSuccess(false);
            result.setMessage(e.getMessage());
            result.setErrorCode(e.getErrorCode());
            logError("Trading platform error", e);

        } catch (Exception e) {
            // Catch-all for unexpected errors
            result.setSuccess(false);
            result.setMessage("An unexpected error occurred. Please contact support.");
            result.setErrorCode("UNKNOWN_ERROR");
            logCritical("Unexpected error during trade", e);

        } finally {
            // Always execute cleanup code
            // This runs whether an exception occurred or not
            result.setProcessingTime(System.currentTimeMillis());
            logTradeAttempt(userId, fruitName, result.isSuccess());
        }

        return result;
    }

    /**
     * Execute trade with retry logic for transient failures
     * This is a common enterprise pattern for handling temporary issues
     */
    private void executeTradeWithRetry(String userId, String fruitName, double price)
            throws TradingPlatformException {
        int attempts = 0;
        Exception lastException = null;

        while (attempts < MAX_RETRY_ATTEMPTS) {
            try {
                // Attempt the trade
                executeTrade(userId, fruitName, price);
                return; // Success!

            } catch (DatabaseException e) {
                // Database might be temporarily unavailable
                lastException = e;
                attempts++;

                if (attempts < MAX_RETRY_ATTEMPTS) {
                    logWarning(String.format("Trade attempt %d failed, retrying...", attempts), e);
                    try {
                        Thread.sleep(RETRY_DELAY_MS * attempts); // Exponential backoff
                    } catch (InterruptedException ie) {
                        Thread.currentThread().interrupt();
                        throw new TradingPlatformException("Trade interrupted", "INTERRUPTED", ie);
                    }
                }
            }
        }

        // All retries failed
        throw new DatabaseException("Trade failed after " + MAX_RETRY_ATTEMPTS + " attempts",
            lastException);
    }

    // Helper methods (simplified for demonstration)
    private void validateTradeInputs(String userId, String fruitName, double price)
            throws TradingPlatformException {
        if (userId == null || userId.trim().isEmpty()) {
            throw new TradingPlatformException("User ID cannot be empty", "INVALID_USER_ID");
        }
        if (fruitName == null || fruitName.trim().isEmpty()) {
            throw new TradingPlatformException("Fruit name cannot be empty", "INVALID_FRUIT_NAME");
        }
        if (price <= 0) {
            throw new TradingPlatformException("Price must be positive", "INVALID_PRICE");
        }
    }

    private double getUserBalance(String userId) throws DatabaseException {
        // In real app, this would query the database
        return 1000000.0; // 1 million Berry
    }

    private boolean devilFruitExists(String fruitName) {
        return true; // Simplified
    }

    private boolean userOwnsDevilFruit(String userId, String fruitName) {
        return false; // Simplified
    }

    private void executeTrade(String userId, String fruitName, double price)
            throws DatabaseException {
        // Actual trade execution logic
        // In real app, this would update database records
    }

    private String generateTransactionId() {
        return "TXN-" + System.currentTimeMillis();
    }

    private void logError(String message, Exception e) {
        System.err.println("[ERROR] " + message + ": " + e);
    }

    private void logWarning(String message, Exception e) {
        System.out.println("[WARN] " + message + ": " + e);
    }

    private void logCritical(String message, Exception e) {
        System.err.println("[CRITICAL] " + message + ": " + e);
        // In real app, send alert to monitoring system
    }

    private void logTradeAttempt(String userId, String fruitName, boolean success) {
        System.out.println(String.format("[AUDIT] User %s attempted to trade for %s: %s",
            userId, fruitName, success ? "SUCCESS" : "FAILED"));
    }
}

/**
 * Result object for trade operations
 */
class TradeResult {
    private boolean success;
    private String message;
    private String errorCode;
    private String transactionId;
    private long processingTime;

    // Getters and setters
    public boolean isSuccess() { return success; }
    public void setSuccess(boolean success) { this.success = success; }

    public String getMessage() { return message; }
    public void setMessage(String message) { this.message = message; }

    public String getErrorCode() { return errorCode; }
    public void setErrorCode(String errorCode) { this.errorCode = errorCode; }

    public String getTransactionId() { return transactionId; }
    public void setTransactionId(String transactionId) { this.transactionId = transactionId; }

    public long getProcessingTime() { return processingTime; }
    public void setProcessingTime(long processingTime) { this.processingTime = processingTime; }
}

/**
 * Try-with-resources example for automatic resource management
 * This ensures resources are always closed, even if exceptions occur
 */
class ResourceManagementExample {

    /**
     * Read trade history from a file using try-with-resources
     * The file will be automatically closed even if an exception occurs
     */
    public void readTradeHistory(String filename) {
        // Try-with-resources: resources declared here are auto-closed
        try (java.io.BufferedReader reader = new java.io.BufferedReader(
                new java.io.FileReader(filename))) {

            String line;
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
            }

        } catch (java.io.FileNotFoundException e) {
            System.err.println("Trade history file not found: " + filename);
        } catch (java.io.IOException e) {
            System.err.println("Error reading trade history: " + e.getMessage());
        }
        // No need for finally block - reader is automatically closed!
    }

    /**
     * Multiple resources in try-with-resources
     */
    public void copyTradeData(String source, String destination) {
        try (java.io.BufferedReader reader = new java.io.BufferedReader(
                new java.io.FileReader(source));
             java.io.BufferedWriter writer = new java.io.BufferedWriter(
                new java.io.FileWriter(destination))) {

            String line;
            while ((line = reader.readLine()) != null) {
                writer.write(line);
                writer.newLine();
            }

        } catch (java.io.IOException e) {
            System.err.println("Error copying trade data: " + e.getMessage());
        }
        // Both reader and writer are automatically closed in reverse order
    }
}

/**
 * EXCEPTION HANDLING DEMO
 */
class ExceptionHandlingDemo {
    public static void runDemo() {
        System.out.println("\n" + "=".repeat(80));
        System.out.println("TOPIC 1: EXCEPTION HANDLING DEMO");
        System.out.println("=".repeat(80));

        EnterpriseTradeService tradeService = new EnterpriseTradeService();

        // Test Case 1: Successful trade
        System.out.println("\n--- Test 1: Successful Trade ---");
        TradeResult result1 = tradeService.processTrade("luffy", "Gomu Gomu no Mi", 500000);
        System.out.println("Result: " + result1.getMessage());
        System.out.println("Transaction ID: " + result1.getTransactionId());

        // Test Case 2: Invalid input
        System.out.println("\n--- Test 2: Invalid Input ---");
        TradeResult result2 = tradeService.processTrade("", "Gomu Gomu no Mi", 500000);
        System.out.println("Result: " + result2.getMessage());
        System.out.println("Error Code: " + result2.getErrorCode());

        // Test Case 3: Negative price
        System.out.println("\n--- Test 3: Invalid Price ---");
        TradeResult result3 = tradeService.processTrade("luffy", "Gomu Gomu no Mi", -100);
        System.out.println("Result: " + result3.getMessage());

        System.out.println("\n" + "=".repeat(80));
        System.out.println("KEY TAKEAWAYS:");
        System.out.println("1. Custom exceptions provide meaningful error information");
        System.out.println("2. Exception hierarchy helps organize error handling");
        System.out.println("3. Try-catch blocks prevent application crashes");
        System.out.println("4. Finally blocks ensure cleanup code always runs");
        System.out.println("5. Try-with-resources automatically manages resource cleanup");
        System.out.println("6. Retry logic handles transient failures");
        System.out.println("7. Proper logging helps debug issues in production");
        System.out.println("=".repeat(80));
    }
}

/*
================================================================================
TOPIC 2: GENERICS
================================================================================

Generics provide type safety at compile time, preventing runtime ClassCastException.
They allow you to write reusable code that works with different types while
maintaining type safety.

WHY GENERICS MATTER IN ENTERPRISE:
1. Type Safety: Catch errors at compile time, not runtime
2. Code Reusability: Write once, use with multiple types
3. Eliminate Casting: No need for explicit type casting
4. Better IDE Support: Auto-completion and type checking
5. Self-Documenting Code: Types are explicit in the signature

GENERIC SYNTAX:
- <T> - Type parameter (can be any name, T is convention)
- <E> - Element (used in collections)
- <K, V> - Key, Value (used in maps)
- <? extends Type> - Upper bounded wildcard
- <? super Type> - Lower bounded wildcard
- <?> - Unbounded wildcard

BEST PRACTICES:
1. Use meaningful type parameter names for clarity
2. Prefer bounded wildcards for API flexibility
3. Use generics for collections to avoid casting
4. Don't use raw types (List instead of List<String>)
5. Be careful with generic arrays (they have limitations)
================================================================================
*/

/**
 * Generic Repository Pattern - Enterprise Standard
 * This is used by all major tech companies for data access
 *
 * @param <T> The entity type this repository manages
 * @param <ID> The type of the entity's identifier
 */
interface GenericRepository<T, ID> {
    T save(T entity);
    T findById(ID id);
    List<T> findAll();
    void delete(ID id);
    boolean exists(ID id);
    long count();
}

/**
 * Generic Response Wrapper - Common in REST APIs
 * Used by companies like Google, Amazon, Netflix
 *
 * @param <T> The type of data being returned
 */
class ApiResponse<T> {
    private boolean success;
    private String message;
    private T data;
    private String errorCode;
    private long timestamp;

    // Constructor for success
    public ApiResponse(T data) {
        this.success = true;
        this.data = data;
        this.message = "Success";
        this.timestamp = System.currentTimeMillis();
    }

    // Constructor for error
    public ApiResponse(String message, String errorCode) {
        this.success = false;
        this.message = message;
        this.errorCode = errorCode;
        this.timestamp = System.currentTimeMillis();
    }

    // Static factory methods for cleaner code
    public static <T> ApiResponse<T> success(T data) {
        return new ApiResponse<>(data);
    }

    public static <T> ApiResponse<T> error(String message, String errorCode) {
        return new ApiResponse<>(message, errorCode);
    }

    // Getters
    public boolean isSuccess() { return success; }
    public String getMessage() { return message; }
    public T getData() { return data; }
    public String getErrorCode() { return errorCode; }
    public long getTimestamp() { return timestamp; }
}

/**
 * Generic Pair class - useful for returning two values
 *
 * @param <F> First element type
 * @param <S> Second element type
 */
class Pair<F, S> {
    private final F first;
    private final S second;

    public Pair(F first, S second) {
        this.first = first;
        this.second = second;
    }

    public F getFirst() { return first; }
    public S getSecond() { return second; }

    @Override
    public String toString() {
        return "(" + first + ", " + second + ")";
    }

    // Static factory method
    public static <F, S> Pair<F, S> of(F first, S second) {
        return new Pair<>(first, second);
    }
}

/**
 * Generic Cache implementation
 * This demonstrates multiple type parameters and bounded types
 *
 * @param <K> Key type (must be comparable for sorting)
 * @param <V> Value type
 */
class Cache<K extends Comparable<K>, V> {
    private final Map<K, CacheEntry<V>> cache;
    private final long ttlMillis;

    public Cache(long ttlMillis) {
        this.cache = new HashMap<>();
        this.ttlMillis = ttlMillis;
    }

    public void put(K key, V value) {
        cache.put(key, new CacheEntry<>(value, System.currentTimeMillis() + ttlMillis));
    }

    public V get(K key) {
        CacheEntry<V> entry = cache.get(key);
        if (entry == null) {
            return null;
        }

        // Check if expired
        if (System.currentTimeMillis() > entry.expiryTime) {
            cache.remove(key);
            return null;
        }

        return entry.value;
    }

    public void clear() {
        cache.clear();
    }

    public int size() {
        return cache.size();
    }

    // Inner generic class
    private static class CacheEntry<V> {
        final V value;
        final long expiryTime;

        CacheEntry(V value, long expiryTime) {
            this.value = value;
            this.expiryTime = expiryTime;
        }
    }
}

/**
 * Devil Fruit Repository using Generics
 * This shows how to implement the generic repository pattern
 */
class DevilFruitRepository implements GenericRepository<DevilFruit, String> {
    private final Map<String, DevilFruit> storage = new HashMap<>();

    @Override
    public DevilFruit save(DevilFruit fruit) {
        storage.put(fruit.getName(), fruit);
        return fruit;
    }

    @Override
    public DevilFruit findById(String name) {
        return storage.get(name);
    }

    @Override
    public List<DevilFruit> findAll() {
        return new ArrayList<>(storage.values());
    }

    @Override
    public void delete(String name) {
        storage.remove(name);
    }

    @Override
    public boolean exists(String name) {
        return storage.containsKey(name);
    }

    @Override
    public long count() {
        return storage.size();
    }

    // Custom query method using generics
    public <R> List<R> findAllAndTransform(java.util.function.Function<DevilFruit, R> transformer) {
        List<R> results = new ArrayList<>();
        for (DevilFruit fruit : storage.values()) {
            results.add(transformer.apply(fruit));
        }
        return results;
    }
}

/**
 * Generic Service Layer
 * This demonstrates bounded type parameters
 *
 * @param <T> Entity type that must extend BaseEntity
 * @param <ID> ID type that must be Comparable
 */
abstract class GenericService<T extends BaseEntity<ID>, ID extends Comparable<ID>> {
    protected final GenericRepository<T, ID> repository;

    public GenericService(GenericRepository<T, ID> repository) {
        this.repository = repository;
    }

    public ApiResponse<T> create(T entity) {
        try {
            T saved = repository.save(entity);
            return ApiResponse.success(saved);
        } catch (Exception e) {
            return ApiResponse.error("Failed to create entity", "CREATE_ERROR");
        }
    }

    public ApiResponse<T> getById(ID id) {
        T entity = repository.findById(id);
        if (entity == null) {
            return ApiResponse.error("Entity not found", "NOT_FOUND");
        }
        return ApiResponse.success(entity);
    }

    public ApiResponse<List<T>> getAll() {
        List<T> entities = repository.findAll();
        return ApiResponse.success(entities);
    }
}

/**
 * Base entity class for generic service
 */
abstract class BaseEntity<ID> {
    protected ID id;

    public ID getId() { return id; }
    public void setId(ID id) { this.id = id; }
}

/**
 * Wildcard Examples - Advanced Generics
 */
class WildcardExamples {

    /**
     * Upper bounded wildcard: <? extends Type>
     * Can READ from the collection, but not WRITE (except null)
     * Use when you want to consume items from a structure
     */
    public static double calculateTotalValue(List<? extends DevilFruit> fruits) {
        double total = 0;
        for (DevilFruit fruit : fruits) {
            total += fruit.getPrice();
        }
        return total;
    }

    /**
     * Lower bounded wildcard: <? super Type>
     * Can WRITE to the collection, but reading gives you Object
     * Use when you want to produce items into a structure
     */
    public static void addLegendaryFruits(List<? super DevilFruit> fruits) {
        fruits.add(new DevilFruit("Gomu Gomu no Mi", "Paramecia", 1000000));
        fruits.add(new DevilFruit("Mera Mera no Mi", "Logia", 2000000));
    }

    /**
     * Unbounded wildcard: <?>
     * Use when you don't care about the type
     */
    public static void printCollectionSize(List<?> list) {
        System.out.println("Collection size: " + list.size());
    }

    /**
     * Multiple bounds
     * Type must implement both Comparable and Serializable
     */
    public static <T extends Comparable<T> & java.io.Serializable> T findMax(List<T> list) {
        if (list.isEmpty()) {
            return null;
        }

        T max = list.get(0);
        for (T item : list) {
            if (item.compareTo(max) > 0) {
                max = item;
            }
        }
        return max;
    }
}

/**
 * Generic Builder Pattern
 * This is used extensively in enterprise applications
 *
 * @param <T> The type being built
 */
class GenericBuilder<T> {
    private final Class<T> type;
    private final Map<String, Object> properties = new HashMap<>();

    public GenericBuilder(Class<T> type) {
        this.type = type;
    }

    public GenericBuilder<T> with(String property, Object value) {
        properties.put(property, value);
        return this;
    }

    public T build() {
        try {
            T instance = type.getDeclaredConstructor().newInstance();
            // In real implementation, use reflection to set properties
            return instance;
        } catch (Exception e) {
            throw new RuntimeException("Failed to build instance", e);
        }
    }

    public static <T> GenericBuilder<T> of(Class<T> type) {
        return new GenericBuilder<>(type);
    }
}

/**
 * GENERICS DEMO
 */
class GenericsDemo {
    public static void runDemo() {
        System.out.println("\n" + "=".repeat(80));
        System.out.println("TOPIC 2: GENERICS DEMO");
        System.out.println("=".repeat(80));

        // Demo 1: Generic Repository
        System.out.println("\n--- Demo 1: Generic Repository ---");
        DevilFruitRepository repo = new DevilFruitRepository();
        repo.save(new DevilFruit("Gomu Gomu no Mi", "Paramecia", 1000000));
        repo.save(new DevilFruit("Mera Mera no Mi", "Logia", 2000000));
        repo.save(new DevilFruit("Ope Ope no Mi", "Paramecia", 5000000));

        System.out.println("Total fruits in repository: " + repo.count());
        DevilFruit fruit = repo.findById("Gomu Gomu no Mi");
        System.out.println("Found: " + fruit.getName() + " - " + fruit.getPrice() + " Berry");

        // Demo 2: Generic API Response
        System.out.println("\n--- Demo 2: Generic API Response ---");
        ApiResponse<DevilFruit> successResponse = ApiResponse.success(fruit);
        System.out.println("Success: " + successResponse.isSuccess());
        System.out.println("Data: " + successResponse.getData().getName());

        ApiResponse<DevilFruit> errorResponse = ApiResponse.error("Fruit not found", "404");
        System.out.println("Error: " + errorResponse.getMessage());
        System.out.println("Error Code: " + errorResponse.getErrorCode());

        // Demo 3: Generic Pair
        System.out.println("\n--- Demo 3: Generic Pair ---");
        Pair<String, Double> fruitPrice = Pair.of("Gomu Gomu no Mi", 1000000.0);
        System.out.println("Fruit: " + fruitPrice.getFirst());
        System.out.println("Price: " + fruitPrice.getSecond() + " Berry");

        Pair<DevilFruit, Integer> fruitQuantity = Pair.of(fruit, 5);
        System.out.println("Available: " + fruitQuantity.getSecond() + " x " +
            fruitQuantity.getFirst().getName());

        // Demo 4: Generic Cache
        System.out.println("\n--- Demo 4: Generic Cache ---");
        Cache<String, DevilFruit> cache = new Cache<>(5000); // 5 second TTL
        cache.put("legendary", new DevilFruit("Gomu Gomu no Mi", "Paramecia", 1000000));

        DevilFruit cached = cache.get("legendary");
        System.out.println("Cached fruit: " + (cached != null ? cached.getName() : "null"));

        // Demo 5: Wildcards
        System.out.println("\n--- Demo 5: Wildcards ---");
        List<DevilFruit> fruits = repo.findAll();
        double totalValue = WildcardExamples.calculateTotalValue(fruits);
        System.out.println("Total value of all fruits: " + totalValue + " Berry");

        System.out.println("\n" + "=".repeat(80));
        System.out.println("KEY TAKEAWAYS:");
        System.out.println("1. Generics provide compile-time type safety");
        System.out.println("2. Generic classes can work with multiple types");
        System.out.println("3. Bounded types restrict what types can be used");
        System.out.println("4. Wildcards provide flexibility in method parameters");
        System.out.println("5. Upper bounds (extends) for reading, lower bounds (super) for writing");
        System.out.println("6. Generic methods can infer types from arguments");
        System.out.println("7. Repository pattern with generics is industry standard");
        System.out.println("=".repeat(80));
    }
}

/*
================================================================================
TOPIC 3: LAMBDA EXPRESSIONS AND STREAM API
================================================================================

Lambda expressions (introduced in Java 8) enable functional programming in Java.
The Stream API provides a powerful way to process collections of data.

WHY LAMBDAS AND STREAMS MATTER IN ENTERPRISE:
1. Concise Code: Less boilerplate, more readable
2. Functional Programming: Declarative style (what, not how)
3. Parallel Processing: Easy parallelization for performance
4. Lazy Evaluation: Operations only execute when needed
5. Immutability: Streams don't modify the source
6. Composability: Chain operations together

LAMBDA SYNTAX:
(parameters) -> expression
(parameters) -> { statements; }

FUNCTIONAL INTERFACES (have exactly one abstract method):
- Predicate<T>: T -> boolean (test/filter)
- Function<T,R>: T -> R (transform)
- Consumer<T>: T -> void (consume/process)
- Supplier<T>: () -> T (supply/create)
- BiFunction<T,U,R>: (T,U) -> R (two inputs)

STREAM OPERATIONS:
Intermediate (return Stream): filter, map, flatMap, sorted, distinct, limit, skip
Terminal (return result): forEach, collect, reduce, count, anyMatch, allMatch, findFirst

BEST PRACTICES:
1. Use method references when possible (Class::method)
2. Keep lambdas short and focused
3. Avoid side effects in lambda expressions
4. Use parallel streams carefully (overhead for small collections)
5. Prefer streams for complex data transformations
================================================================================
*/

/**
 * Functional Interfaces for Devil Fruit Trading
 */
@FunctionalInterface
interface FruitValidator {
    boolean validate(DevilFruit fruit);

    // Default methods are allowed in functional interfaces
    default FruitValidator and(FruitValidator other) {
        return fruit -> this.validate(fruit) && other.validate(fruit);
    }

    default FruitValidator or(FruitValidator other) {
        return fruit -> this.validate(fruit) || other.validate(fruit);
    }
}

@FunctionalInterface
interface PriceCalculator {
    double calculate(DevilFruit fruit, double multiplier);
}

@FunctionalInterface
interface FruitTransformer<R> {
    R transform(DevilFruit fruit);
}

/**
 * Enterprise Trading Analytics using Streams
 * This demonstrates real-world use cases for Stream API
 */
class TradingAnalytics {
    private final List<DevilFruit> fruits;
    private final List<Trade> trades;

    public TradingAnalytics(List<DevilFruit> fruits, List<Trade> trades) {
        this.fruits = fruits;
        this.trades = trades;
    }

    /**
     * Example 1: Filter and Map
     * Find all Logia fruits and get their names
     */
    public List<String> getLogiaFruitNames() {
        return fruits.stream()
            .filter(fruit -> "Logia".equals(fruit.getType()))
            .map(DevilFruit::getName)
            .collect(java.util.stream.Collectors.toList());
    }

    /**
     * Example 2: Sorting and Limiting
     * Get top 5 most expensive fruits
     */
    public List<DevilFruit> getTopExpensiveFruits(int limit) {
        return fruits.stream()
            .sorted((f1, f2) -> Double.compare(f2.getPrice(), f1.getPrice()))
            .limit(limit)
            .collect(java.util.stream.Collectors.toList());
    }

    /**
     * Example 3: Grouping
     * Group fruits by type
     */
    public Map<String, List<DevilFruit>> groupByType() {
        return fruits.stream()
            .collect(java.util.stream.Collectors.groupingBy(DevilFruit::getType));
    }

    /**
     * Example 4: Aggregation
     * Calculate total value of all fruits
     */
    public double calculateTotalValue() {
        return fruits.stream()
            .mapToDouble(DevilFruit::getPrice)
            .sum();
    }

    /**
     * Example 5: Statistics
     * Get price statistics
     */
    public PriceStatistics getPriceStatistics() {
        java.util.DoubleSummaryStatistics stats = fruits.stream()
            .mapToDouble(DevilFruit::getPrice)
            .summaryStatistics();

        return new PriceStatistics(
            stats.getMin(),
            stats.getMax(),
            stats.getAverage(),
            stats.getCount()
        );
    }

    /**
     * Example 6: Complex Filtering with Multiple Conditions
     * Find affordable Paramecia fruits
     */
    public List<DevilFruit> findAffordableParamecia(double maxPrice) {
        return fruits.stream()
            .filter(fruit -> "Paramecia".equals(fruit.getType()))
            .filter(fruit -> fruit.getPrice() <= maxPrice)
            .sorted((f1, f2) -> Double.compare(f1.getPrice(), f2.getPrice()))
            .collect(java.util.stream.Collectors.toList());
    }

    /**
     * Example 7: FlatMap - Flatten nested structures
     * Get all unique buyers from all trades
     */
    public List<String> getAllUniqueBuyers() {
        return trades.stream()
            .map(Trade::getBuyerId)
            .distinct()
            .sorted()
            .collect(java.util.stream.Collectors.toList());
    }

    /**
     * Example 8: Reduce - Custom aggregation
     * Calculate total trading volume
     */
    public double calculateTotalTradingVolume() {
        return trades.stream()
            .map(Trade::getAmount)
            .reduce(0.0, Double::sum);
    }

    /**
     * Example 9: Partitioning
     * Separate expensive and affordable fruits
     */
    public Map<Boolean, List<DevilFruit>> partitionByPrice(double threshold) {
        return fruits.stream()
            .collect(java.util.stream.Collectors.partitioningBy(
                fruit -> fruit.getPrice() > threshold
            ));
    }

    /**
     * Example 10: Custom Collector
     * Create a summary report
     */
    public String generateSummaryReport() {
        return fruits.stream()
            .map(fruit -> String.format("%s (%s): %.0f Berry",
                fruit.getName(), fruit.getType(), fruit.getPrice()))
            .collect(java.util.stream.Collectors.joining("\n",
                "=== DEVIL FRUIT INVENTORY ===\n",
                "\n=== END OF REPORT ==="));
    }

    /**
     * Example 11: Parallel Stream for Performance
     * Process large dataset in parallel
     */
    public long countExpensiveFruitsParallel(double threshold) {
        return fruits.parallelStream()
            .filter(fruit -> fruit.getPrice() > threshold)
            .count();
    }

    /**
     * Example 12: Method Reference Examples
     */
    public void demonstrateMethodReferences() {
        // Static method reference
        fruits.stream()
            .map(DevilFruit::getName)
            .forEach(System.out::println);

        // Instance method reference
        fruits.stream()
            .filter(this::isExpensive)
            .forEach(System.out::println);

        // Constructor reference
        List<String> names = fruits.stream()
            .map(DevilFruit::getName)
            .collect(java.util.stream.Collectors.toCollection(ArrayList::new));
    }

    private boolean isExpensive(DevilFruit fruit) {
        return fruit.getPrice() > 1000000;
    }

    /**
     * Example 13: Optional to handle null safely
     */
    public java.util.Optional<DevilFruit> findMostExpensiveFruit() {
        return fruits.stream()
            .max((f1, f2) -> Double.compare(f1.getPrice(), f2.getPrice()));
    }

    /**
     * Example 14: Combining multiple operations
     * Complex business logic using streams
     */
    public Map<String, Double> calculateAveragePriceByType() {
        return fruits.stream()
            .collect(java.util.stream.Collectors.groupingBy(
                DevilFruit::getType,
                java.util.stream.Collectors.averagingDouble(DevilFruit::getPrice)
            ));
    }

    /**
     * Example 15: Custom filtering with functional interface
     */
    public List<DevilFruit> filterFruits(FruitValidator validator) {
        return fruits.stream()
            .filter(validator::validate)
            .collect(java.util.stream.Collectors.toList());
    }
}

/**
 * Trade entity for analytics
 */
class Trade {
    private String tradeId;
    private String buyerId;
    private String sellerId;
    private String fruitName;
    private double amount;
    private long timestamp;

    public Trade(String tradeId, String buyerId, String sellerId,
                 String fruitName, double amount) {
        this.tradeId = tradeId;
        this.buyerId = buyerId;
        this.sellerId = sellerId;
        this.fruitName = fruitName;
        this.amount = amount;
        this.timestamp = System.currentTimeMillis();
    }

    // Getters
    public String getTradeId() { return tradeId; }
    public String getBuyerId() { return buyerId; }
    public String getSellerId() { return sellerId; }
    public String getFruitName() { return fruitName; }
    public double getAmount() { return amount; }
    public long getTimestamp() { return timestamp; }
}

/**
 * Price statistics result
 */
class PriceStatistics {
    private final double min;
    private final double max;
    private final double average;
    private final long count;

    public PriceStatistics(double min, double max, double average, long count) {
        this.min = min;
        this.max = max;
        this.average = average;
        this.count = count;
    }

    public double getMin() { return min; }
    public double getMax() { return max; }
    public double getAverage() { return average; }
    public long getCount() { return count; }

    @Override
    public String toString() {
        return String.format("Min: %.0f, Max: %.0f, Avg: %.2f, Count: %d",
            min, max, average, count);
    }
}

/**
 * Advanced Lambda Examples
 */
class AdvancedLambdaExamples {

    /**
     * Lambda with multiple parameters
     */
    public static double applyDiscount(DevilFruit fruit, double discountPercent) {
        PriceCalculator calculator = (f, discount) -> f.getPrice() * (1 - discount / 100);
        return calculator.calculate(fruit, discountPercent);
    }

    /**
     * Lambda with block body
     */
    public static FruitValidator createComplexValidator(double minPrice, double maxPrice) {
        return fruit -> {
            if (fruit == null) return false;
            if (fruit.getPrice() < minPrice) return false;
            if (fruit.getPrice() > maxPrice) return false;
            return fruit.getType() != null && !fruit.getType().isEmpty();
        };
    }

    /**
     * Composing validators
     */
    public static List<DevilFruit> filterWithComposedValidators(List<DevilFruit> fruits) {
        FruitValidator isExpensive = fruit -> fruit.getPrice() > 1000000;
        FruitValidator isLogia = fruit -> "Logia".equals(fruit.getType());
        FruitValidator combined = isExpensive.and(isLogia);

        return fruits.stream()
            .filter(combined::validate)
            .collect(java.util.stream.Collectors.toList());
    }

    /**
     * Higher-order function: function that returns a function
     */
    public static java.util.function.Function<DevilFruit, String> createFormatter(String format) {
        return fruit -> String.format(format, fruit.getName(), fruit.getType(), fruit.getPrice());
    }
}

/**
 * LAMBDA AND STREAM API DEMO
 */
class LambdaStreamDemo {
    public static void runDemo() {
        System.out.println("\n" + "=".repeat(80));
        System.out.println("TOPIC 3: LAMBDA EXPRESSIONS AND STREAM API DEMO");
        System.out.println("=".repeat(80));

        // Setup test data
        List<DevilFruit> fruits = Arrays.asList(
            new DevilFruit("Gomu Gomu no Mi", "Paramecia", 1000000),
            new DevilFruit("Mera Mera no Mi", "Logia", 2000000),
            new DevilFruit("Ope Ope no Mi", "Paramecia", 5000000),
            new DevilFruit("Goro Goro no Mi", "Logia", 3000000),
            new DevilFruit("Hito Hito no Mi", "Zoan", 500000),
            new DevilFruit("Yami Yami no Mi", "Logia", 4000000)
        );

        List<Trade> trades = Arrays.asList(
            new Trade("T1", "luffy", "shanks", "Gomu Gomu no Mi", 1000000),
            new Trade("T2", "ace", "whitebeard", "Mera Mera no Mi", 2000000),
            new Trade("T3", "law", "doflamingo", "Ope Ope no Mi", 5000000)
        );

        TradingAnalytics analytics = new TradingAnalytics(fruits, trades);

        // Demo 1: Filter and Map
        System.out.println("\n--- Demo 1: Logia Fruits ---");
        List<String> logiaNames = analytics.getLogiaFruitNames();
        logiaNames.forEach(name -> System.out.println("- " + name));

        // Demo 2: Top Expensive Fruits
        System.out.println("\n--- Demo 2: Top 3 Most Expensive Fruits ---");
        analytics.getTopExpensiveFruits(3).forEach(fruit ->
            System.out.println(fruit.getName() + ": " + fruit.getPrice() + " Berry")
        );

        // Demo 3: Group by Type
        System.out.println("\n--- Demo 3: Fruits Grouped by Type ---");
        analytics.groupByType().forEach((type, fruitList) -> {
            System.out.println(type + ": " + fruitList.size() + " fruits");
        });

        // Demo 4: Total Value
        System.out.println("\n--- Demo 4: Total Inventory Value ---");
        System.out.println("Total: " + analytics.calculateTotalValue() + " Berry");

        // Demo 5: Statistics
        System.out.println("\n--- Demo 5: Price Statistics ---");
        System.out.println(analytics.getPriceStatistics());

        // Demo 6: Complex Filtering
        System.out.println("\n--- Demo 6: Affordable Paramecia (< 2M Berry) ---");
        analytics.findAffordableParamecia(2000000).forEach(fruit ->
            System.out.println(fruit.getName() + ": " + fruit.getPrice() + " Berry")
        );

        // Demo 7: Partitioning
        System.out.println("\n--- Demo 7: Partition by Price (threshold: 2M) ---");
        Map<Boolean, List<DevilFruit>> partitioned = analytics.partitionByPrice(2000000);
        System.out.println("Expensive (>2M): " + partitioned.get(true).size());
        System.out.println("Affordable (<=2M): " + partitioned.get(false).size());

        // Demo 8: Summary Report
        System.out.println("\n--- Demo 8: Summary Report ---");
        System.out.println(analytics.generateSummaryReport());

        // Demo 9: Custom Validator
        System.out.println("\n--- Demo 9: Custom Validator (Expensive Logia) ---");
        FruitValidator validator = fruit ->
            "Logia".equals(fruit.getType()) && fruit.getPrice() > 1500000;
        analytics.filterFruits(validator).forEach(fruit ->
            System.out.println(fruit.getName())
        );

        // Demo 10: Optional
        System.out.println("\n--- Demo 10: Most Expensive Fruit ---");
        analytics.findMostExpensiveFruit().ifPresent(fruit ->
            System.out.println(fruit.getName() + ": " + fruit.getPrice() + " Berry")
        );

        System.out.println("\n" + "=".repeat(80));
        System.out.println("KEY TAKEAWAYS:");
        System.out.println("1. Lambdas provide concise syntax for functional programming");
        System.out.println("2. Streams enable declarative data processing");
        System.out.println("3. Method references make code even more readable");
        System.out.println("4. Intermediate operations are lazy (only execute when needed)");
        System.out.println("5. Terminal operations trigger stream processing");
        System.out.println("6. Collectors provide powerful ways to aggregate data");
        System.out.println("7. Parallel streams can improve performance for large datasets");
        System.out.println("8. Optional helps avoid null pointer exceptions");
        System.out.println("=".repeat(80));
    }
}

/*
================================================================================
TOPIC 4: MULTITHREADING AND CONCURRENCY
================================================================================

Multithreading allows multiple tasks to run concurrently, improving performance
and responsiveness in enterprise applications.

WHY MULTITHREADING MATTERS IN ENTERPRISE:
1. Performance: Utilize multiple CPU cores
2. Responsiveness: Keep UI responsive while processing
3. Scalability: Handle multiple requests simultaneously
4. Resource Utilization: Better use of system resources
5. Asynchronous Processing: Background tasks, batch jobs

KEY CONCEPTS:
- Thread: Independent path of execution
- Synchronization: Coordinate access to shared resources
- Thread Safety: Code that works correctly with multiple threads
- Race Condition: Bug when timing affects correctness
- Deadlock: Threads waiting for each other indefinitely
- Thread Pool: Reusable threads for better performance

CONCURRENCY UTILITIES (java.util.concurrent):
- ExecutorService: Manage thread pools
- Future/CompletableFuture: Asynchronous results
- CountDownLatch: Wait for multiple threads
- CyclicBarrier: Synchronization point for threads
- Semaphore: Limit concurrent access
- ConcurrentHashMap: Thread-safe map
- AtomicInteger/AtomicLong: Thread-safe counters

BEST PRACTICES:
1. Use ExecutorService instead of creating threads manually
2. Prefer immutable objects for thread safety
3. Use concurrent collections instead of synchronized collections
4. Avoid shared mutable state when possible
5. Use CompletableFuture for async operations
6. Always shut down ExecutorService properly
7. Be careful with synchronized blocks (can cause deadlocks)
================================================================================
*/

/**
 * Thread-Safe Trading Order Book
 * Uses ConcurrentHashMap for thread safety
 */
class OrderBook {
    private final java.util.concurrent.ConcurrentHashMap<String, Order> orders;
    private final java.util.concurrent.atomic.AtomicLong orderIdCounter;

    public OrderBook() {
        this.orders = new java.util.concurrent.ConcurrentHashMap<>();
        this.orderIdCounter = new java.util.concurrent.atomic.AtomicLong(0);
    }

    /**
     * Place an order (thread-safe)
     */
    public String placeOrder(String userId, String fruitName, double price, int quantity) {
        String orderId = "ORD-" + orderIdCounter.incrementAndGet();
        Order order = new Order(orderId, userId, fruitName, price, quantity);
        orders.put(orderId, order);
        System.out.println(Thread.currentThread().getName() + " placed order: " + orderId);
        return orderId;
    }

    /**
     * Cancel an order (thread-safe)
     */
    public boolean cancelOrder(String orderId) {
        Order removed = orders.remove(orderId);
        if (removed != null) {
            System.out.println(Thread.currentThread().getName() + " cancelled order: " + orderId);
            return true;
        }
        return false;
    }

    /**
     * Get order count (thread-safe)
     */
    public int getOrderCount() {
        return orders.size();
    }

    /**
     * Get all orders (returns snapshot)
     */
    public List<Order> getAllOrders() {
        return new ArrayList<>(orders.values());
    }
}

/**
 * Order entity
 */
class Order {
    private final String orderId;
    private final String userId;
    private final String fruitName;
    private final double price;
    private final int quantity;
    private final long timestamp;

    public Order(String orderId, String userId, String fruitName, double price, int quantity) {
        this.orderId = orderId;
        this.userId = userId;
        this.fruitName = fruitName;
        this.price = price;
        this.quantity = quantity;
        this.timestamp = System.currentTimeMillis();
    }

    // Getters
    public String getOrderId() { return orderId; }
    public String getUserId() { return userId; }
    public String getFruitName() { return fruitName; }
    public double getPrice() { return price; }
    public int getQuantity() { return quantity; }
    public long getTimestamp() { return timestamp; }
}

/**
 * Asynchronous Trade Processor using ExecutorService
 * This is how enterprise applications handle background tasks
 */
class AsyncTradeProcessor {
    private final java.util.concurrent.ExecutorService executorService;
    private final OrderBook orderBook;

    public AsyncTradeProcessor(int threadPoolSize) {
        this.executorService = java.util.concurrent.Executors.newFixedThreadPool(threadPoolSize);
        this.orderBook = new OrderBook();
    }

    /**
     * Process trade asynchronously using Future
     */
    public java.util.concurrent.Future<TradeResult> processTradeAsync(
            String userId, String fruitName, double price) {

        return executorService.submit(() -> {
            // Simulate processing time
            Thread.sleep(1000);

            // Process the trade
            System.out.println(Thread.currentThread().getName() +
                " processing trade for " + userId);

            TradeResult result = new TradeResult();
            result.setSuccess(true);
            result.setMessage("Trade processed successfully");
            result.setTransactionId("TXN-" + System.currentTimeMillis());

            return result;
        });
    }

    /**
     * Process multiple trades in parallel
     */
    public List<java.util.concurrent.Future<TradeResult>> processMultipleTrades(
            List<TradeRequest> requests) {

        List<java.util.concurrent.Future<TradeResult>> futures = new ArrayList<>();

        for (TradeRequest request : requests) {
            java.util.concurrent.Future<TradeResult> future =
                processTradeAsync(request.userId, request.fruitName, request.price);
            futures.add(future);
        }

        return futures;
    }

    /**
     * Shutdown the executor service
     */
    public void shutdown() {
        executorService.shutdown();
        try {
            if (!executorService.awaitTermination(60, java.util.concurrent.TimeUnit.SECONDS)) {
                executorService.shutdownNow();
            }
        } catch (InterruptedException e) {
            executorService.shutdownNow();
            Thread.currentThread().interrupt();
        }
    }

    public OrderBook getOrderBook() {
        return orderBook;
    }
}

/**
 * Trade request
 */
class TradeRequest {
    final String userId;
    final String fruitName;
    final double price;

    public TradeRequest(String userId, String fruitName, double price) {
        this.userId = userId;
        this.fruitName = fruitName;
        this.price = price;
    }
}

/**
 * CompletableFuture Examples - Modern Async Programming
 * This is the preferred way in modern Java applications
 */
class CompletableFutureExamples {

    /**
     * Simple async operation
     */
    public static java.util.concurrent.CompletableFuture<String> fetchFruitDataAsync(String fruitName) {
        return java.util.concurrent.CompletableFuture.supplyAsync(() -> {
            // Simulate API call
            try {
                Thread.sleep(500);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
            return "Data for " + fruitName;
        });
    }

    /**
     * Chain multiple async operations
     */
    public static java.util.concurrent.CompletableFuture<TradeResult> processTradeWithValidation(
            String userId, String fruitName, double price) {

        return java.util.concurrent.CompletableFuture
            // Step 1: Validate user
            .supplyAsync(() -> {
                System.out.println("Validating user: " + userId);
                return userId;
            })
            // Step 2: Check fruit availability
            .thenApplyAsync(user -> {
                System.out.println("Checking fruit availability: " + fruitName);
                return new Pair<>(user, fruitName);
            })
            // Step 3: Process payment
            .thenApplyAsync(pair -> {
                System.out.println("Processing payment: " + price);
                TradeResult result = new TradeResult();
                result.setSuccess(true);
                result.setMessage("Trade completed");
                return result;
            })
            // Handle errors
            .exceptionally(ex -> {
                TradeResult result = new TradeResult();
                result.setSuccess(false);
                result.setMessage("Trade failed: " + ex.getMessage());
                return result;
            });
    }

    /**
     * Combine multiple async operations
     */
    public static java.util.concurrent.CompletableFuture<String> fetchMultipleFruitsData(
            String fruit1, String fruit2) {

        java.util.concurrent.CompletableFuture<String> future1 = fetchFruitDataAsync(fruit1);
        java.util.concurrent.CompletableFuture<String> future2 = fetchFruitDataAsync(fruit2);

        // Combine results when both complete
        return future1.thenCombine(future2, (data1, data2) ->
            data1 + " | " + data2
        );
    }

    /**
     * Wait for all futures to complete
     */
    public static java.util.concurrent.CompletableFuture<Void> processAllTrades(
            List<String> fruitNames) {

        java.util.concurrent.CompletableFuture<?>[] futures = fruitNames.stream()
            .map(CompletableFutureExamples::fetchFruitDataAsync)
            .toArray(java.util.concurrent.CompletableFuture[]::new);

        return java.util.concurrent.CompletableFuture.allOf(futures);
    }
}

/**
 * Producer-Consumer Pattern using BlockingQueue
 * Common pattern in enterprise applications for task processing
 */
class ProducerConsumerExample {
    private final java.util.concurrent.BlockingQueue<TradeRequest> queue;
    private final int numConsumers;
    private volatile boolean running = true;

    public ProducerConsumerExample(int queueSize, int numConsumers) {
        this.queue = new java.util.concurrent.ArrayBlockingQueue<>(queueSize);
        this.numConsumers = numConsumers;
    }

    /**
     * Producer: Add trades to queue
     */
    class Producer implements Runnable {
        @Override
        public void run() {
            try {
                for (int i = 0; i < 10; i++) {
                    TradeRequest request = new TradeRequest(
                        "user" + i,
                        "Fruit" + i,
                        1000.0 * (i + 1)
                    );
                    queue.put(request); // Blocks if queue is full
                    System.out.println("Produced: " + request.fruitName);
                    Thread.sleep(100);
                }
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        }
    }

    /**
     * Consumer: Process trades from queue
     */
    class Consumer implements Runnable {
        private final int id;

        public Consumer(int id) {
            this.id = id;
        }

        @Override
        public void run() {
            try {
                while (running) {
                    TradeRequest request = queue.poll(1, java.util.concurrent.TimeUnit.SECONDS);
                    if (request != null) {
                        System.out.println("Consumer " + id + " processing: " + request.fruitName);
                        Thread.sleep(500); // Simulate processing
                    }
                }
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        }
    }

    /**
     * Start the producer-consumer system
     */
    public void start() {
        // Start producer
        Thread producer = new Thread(new Producer());
        producer.start();

        // Start consumers
        for (int i = 0; i < numConsumers; i++) {
            Thread consumer = new Thread(new Consumer(i));
            consumer.start();
        }
    }

    public void stop() {
        running = false;
    }
}

/**
 * Thread Synchronization Example
 * Shows how to prevent race conditions
 */
class BankAccount {
    private double balance;
    private final Object lock = new Object();

    public BankAccount(double initialBalance) {
        this.balance = initialBalance;
    }

    /**
     * Synchronized method - only one thread can execute at a time
     */
    public synchronized void deposit(double amount) {
        double newBalance = balance + amount;
        // Simulate processing time
        try {
            Thread.sleep(10);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
        balance = newBalance;
        System.out.println(Thread.currentThread().getName() +
            " deposited " + amount + ", new balance: " + balance);
    }

    /**
     * Synchronized block - more fine-grained control
     */
    public void withdraw(double amount) {
        synchronized (lock) {
            if (balance >= amount) {
                balance -= amount;
                System.out.println(Thread.currentThread().getName() +
                    " withdrew " + amount + ", new balance: " + balance);
            } else {
                System.out.println(Thread.currentThread().getName() +
                    " insufficient funds");
            }
        }
    }

    public synchronized double getBalance() {
        return balance;
    }
}

/**
 * MULTITHREADING DEMO
 */
class MultithreadingDemo {
    public static void runDemo() {
        System.out.println("\n" + "=".repeat(80));
        System.out.println("TOPIC 4: MULTITHREADING AND CONCURRENCY DEMO");
        System.out.println("=".repeat(80));

        // Demo 1: Thread-Safe Order Book
        System.out.println("\n--- Demo 1: Concurrent Order Placement ---");
        OrderBook orderBook = new OrderBook();

        // Create multiple threads placing orders
        Thread t1 = new Thread(() -> {
            for (int i = 0; i < 3; i++) {
                orderBook.placeOrder("luffy", "Gomu Gomu no Mi", 1000000, 1);
            }
        }, "Thread-1");

        Thread t2 = new Thread(() -> {
            for (int i = 0; i < 3; i++) {
                orderBook.placeOrder("zoro", "Hito Hito no Mi", 500000, 1);
            }
        }, "Thread-2");

        t1.start();
        t2.start();

        try {
            t1.join();
            t2.join();
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }

        System.out.println("Total orders: " + orderBook.getOrderCount());

        // Demo 2: ExecutorService with Future
        System.out.println("\n--- Demo 2: Async Trade Processing ---");
        AsyncTradeProcessor processor = new AsyncTradeProcessor(3);

        try {
            java.util.concurrent.Future<TradeResult> future =
                processor.processTradeAsync("luffy", "Gomu Gomu no Mi", 1000000);

            System.out.println("Trade submitted, doing other work...");

            // Get result (blocks until complete)
            TradeResult result = future.get(5, java.util.concurrent.TimeUnit.SECONDS);
            System.out.println("Trade result: " + result.getMessage());

        } catch (Exception e) {
            System.err.println("Error: " + e.getMessage());
        } finally {
            processor.shutdown();
        }

        // Demo 3: CompletableFuture
        System.out.println("\n--- Demo 3: CompletableFuture Chaining ---");
        java.util.concurrent.CompletableFuture<TradeResult> futureResult =
            CompletableFutureExamples.processTradeWithValidation(
                "luffy", "Gomu Gomu no Mi", 1000000);

        futureResult.thenAccept(result ->
            System.out.println("Async result: " + result.getMessage())
        ).join(); // Wait for completion

        // Demo 4: Combining Futures
        System.out.println("\n--- Demo 4: Combining Multiple Async Operations ---");
        java.util.concurrent.CompletableFuture<String> combined =
            CompletableFutureExamples.fetchMultipleFruitsData(
                "Gomu Gomu no Mi", "Mera Mera no Mi");

        combined.thenAccept(data ->
            System.out.println("Combined data: " + data)
        ).join();

        // Demo 5: Synchronized Access
        System.out.println("\n--- Demo 5: Thread Synchronization ---");
        BankAccount account = new BankAccount(1000);

        Thread depositor = new Thread(() -> {
            for (int i = 0; i < 3; i++) {
                account.deposit(100);
            }
        }, "Depositor");

        Thread withdrawer = new Thread(() -> {
            for (int i = 0; i < 3; i++) {
                account.withdraw(50);
            }
        }, "Withdrawer");

        depositor.start();
        withdrawer.start();

        try {
            depositor.join();
            withdrawer.join();
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }

        System.out.println("Final balance: " + account.getBalance());

        System.out.println("\n" + "=".repeat(80));
        System.out.println("KEY TAKEAWAYS:");
        System.out.println("1. Use ExecutorService for thread pool management");
        System.out.println("2. CompletableFuture enables modern async programming");
        System.out.println("3. ConcurrentHashMap provides thread-safe collections");
        System.out.println("4. Synchronized blocks prevent race conditions");
        System.out.println("5. BlockingQueue enables producer-consumer pattern");
        System.out.println("6. Always shutdown ExecutorService properly");
        System.out.println("7. Atomic classes provide lock-free thread safety");
        System.out.println("=".repeat(80));
    }
}

/*
================================================================================
TOPIC 5: FILE I/O AND SERIALIZATION
================================================================================

File I/O allows reading from and writing to files. Serialization converts
objects to bytes for storage or transmission.

WHY FILE I/O MATTERS IN ENTERPRISE:
1. Data Persistence: Save application state
2. Configuration: Read config files
3. Logging: Write application logs
4. Data Export/Import: CSV, JSON, XML files
5. Batch Processing: Process large files
6. Backup/Restore: Save and restore data

FILE I/O CLASSES:
- File/Path: Represent file paths
- FileInputStream/FileOutputStream: Byte streams
- FileReader/FileWriter: Character streams
- BufferedReader/BufferedWriter: Buffered I/O (faster)
- Files (java.nio.file): Modern file operations

SERIALIZATION:
- Serializable interface: Mark class as serializable
- ObjectOutputStream: Write objects to stream
- ObjectInputStream: Read objects from stream
- transient keyword: Skip field during serialization
- serialVersionUID: Version control for serialized classes

MODERN ALTERNATIVES:
- JSON: Jackson, Gson libraries
- XML: JAXB
- Protocol Buffers: Google's binary format
- Apache Avro: Hadoop ecosystem

BEST PRACTICES:
1. Use try-with-resources for automatic resource cleanup
2. Use BufferedReader/Writer for better performance
3. Use java.nio.file.Files for modern file operations
4. Prefer JSON over Java serialization for flexibility
5. Always handle IOException
6. Use Path instead of File (modern API)
================================================================================
*/

/**
 * Serializable Devil Fruit for persistence
 */
class SerializableDevilFruit implements java.io.Serializable {
    private static final long serialVersionUID = 1L;

    private String name;
    private String type;
    private double price;
    private transient String tempData; // Not serialized

    public SerializableDevilFruit(String name, String type, double price) {
        this.name = name;
        this.type = type;
        this.price = price;
        this.tempData = "temporary";
    }

    // Getters and setters
    public String getName() { return name; }
    public String getType() { return type; }
    public double getPrice() { return price; }

    @Override
    public String toString() {
        return String.format("%s (%s): %.0f Berry", name, type, price);
    }
}

/**
 * File-based Repository for Devil Fruits
 * Demonstrates various file I/O operations
 */
class FileBasedFruitRepository {
    private final String dataDirectory;

    public FileBasedFruitRepository(String dataDirectory) {
        this.dataDirectory = dataDirectory;
        createDirectoryIfNotExists();
    }

    /**
     * Create directory if it doesn't exist
     */
    private void createDirectoryIfNotExists() {
        try {
            java.nio.file.Path path = java.nio.file.Paths.get(dataDirectory);
            if (!java.nio.file.Files.exists(path)) {
                java.nio.file.Files.createDirectories(path);
            }
        } catch (java.io.IOException e) {
            System.err.println("Failed to create directory: " + e.getMessage());
        }
    }

    /**
     * Save fruit to CSV file
     */
    public void saveToCsv(List<SerializableDevilFruit> fruits, String filename) {
        String filepath = dataDirectory + "/" + filename;

        try (java.io.BufferedWriter writer = new java.io.BufferedWriter(
                new java.io.FileWriter(filepath))) {

            // Write header
            writer.write("Name,Type,Price");
            writer.newLine();

            // Write data
            for (SerializableDevilFruit fruit : fruits) {
                writer.write(String.format("%s,%s,%.2f",
                    fruit.getName(), fruit.getType(), fruit.getPrice()));
                writer.newLine();
            }

            System.out.println("Saved " + fruits.size() + " fruits to " + filename);

        } catch (java.io.IOException e) {
            System.err.println("Error saving to CSV: " + e.getMessage());
        }
    }

    /**
     * Load fruits from CSV file
     */
    public List<SerializableDevilFruit> loadFromCsv(String filename) {
        List<SerializableDevilFruit> fruits = new ArrayList<>();
        String filepath = dataDirectory + "/" + filename;

        try (java.io.BufferedReader reader = new java.io.BufferedReader(
                new java.io.FileReader(filepath))) {

            // Skip header
            reader.readLine();

            String line;
            while ((line = reader.readLine()) != null) {
                String[] parts = line.split(",");
                if (parts.length == 3) {
                    String name = parts[0];
                    String type = parts[1];
                    double price = Double.parseDouble(parts[2]);
                    fruits.add(new SerializableDevilFruit(name, type, price));
                }
            }

            System.out.println("Loaded " + fruits.size() + " fruits from " + filename);

        } catch (java.io.FileNotFoundException e) {
            System.err.println("File not found: " + filename);
        } catch (java.io.IOException e) {
            System.err.println("Error loading from CSV: " + e.getMessage());
        }

        return fruits;
    }

    /**
     * Serialize fruits to binary file
     */
    public void serializeFruits(List<SerializableDevilFruit> fruits, String filename) {
        String filepath = dataDirectory + "/" + filename;

        try (java.io.ObjectOutputStream oos = new java.io.ObjectOutputStream(
                new java.io.FileOutputStream(filepath))) {

            oos.writeObject(fruits);
            System.out.println("Serialized " + fruits.size() + " fruits to " + filename);

        } catch (java.io.IOException e) {
            System.err.println("Error serializing: " + e.getMessage());
        }
    }

    /**
     * Deserialize fruits from binary file
     */
    @SuppressWarnings("unchecked")
    public List<SerializableDevilFruit> deserializeFruits(String filename) {
        String filepath = dataDirectory + "/" + filename;

        try (java.io.ObjectInputStream ois = new java.io.ObjectInputStream(
                new java.io.FileInputStream(filepath))) {

            List<SerializableDevilFruit> fruits =
                (List<SerializableDevilFruit>) ois.readObject();
            System.out.println("Deserialized " + fruits.size() + " fruits from " + filename);
            return fruits;

        } catch (java.io.FileNotFoundException e) {
            System.err.println("File not found: " + filename);
        } catch (java.io.IOException | ClassNotFoundException e) {
            System.err.println("Error deserializing: " + e.getMessage());
        }

        return new ArrayList<>();
    }

    /**
     * Write trade log using modern NIO API
     */
    public void writeTradeLog(String message) {
        String filepath = dataDirectory + "/trade.log";

        try {
            String logEntry = String.format("[%s] %s%n",
                java.time.LocalDateTime.now(), message);

            java.nio.file.Files.write(
                java.nio.file.Paths.get(filepath),
                logEntry.getBytes(),
                java.nio.file.StandardOpenOption.CREATE,
                java.nio.file.StandardOpenOption.APPEND
            );

        } catch (java.io.IOException e) {
            System.err.println("Error writing log: " + e.getMessage());
        }
    }

    /**
     * Read all log entries
     */
    public List<String> readTradeLog() {
        String filepath = dataDirectory + "/trade.log";

        try {
            return java.nio.file.Files.readAllLines(
                java.nio.file.Paths.get(filepath));
        } catch (java.io.IOException e) {
            System.err.println("Error reading log: " + e.getMessage());
            return new ArrayList<>();
        }
    }

    /**
     * List all files in directory
     */
    public void listFiles() {
        try {
            java.nio.file.Files.list(java.nio.file.Paths.get(dataDirectory))
                .forEach(path -> System.out.println("- " + path.getFileName()));
        } catch (java.io.IOException e) {
            System.err.println("Error listing files: " + e.getMessage());
        }
    }

    /**
     * Delete a file
     */
    public boolean deleteFile(String filename) {
        try {
            java.nio.file.Files.deleteIfExists(
                java.nio.file.Paths.get(dataDirectory + "/" + filename));
            return true;
        } catch (java.io.IOException e) {
            System.err.println("Error deleting file: " + e.getMessage());
            return false;
        }
    }
}

/**
 * FILE I/O DEMO
 */
class FileIODemo {
    public static void runDemo() {
        System.out.println("\n" + "=".repeat(80));
        System.out.println("TOPIC 5: FILE I/O AND SERIALIZATION DEMO");
        System.out.println("=".repeat(80));

        FileBasedFruitRepository repo = new FileBasedFruitRepository("./data");

        // Create test data
        List<SerializableDevilFruit> fruits = Arrays.asList(
            new SerializableDevilFruit("Gomu Gomu no Mi", "Paramecia", 1000000),
            new SerializableDevilFruit("Mera Mera no Mi", "Logia", 2000000),
            new SerializableDevilFruit("Ope Ope no Mi", "Paramecia", 5000000)
        );

        // Demo 1: Save to CSV
        System.out.println("\n--- Demo 1: Save to CSV ---");
        repo.saveToCsv(fruits, "fruits.csv");

        // Demo 2: Load from CSV
        System.out.println("\n--- Demo 2: Load from CSV ---");
        List<SerializableDevilFruit> loadedFruits = repo.loadFromCsv("fruits.csv");
        loadedFruits.forEach(fruit -> System.out.println("- " + fruit));

        // Demo 3: Serialize to binary
        System.out.println("\n--- Demo 3: Serialize to Binary ---");
        repo.serializeFruits(fruits, "fruits.dat");

        // Demo 4: Deserialize from binary
        System.out.println("\n--- Demo 4: Deserialize from Binary ---");
        List<SerializableDevilFruit> deserializedFruits = repo.deserializeFruits("fruits.dat");
        deserializedFruits.forEach(fruit -> System.out.println("- " + fruit));

        // Demo 5: Write logs
        System.out.println("\n--- Demo 5: Write Trade Logs ---");
        repo.writeTradeLog("User luffy purchased Gomu Gomu no Mi");
        repo.writeTradeLog("User ace purchased Mera Mera no Mi");
        repo.writeTradeLog("User law purchased Ope Ope no Mi");

        // Demo 6: Read logs
        System.out.println("\n--- Demo 6: Read Trade Logs ---");
        List<String> logs = repo.readTradeLog();
        logs.forEach(System.out::println);

        // Demo 7: List files
        System.out.println("\n--- Demo 7: List Files in Directory ---");
        repo.listFiles();

        System.out.println("\n" + "=".repeat(80));
        System.out.println("KEY TAKEAWAYS:");
        System.out.println("1. Use try-with-resources for automatic resource cleanup");
        System.out.println("2. BufferedReader/Writer improve performance");
        System.out.println("3. java.nio.file.Files provides modern file operations");
        System.out.println("4. Serialization preserves object state");
        System.out.println("5. transient keyword excludes fields from serialization");
        System.out.println("6. CSV is human-readable, binary is more efficient");
        System.out.println("7. Always handle IOException properly");
        System.out.println("=".repeat(80));
    }
}

/*
================================================================================
TOPIC 6: DESIGN PATTERNS
================================================================================

Design patterns are reusable solutions to common software design problems.
They represent best practices evolved over time.

WHY DESIGN PATTERNS MATTER IN ENTERPRISE:
1. Proven Solutions: Battle-tested approaches
2. Common Vocabulary: Team communication
3. Code Quality: Better structure and maintainability
4. Scalability: Patterns support growth
5. Best Practices: Industry standards

COMMON PATTERNS IN ENTERPRISE JAVA:

CREATIONAL PATTERNS (Object Creation):
- Singleton: Single instance of a class
- Factory: Create objects without specifying exact class
- Builder: Construct complex objects step by step
- Prototype: Clone existing objects

STRUCTURAL PATTERNS (Object Composition):
- Adapter: Make incompatible interfaces work together
- Decorator: Add behavior to objects dynamically
- Facade: Simplified interface to complex subsystem
- Proxy: Control access to objects

BEHAVIORAL PATTERNS (Object Interaction):
- Strategy: Encapsulate algorithms
- Observer: Notify dependents of state changes
- Command: Encapsulate requests as objects
- Template Method: Define algorithm skeleton

ENTERPRISE PATTERNS:
- Repository: Data access abstraction
- Service Layer: Business logic layer
- DTO (Data Transfer Object): Transfer data between layers
- Dependency Injection: Inversion of control

BEST PRACTICES:
1. Don't overuse patterns - use when appropriate
2. Understand the problem before applying a pattern
3. Patterns should simplify, not complicate
4. Combine patterns when needed
5. Keep SOLID principles in mind
================================================================================
*/

/**
 * PATTERN 1: SINGLETON
 * Ensures only one instance of a class exists
 * Used for: Configuration, Logging, Database connections
 */
class TradingPlatformConfig {
    // Thread-safe singleton using enum (best practice)
    private static class Holder {
        private static final TradingPlatformConfig INSTANCE = new TradingPlatformConfig();
    }

    private String platformName;
    private String apiEndpoint;
    private int maxConcurrentTrades;

    private TradingPlatformConfig() {
        // Private constructor prevents instantiation
        this.platformName = "One Piece Trading Platform";
        this.apiEndpoint = "https://api.onepiece-trading.com";
        this.maxConcurrentTrades = 100;
    }

    public static TradingPlatformConfig getInstance() {
        return Holder.INSTANCE;
    }

    // Getters
    public String getPlatformName() { return platformName; }
    public String getApiEndpoint() { return apiEndpoint; }
    public int getMaxConcurrentTrades() { return maxConcurrentTrades; }

    // Setters
    public void setPlatformName(String platformName) { this.platformName = platformName; }
    public void setApiEndpoint(String apiEndpoint) { this.apiEndpoint = apiEndpoint; }
    public void setMaxConcurrentTrades(int max) { this.maxConcurrentTrades = max; }
}

/**
 * PATTERN 2: FACTORY
 * Creates objects without specifying exact class
 * Used for: Creating different types of objects based on input
 */
interface PaymentMethod {
    boolean processPayment(double amount);
    String getPaymentType();
}

class BerryPayment implements PaymentMethod {
    @Override
    public boolean processPayment(double amount) {
        System.out.println("Processing Berry payment: " + amount);
        return true;
    }

    @Override
    public String getPaymentType() {
        return "Berry";
    }
}

class TreasurePayment implements PaymentMethod {
    @Override
    public boolean processPayment(double amount) {
        System.out.println("Processing Treasure payment: " + amount);
        return true;
    }

    @Override
    public String getPaymentType() {
        return "Treasure";
    }
}

class CreditPayment implements PaymentMethod {
    @Override
    public boolean processPayment(double amount) {
        System.out.println("Processing Credit payment: " + amount);
        return true;
    }

    @Override
    public String getPaymentType() {
        return "Credit";
    }
}

class PaymentFactory {
    public static PaymentMethod createPayment(String type) {
        switch (type.toLowerCase()) {
            case "berry":
                return new BerryPayment();
            case "treasure":
                return new TreasurePayment();
            case "credit":
                return new CreditPayment();
            default:
                throw new IllegalArgumentException("Unknown payment type: " + type);
        }
    }
}

/**
 * PATTERN 3: BUILDER
 * Construct complex objects step by step
 * Used for: Objects with many optional parameters
 */
class TradingOrder {
    // Required parameters
    private final String orderId;
    private final String userId;
    private final String fruitName;

    // Optional parameters
    private final double price;
    private final int quantity;
    private final String orderType;
    private final boolean isUrgent;
    private final String notes;

    private TradingOrder(Builder builder) {
        this.orderId = builder.orderId;
        this.userId = builder.userId;
        this.fruitName = builder.fruitName;
        this.price = builder.price;
        this.quantity = builder.quantity;
        this.orderType = builder.orderType;
        this.isUrgent = builder.isUrgent;
        this.notes = builder.notes;
    }

    public static class Builder {
        // Required parameters
        private final String orderId;
        private final String userId;
        private final String fruitName;

        // Optional parameters with defaults
        private double price = 0;
        private int quantity = 1;
        private String orderType = "BUY";
        private boolean isUrgent = false;
        private String notes = "";

        public Builder(String orderId, String userId, String fruitName) {
            this.orderId = orderId;
            this.userId = userId;
            this.fruitName = fruitName;
        }

        public Builder price(double price) {
            this.price = price;
            return this;
        }

        public Builder quantity(int quantity) {
            this.quantity = quantity;
            return this;
        }

        public Builder orderType(String orderType) {
            this.orderType = orderType;
            return this;
        }

        public Builder urgent(boolean isUrgent) {
            this.isUrgent = isUrgent;
            return this;
        }

        public Builder notes(String notes) {
            this.notes = notes;
            return this;
        }

        public TradingOrder build() {
            return new TradingOrder(this);
        }
    }

    @Override
    public String toString() {
        return String.format("Order[%s]: %s buying %s x%d @ %.0f Berry %s",
            orderId, userId, fruitName, quantity, price, isUrgent ? "(URGENT)" : "");
    }
}

/**
 * PATTERN 4: STRATEGY
 * Encapsulate algorithms and make them interchangeable
 * Used for: Different ways to perform the same task
 */
interface PricingStrategy {
    double calculatePrice(DevilFruit fruit);
}

class StandardPricing implements PricingStrategy {
    @Override
    public double calculatePrice(DevilFruit fruit) {
        return fruit.getPrice();
    }
}

class DiscountPricing implements PricingStrategy {
    private final double discountPercent;

    public DiscountPricing(double discountPercent) {
        this.discountPercent = discountPercent;
    }

    @Override
    public double calculatePrice(DevilFruit fruit) {
        return fruit.getPrice() * (1 - discountPercent / 100);
    }
}

class PremiumPricing implements PricingStrategy {
    @Override
    public double calculatePrice(DevilFruit fruit) {
        // Logia fruits get 50% premium
        if ("Logia".equals(fruit.getType())) {
            return fruit.getPrice() * 1.5;
        }
        return fruit.getPrice();
    }
}

class PriceCalculatorService {
    private PricingStrategy strategy;

    public PriceCalculatorService(PricingStrategy strategy) {
        this.strategy = strategy;
    }

    public void setStrategy(PricingStrategy strategy) {
        this.strategy = strategy;
    }

    public double calculatePrice(DevilFruit fruit) {
        return strategy.calculatePrice(fruit);
    }
}

/**
 * PATTERN 5: OBSERVER
 * Notify dependents when state changes
 * Used for: Event handling, notifications
 */
interface TradeObserver {
    void onTradeCompleted(TradeEvent event);
}

class TradeEvent {
    private final String tradeId;
    private final String userId;
    private final String fruitName;
    private final double amount;

    public TradeEvent(String tradeId, String userId, String fruitName, double amount) {
        this.tradeId = tradeId;
        this.userId = userId;
        this.fruitName = fruitName;
        this.amount = amount;
    }

    public String getTradeId() { return tradeId; }
    public String getUserId() { return userId; }
    public String getFruitName() { return fruitName; }
    public double getAmount() { return amount; }
}

class EmailNotificationObserver implements TradeObserver {
    @Override
    public void onTradeCompleted(TradeEvent event) {
        System.out.println("📧 Email sent to " + event.getUserId() +
            ": Trade " + event.getTradeId() + " completed");
    }
}

class SMSNotificationObserver implements TradeObserver {
    @Override
    public void onTradeCompleted(TradeEvent event) {
        System.out.println("📱 SMS sent to " + event.getUserId() +
            ": You purchased " + event.getFruitName());
    }
}

class AuditLogObserver implements TradeObserver {
    @Override
    public void onTradeCompleted(TradeEvent event) {
        System.out.println("📝 Audit log: Trade " + event.getTradeId() +
            " - Amount: " + event.getAmount());
    }
}

class ObservableTradeService {
    private final List<TradeObserver> observers = new ArrayList<>();

    public void addObserver(TradeObserver observer) {
        observers.add(observer);
    }

    public void removeObserver(TradeObserver observer) {
        observers.remove(observer);
    }

    public void executeTrade(String tradeId, String userId, String fruitName, double amount) {
        // Execute trade logic
        System.out.println("Executing trade: " + tradeId);

        // Notify all observers
        TradeEvent event = new TradeEvent(tradeId, userId, fruitName, amount);
        notifyObservers(event);
    }

    private void notifyObservers(TradeEvent event) {
        for (TradeObserver observer : observers) {
            observer.onTradeCompleted(event);
        }
    }
}

/**
 * PATTERN 6: DECORATOR
 * Add behavior to objects dynamically
 * Used for: Adding features without modifying original class
 */
interface FruitListing {
    String getDescription();
    double getPrice();
}

class BasicFruitListing implements FruitListing {
    private final DevilFruit fruit;

    public BasicFruitListing(DevilFruit fruit) {
        this.fruit = fruit;
    }

    @Override
    public String getDescription() {
        return fruit.getName();
    }

    @Override
    public double getPrice() {
        return fruit.getPrice();
    }
}

abstract class FruitListingDecorator implements FruitListing {
    protected final FruitListing wrappedListing;

    public FruitListingDecorator(FruitListing listing) {
        this.wrappedListing = listing;
    }
}

class FeaturedDecorator extends FruitListingDecorator {
    public FeaturedDecorator(FruitListing listing) {
        super(listing);
    }

    @Override
    public String getDescription() {
        return "⭐ FEATURED: " + wrappedListing.getDescription();
    }

    @Override
    public double getPrice() {
        return wrappedListing.getPrice() * 1.1; // 10% premium
    }
}

class InsuredDecorator extends FruitListingDecorator {
    public InsuredDecorator(FruitListing listing) {
        super(listing);
    }

    @Override
    public String getDescription() {
        return wrappedListing.getDescription() + " [INSURED]";
    }

    @Override
    public double getPrice() {
        return wrappedListing.getPrice() + 50000; // Insurance fee
    }
}

/**
 * PATTERN 7: ADAPTER
 * Make incompatible interfaces work together
 * Used for: Integrating third-party libraries
 */
// Legacy system interface
class LegacyFruitData {
    private String fruitName;
    private String fruitCategory;
    private int priceInGold;

    public LegacyFruitData(String fruitName, String fruitCategory, int priceInGold) {
        this.fruitName = fruitName;
        this.fruitCategory = fruitCategory;
        this.priceInGold = priceInGold;
    }

    public String getFruitName() { return fruitName; }
    public String getFruitCategory() { return fruitCategory; }
    public int getPriceInGold() { return priceInGold; }
}

// Adapter to convert legacy data to modern format
class FruitDataAdapter extends DevilFruit {
    private static final double GOLD_TO_BERRY_RATE = 10000;

    public FruitDataAdapter(LegacyFruitData legacyData) {
        super(
            legacyData.getFruitName(),
            legacyData.getFruitCategory(),
            legacyData.getPriceInGold() * GOLD_TO_BERRY_RATE
        );
    }
}

/**
 * PATTERN 8: TEMPLATE METHOD
 * Define algorithm skeleton, let subclasses override steps
 * Used for: Common workflow with customizable steps
 */
abstract class TradeProcessor {
    // Template method - defines the algorithm structure
    public final TradeResult processTrade(String userId, String fruitName, double price) {
        TradeResult result = new TradeResult();

        try {
            // Step 1: Validate (can be overridden)
            if (!validateTrade(userId, fruitName, price)) {
                result.setSuccess(false);
                result.setMessage("Validation failed");
                return result;
            }

            // Step 2: Pre-process (can be overridden)
            preProcess(userId, fruitName);

            // Step 3: Execute (must be implemented)
            executeTrade(userId, fruitName, price);

            // Step 4: Post-process (can be overridden)
            postProcess(userId, fruitName);

            result.setSuccess(true);
            result.setMessage("Trade completed");

        } catch (Exception e) {
            result.setSuccess(false);
            result.setMessage("Error: " + e.getMessage());
        }

        return result;
    }

    // Hook methods - can be overridden
    protected boolean validateTrade(String userId, String fruitName, double price) {
        return true; // Default implementation
    }

    protected void preProcess(String userId, String fruitName) {
        // Default: do nothing
    }

    protected void postProcess(String userId, String fruitName) {
        // Default: do nothing
    }

    // Abstract method - must be implemented
    protected abstract void executeTrade(String userId, String fruitName, double price);
}

class StandardTradeProcessor extends TradeProcessor {
    @Override
    protected void executeTrade(String userId, String fruitName, double price) {
        System.out.println("Executing standard trade for " + userId);
    }

    @Override
    protected void postProcess(String userId, String fruitName) {
        System.out.println("Sending confirmation email to " + userId);
    }
}

class PremiumTradeProcessor extends TradeProcessor {
    @Override
    protected boolean validateTrade(String userId, String fruitName, double price) {
        System.out.println("Premium validation for " + userId);
        return true;
    }

    @Override
    protected void preProcess(String userId, String fruitName) {
        System.out.println("Applying premium benefits for " + userId);
    }

    @Override
    protected void executeTrade(String userId, String fruitName, double price) {
        System.out.println("Executing premium trade with priority for " + userId);
    }

    @Override
    protected void postProcess(String userId, String fruitName) {
        System.out.println("Sending premium confirmation and gift to " + userId);
    }
}

/**
 * DESIGN PATTERNS DEMO
 */
class DesignPatternsDemo {
    public static void runDemo() {
        System.out.println("\n" + "=".repeat(80));
        System.out.println("TOPIC 6: DESIGN PATTERNS DEMO");
        System.out.println("=".repeat(80));

        // Demo 1: Singleton
        System.out.println("\n--- Demo 1: Singleton Pattern ---");
        TradingPlatformConfig config = TradingPlatformConfig.getInstance();
        System.out.println("Platform: " + config.getPlatformName());
        System.out.println("API: " + config.getApiEndpoint());

        // Demo 2: Factory
        System.out.println("\n--- Demo 2: Factory Pattern ---");
        PaymentMethod berryPayment = PaymentFactory.createPayment("berry");
        PaymentMethod creditPayment = PaymentFactory.createPayment("credit");
        berryPayment.processPayment(1000000);
        creditPayment.processPayment(500000);

        // Demo 3: Builder
        System.out.println("\n--- Demo 3: Builder Pattern ---");
        TradingOrder order = new TradingOrder.Builder("ORD-001", "luffy", "Gomu Gomu no Mi")
            .price(1000000)
            .quantity(1)
            .urgent(true)
            .notes("First purchase!")
            .build();
        System.out.println(order);

        // Demo 4: Strategy
        System.out.println("\n--- Demo 4: Strategy Pattern ---");
        DevilFruit fruit = new DevilFruit("Mera Mera no Mi", "Logia", 2000000);

        PriceCalculatorService calculator = new PriceCalculatorService(new StandardPricing());
        System.out.println("Standard price: " + calculator.calculatePrice(fruit));

        calculator.setStrategy(new DiscountPricing(20));
        System.out.println("Discounted price: " + calculator.calculatePrice(fruit));

        calculator.setStrategy(new PremiumPricing());
        System.out.println("Premium price: " + calculator.calculatePrice(fruit));

        // Demo 5: Observer
        System.out.println("\n--- Demo 5: Observer Pattern ---");
        ObservableTradeService tradeService = new ObservableTradeService();
        tradeService.addObserver(new EmailNotificationObserver());
        tradeService.addObserver(new SMSNotificationObserver());
        tradeService.addObserver(new AuditLogObserver());

        tradeService.executeTrade("T-001", "luffy", "Gomu Gomu no Mi", 1000000);

        // Demo 6: Decorator
        System.out.println("\n--- Demo 6: Decorator Pattern ---");
        FruitListing basicListing = new BasicFruitListing(fruit);
        System.out.println(basicListing.getDescription() + ": " + basicListing.getPrice());

        FruitListing featuredListing = new FeaturedDecorator(basicListing);
        System.out.println(featuredListing.getDescription() + ": " + featuredListing.getPrice());

        FruitListing featuredInsured = new InsuredDecorator(featuredListing);
        System.out.println(featuredInsured.getDescription() + ": " + featuredInsured.getPrice());

        // Demo 7: Adapter
        System.out.println("\n--- Demo 7: Adapter Pattern ---");
        LegacyFruitData legacyData = new LegacyFruitData("Ope Ope no Mi", "Paramecia", 500);
        DevilFruit adaptedFruit = new FruitDataAdapter(legacyData);
        System.out.println("Adapted: " + adaptedFruit.getName() + " - " + adaptedFruit.getPrice() + " Berry");

        // Demo 8: Template Method
        System.out.println("\n--- Demo 8: Template Method Pattern ---");
        TradeProcessor standardProcessor = new StandardTradeProcessor();
        standardProcessor.processTrade("zoro", "Hito Hito no Mi", 500000);

        System.out.println();
        TradeProcessor premiumProcessor = new PremiumTradeProcessor();
        premiumProcessor.processTrade("nami", "Goro Goro no Mi", 3000000);

        System.out.println("\n" + "=".repeat(80));
        System.out.println("KEY TAKEAWAYS:");
        System.out.println("1. Singleton ensures single instance (config, connections)");
        System.out.println("2. Factory creates objects without specifying exact class");
        System.out.println("3. Builder constructs complex objects step by step");
        System.out.println("4. Strategy makes algorithms interchangeable");
        System.out.println("5. Observer enables event-driven architecture");
        System.out.println("6. Decorator adds behavior without modifying original");
        System.out.println("7. Adapter makes incompatible interfaces work together");
        System.out.println("8. Template Method defines algorithm skeleton");
        System.out.println("=".repeat(80));
    }
}

/*
================================================================================
TOPIC 7: SPRING FRAMEWORK - COMPLETE EDUCATIONAL GUIDE
================================================================================

╔══════════════════════════════════════════════════════════════════════════╗
║                    WHAT IS SPRING BOOT?                                  ║
╚══════════════════════════════════════════════════════════════════════════╝

Spring Boot is a framework that makes it easy to create production-ready
applications with minimal configuration. Think of it as a "smart assistant"
that handles all the boring setup work so you can focus on writing business logic.

ANALOGY: Building a House
- Without Spring Boot: You need to buy lumber, nails, tools, hire workers,
  manage everything yourself
- With Spring Boot: You get a construction company that brings everything
  pre-configured, you just tell them what rooms you want

╔══════════════════════════════════════════════════════════════════════════╗
║                    WHY DOES SPRING BOOT EXIST?                           ║
╚══════════════════════════════════════════════════════════════════════════╝

PROBLEMS IT SOLVES:

1. CONFIGURATION HELL
   Before: 100+ lines of XML configuration just to connect to a database
   After: 3 lines in application.properties

2. DEPENDENCY MANAGEMENT
   Before: Manually ensure all library versions are compatible
   After: Spring Boot starters bundle compatible versions

3. BOILERPLATE CODE
   Before: Write tons of code to set up web server, database connections
   After: Spring Boot auto-configures everything

4. TESTING DIFFICULTY
   Before: Hard to test because objects create their own dependencies
   After: Dependency Injection makes testing easy (inject mock objects)

5. PRODUCTION READINESS
   Before: Manually add monitoring, health checks, metrics
   After: Built-in production features

╔══════════════════════════════════════════════════════════════════════════╗
║              HOW SPRING BOOT WORKS - THE MAGIC EXPLAINED                 ║
╚══════════════════════════════════════════════════════════════════════════╝

CORE CONCEPT: INVERSION OF CONTROL (IoC)

Traditional Programming:
    class CarService {
        private Engine engine = new Engine(); // CarService creates Engine
    }
    Problem: CarService is tightly coupled to Engine. Hard to test.

Spring Boot Way:
    class CarService {
        private Engine engine; // Spring will provide Engine

        public CarService(Engine engine) { // Constructor injection
            this.engine = engine;
        }
    }
    Benefit: CarService doesn't create Engine. Spring provides it.
             Easy to test (inject a mock Engine).

WHAT HAPPENS WHEN SPRING BOOT STARTS:

Step 1: COMPONENT SCANNING
   - Spring scans your code for classes with @Component, @Service, @Repository
   - It finds all the "beans" (objects Spring should manage)

Step 2: DEPENDENCY RESOLUTION
   - Spring looks at what each bean needs (constructor parameters)
   - It builds a dependency graph

Step 3: BEAN CREATION
   - Spring creates all beans in the correct order
   - If ServiceA needs RepositoryB, Spring creates RepositoryB first

Step 4: DEPENDENCY INJECTION
   - Spring "injects" dependencies into each bean
   - Your objects are now ready to use

Step 5: APPLICATION READY
   - Web server starts (Tomcat on port 8080 by default)
   - Your REST APIs are now accessible

╔══════════════════════════════════════════════════════════════════════════╗
║                    LAYERED ARCHITECTURE EXPLAINED                        ║
╚══════════════════════════════════════════════════════════════════════════╝

WHY LAYERS? Separation of Concerns - each layer has ONE job.

LAYER 1: CONTROLLER (Presentation Layer)
   Job: Handle HTTP requests/responses
   What it does: Receives requests, calls service, returns response
   What it DOESN'T do: Business logic, database access
   Annotation: @RestController

LAYER 2: SERVICE (Business Logic Layer)
   Job: Implement business rules
   What it does: Validation, calculations, orchestration
   What it DOESN'T do: HTTP handling, direct database access
   Annotation: @Service

LAYER 3: REPOSITORY (Data Access Layer)
   Job: Talk to the database
   What it does: CRUD operations, queries
   What it DOESN'T do: Business logic
   Annotation: @Repository (or extends JpaRepository)

LAYER 4: ENTITY (Data Model Layer)
   Job: Represent database tables
   What it does: Map to database columns
   Annotation: @Entity

FLOW OF A REQUEST:
   Client → Controller → Service → Repository → Database
   Database → Repository → Service → Controller → Client

EXAMPLE: Creating a Devil Fruit
   1. Client sends POST /api/fruits with JSON
   2. Controller receives request, extracts data
   3. Controller calls Service.createFruit()
   4. Service validates business rules (price > 0, name unique)
   5. Service calls Repository.save()
   6. Repository executes SQL INSERT
   7. Database stores the record
   8. Repository returns saved entity
   9. Service converts to DTO
   10. Controller returns JSON response

================================================================================
*/

/*
NOTE: The following Spring Boot code is for demonstration and learning.
To run this code, you would need to:
1. Create a Spring Boot project (using Spring Initializr)
2. Add dependencies in pom.xml or build.gradle
3. Configure application.properties
4. Run as a Spring Boot application

This code shows the structure and patterns used in real enterprise applications.
*/

/**
 * SPRING BOOT APPLICATION STRUCTURE
 *
 * This demonstrates a complete Spring Boot application for the
 * One Piece Trading Platform with cloud database integration.
 */

// ============================================================================
// LAYER 1: ENTITY LAYER (Domain Models)
// ============================================================================

/**
 * ============================================================================
 * JPA ENTITY: DevilFruitEntity
 * ============================================================================
 *
 * WHAT IS THIS?
 * This is a JPA Entity class that represents a database table. Each instance
 * of this class represents one row in the "devil_fruits" table.
 *
 * WHY DO WE NEED IT?
 * - Maps Java objects to database tables (Object-Relational Mapping)
 * - Allows us to work with objects instead of writing SQL
 * - JPA/Hibernate automatically creates the table from this class
 *
 * HOW IT WORKS:
 * 1. JPA scans for @Entity classes when application starts
 * 2. Creates database table based on class structure
 * 3. Each field becomes a column in the table
 * 4. Annotations configure column properties (nullable, unique, etc.)
 *
 * WHEN TO USE:
 * - Every database table needs a corresponding entity class
 * - Use entities for persistent data (data that survives app restarts)
 *
 * COMMON MISTAKES:
 * ❌ Forgetting @Entity annotation → JPA won't recognize it
 * ❌ No default constructor → JPA can't instantiate it
 * ❌ Using primitive types (int) instead of wrapper (Integer) → Can't be null
 * ❌ Forgetting @Id → No primary key defined
 *
 * ============================================================================
 */

// @Entity  ← WHAT: Tells JPA this class maps to a database table
//             WHY: JPA needs to know which classes to persist
//             WHEN: On every class that represents a database table
//             RESULT: JPA creates a table named "devil_fruit_entity" by default

// @Table(name = "devil_fruits")  ← WHAT: Specifies exact table name
//                                   WHY: Class name might not match desired table name
//                                   WHEN: When you want custom table name
//                                   RESULT: Table will be named "devil_fruits"

class DevilFruitEntity {

    // ========================================================================
    // PRIMARY KEY FIELD
    // ========================================================================

    // @Id  ← WHAT: Marks this field as the primary key
    //        WHY: Every table needs a unique identifier
    //        WHEN: On the field that uniquely identifies each row
    //        RESULT: Creates PRIMARY KEY constraint in database

    // @GeneratedValue(strategy = GenerationType.IDENTITY)
    //        ↑ WHAT: Auto-generates ID values
    //          WHY: You don't want to manually assign IDs
    //          HOW: Database auto-increments (1, 2, 3, ...)
    //          WHEN: When you want database to handle ID generation
    //          STRATEGIES:
    //            - IDENTITY: Database auto-increment (PostgreSQL SERIAL, MySQL AUTO_INCREMENT)
    //            - AUTO: JPA chooses best strategy for your database
    //            - SEQUENCE: Uses database sequence (Oracle, PostgreSQL)
    //            - TABLE: Uses separate table to generate IDs (portable but slower)

    private Long id;  // ← WHY Long? Can be null before saving, supports large numbers

    // ========================================================================
    // REGULAR FIELDS (Database Columns)
    // ========================================================================

    // @Column(nullable = false, unique = true)
    //        ↑ WHAT: Configures column properties
    //          WHY: Add database constraints for data integrity
    //          OPTIONS:
    //            - nullable = false → NOT NULL constraint (required field)
    //            - unique = true → UNIQUE constraint (no duplicates)
    //            - length = 100 → VARCHAR(100) for strings
    //            - name = "fruit_name" → Custom column name
    //            - precision = 10, scale = 2 → DECIMAL(10,2) for money
    //          RESULT: SQL → name VARCHAR(255) NOT NULL UNIQUE

    private String name;  // ← Devil Fruit name (e.g., "Gomu Gomu no Mi")

    // @Column(nullable = false)
    //        ↑ This field is required (cannot be null)

    private String type;  // ← Type: "Logia", "Paramecia", or "Zoan"

    // @Column(nullable = false)
    private Double price;  // ← Price in Berries (One Piece currency)

    // @Column(name = "created_at")
    //        ↑ WHAT: Maps to column named "created_at" in database
    //          WHY: Java uses camelCase, databases use snake_case
    //          RESULT: Field "createdAt" → Column "created_at"

    private java.time.LocalDateTime createdAt;  // ← When record was created

    // @Column(name = "updated_at")
    private java.time.LocalDateTime updatedAt;  // ← When record was last updated

    // ========================================================================
    // CONSTRUCTORS
    // ========================================================================

    /**
     * Default Constructor (REQUIRED by JPA)
     *
     * WHY REQUIRED?
     * - JPA uses reflection to create instances
     * - Needs a no-argument constructor to instantiate objects
     * - Called when loading data from database
     *
     * WHAT HAPPENS:
     * 1. JPA executes SQL query
     * 2. For each row, calls new DevilFruitEntity()
     * 3. Sets field values using setters or reflection
     *
     * COMMON MISTAKE:
     * ❌ Only having parameterized constructor → JPA can't instantiate
     * ✅ Always include default constructor
     */
    public DevilFruitEntity() {
        // Initialize timestamps when object is created
        this.createdAt = java.time.LocalDateTime.now();
        this.updatedAt = java.time.LocalDateTime.now();
    }

    /**
     * Parameterized Constructor (for convenience)
     *
     * WHY USEFUL?
     * - Easy to create new entities: new DevilFruitEntity("Gomu Gomu", "Paramecia", 1000000.0)
     * - More readable than calling setters
     *
     * WHEN TO USE:
     * - When creating new entities in your code
     * - Not used by JPA (JPA uses default constructor)
     */
    public DevilFruitEntity(String name, String type, Double price) {
        this();  // ← IMPORTANT: Call default constructor to initialize timestamps
        this.name = name;
        this.type = type;
        this.price = price;
    }

    // ========================================================================
    // GETTERS AND SETTERS
    // ========================================================================

    /**
     * WHY DO WE NEED GETTERS AND SETTERS?
     *
     * 1. ENCAPSULATION: Hide internal representation
     *    - Can change internal implementation without breaking code
     *    - Can add validation in setters
     *
     * 2. JPA REQUIREMENT: JPA uses getters/setters to access fields
     *    - When loading from database, JPA calls setters
     *    - When saving to database, JPA calls getters
     *
     * 3. FRAMEWORKS: Many frameworks expect JavaBean pattern
     *    - JSON serialization (Jackson)
     *    - Validation frameworks
     *    - Spring Data binding
     *
     * ALTERNATIVE: Use Lombok @Data annotation to generate automatically
     *   @Data  ← Generates getters, setters, toString, equals, hashCode
     *   class DevilFruitEntity { ... }
     */

    // ID getter/setter
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    // NOTE: Usually you don't call setId() manually - database sets it

    // Name getter/setter
    public String getName() { return name; }
    public void setName(String name) {
        // BEST PRACTICE: Add validation in setters
        // if (name == null || name.trim().isEmpty()) {
        //     throw new IllegalArgumentException("Name cannot be empty");
        // }
        this.name = name;
    }

    // Type getter/setter
    public String getType() { return type; }
    public void setType(String type) { this.type = type; }

    // Price getter/setter
    public Double getPrice() { return price; }
    public void setPrice(Double price) {
        // BEST PRACTICE: Validate business rules
        // if (price != null && price < 0) {
        //     throw new IllegalArgumentException("Price cannot be negative");
        // }
        this.price = price;
    }

    // Timestamp getters/setters
    public java.time.LocalDateTime getCreatedAt() { return createdAt; }
    public void setCreatedAt(java.time.LocalDateTime createdAt) { this.createdAt = createdAt; }

    public java.time.LocalDateTime getUpdatedAt() { return updatedAt; }
    public void setUpdatedAt(java.time.LocalDateTime updatedAt) { this.updatedAt = updatedAt; }

    // ========================================================================
    // OPTIONAL: LIFECYCLE CALLBACKS
    // ========================================================================

    /**
     * These methods are called automatically by JPA at specific times
     *
     * @PrePersist  ← Called before INSERT (before saving new entity)
     * @PreUpdate   ← Called before UPDATE (before updating existing entity)
     * @PostPersist ← Called after INSERT
     * @PostUpdate  ← Called after UPDATE
     * @PreRemove   ← Called before DELETE
     * @PostRemove  ← Called after DELETE
     * @PostLoad    ← Called after loading from database
     */

    // @PrePersist  ← Uncomment in real Spring Boot app
    protected void onCreate() {
        // WHAT: Automatically set createdAt when saving new entity
        // WHEN: Called right before INSERT statement
        // WHY: Ensures timestamp is always set correctly
        createdAt = java.time.LocalDateTime.now();
        updatedAt = java.time.LocalDateTime.now();
    }

    // @PreUpdate  ← Uncomment in real Spring Boot app
    protected void onUpdate() {
        // WHAT: Automatically update updatedAt when modifying entity
        // WHEN: Called right before UPDATE statement
        // WHY: Track when record was last modified
        updatedAt = java.time.LocalDateTime.now();
    }

    // ========================================================================
    // OPTIONAL: toString, equals, hashCode
    // ========================================================================

    /**
     * toString() - For debugging and logging
     *
     * WHY OVERRIDE?
     * - Default toString() shows memory address (not useful)
     * - Custom toString() shows actual data
     *
     * WHEN TO USE:
     * - Logging: logger.info("Saved fruit: " + fruit);
     * - Debugging: System.out.println(fruit);
     */
    @Override
    public String toString() {
        return "DevilFruitEntity{" +
                "id=" + id +
                ", name='" + name + '\'' +
                ", type='" + type + '\'' +
                ", price=" + price +
                '}';
    }

    /**
     * equals() and hashCode() - For comparing entities
     *
     * WHY OVERRIDE?
     * - Default equals() compares memory addresses
     * - We want to compare by ID (business key)
     *
     * WHEN TO USE:
     * - Checking if two entities are the same
     * - Using entities in HashSet or HashMap
     *
     * BEST PRACTICE:
     * - Compare by ID (primary key)
     * - If ID is null, entities are not equal
     */
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;  // Same object reference
        if (o == null || getClass() != o.getClass()) return false;  // Different class
        DevilFruitEntity that = (DevilFruitEntity) o;
        return id != null && id.equals(that.id);  // Compare by ID
    }

    @Override
    public int hashCode() {
        return getClass().hashCode();  // Use class hashCode (stable across instances)
    }
}

/**
 * User Entity
 */
class UserEntity {
    // @Id
    // @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    // @Column(nullable = false, unique = true)
    private String username;

    // @Column(nullable = false)
    private String email;

    // @Column(nullable = false)
    private Double balance;

    // @OneToMany(mappedBy = "user", cascade = CascadeType.ALL)
    // private List<TradeEntity> trades;

    public UserEntity() {
        this.balance = 0.0;
    }

    public UserEntity(String username, String email, Double balance) {
        this.username = username;
        this.email = email;
        this.balance = balance;
    }

    // Getters and Setters
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }

    public String getUsername() { return username; }
    public void setUsername(String username) { this.username = username; }

    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }

    public Double getBalance() { return balance; }
    public void setBalance(Double balance) { this.balance = balance; }
}

/**
 * Trade Entity
 */
class TradeEntity {
    // @Id
    // @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    // @ManyToOne
    // @JoinColumn(name = "user_id", nullable = false)
    private UserEntity user;

    // @ManyToOne
    // @JoinColumn(name = "fruit_id", nullable = false)
    private DevilFruitEntity fruit;

    private Double amount;
    private String status;
    private java.time.LocalDateTime tradeDate;

    public TradeEntity() {
        this.tradeDate = java.time.LocalDateTime.now();
        this.status = "PENDING";
    }

    // Getters and Setters
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }

    public UserEntity getUser() { return user; }
    public void setUser(UserEntity user) { this.user = user; }

    public DevilFruitEntity getFruit() { return fruit; }
    public void setFruit(DevilFruitEntity fruit) { this.fruit = fruit; }

    public Double getAmount() { return amount; }
    public void setAmount(Double amount) { this.amount = amount; }

    public String getStatus() { return status; }
    public void setStatus(String status) { this.status = status; }

    public java.time.LocalDateTime getTradeDate() { return tradeDate; }
    public void setTradeDate(java.time.LocalDateTime tradeDate) { this.tradeDate = tradeDate; }
}

// ============================================================================
// LAYER 2: REPOSITORY LAYER (Data Access)
// ============================================================================

/**
 * ============================================================================
 * SPRING DATA JPA REPOSITORY - THE MAGIC EXPLAINED
 * ============================================================================
 *
 * WHAT IS A REPOSITORY?
 * An interface that handles all database operations (CRUD: Create, Read, Update, Delete)
 *
 * WHY IS IT JUST AN INTERFACE?
 * Spring Data JPA automatically creates the implementation for you!
 * You write the interface, Spring writes the code.
 *
 * HOW DOES IT WORK?
 * 1. You create an interface extending JpaRepository
 * 2. Spring scans for @Repository or interfaces extending JpaRepository
 * 3. Spring creates a PROXY class implementing your interface
 * 4. The proxy class contains all the database logic
 * 5. Spring registers it as a bean (available for dependency injection)
 *
 * REAL DECLARATION (in actual Spring Boot app):
 *
 * @Repository  ← Optional: Spring auto-detects JpaRepository extensions
 * public interface DevilFruitRepository extends JpaRepository<DevilFruitEntity, Long> {
 *                                                              ↑              ↑
 *                                                         Entity Type    ID Type
 *     // Your custom methods here
 * }
 *
 * WHAT YOU GET FOR FREE:
 * By extending JpaRepository, you automatically get 20+ methods:
 * - save(), saveAll()
 * - findById(), findAll(), findAllById()
 * - deleteById(), delete(), deleteAll()
 * - count(), existsById()
 * - And many more!
 *
 * NO SQL REQUIRED! Spring generates all SQL automatically.
 *
 * ============================================================================
 */

// @Repository  ← WHAT: Marks this as a repository component
//                 WHY: Spring creates implementation and manages it
//                 WHEN: On interfaces that extend JpaRepository
//                 NOTE: Optional if extending JpaRepository (auto-detected)

// In real app: extends JpaRepository<DevilFruitEntity, Long>
//                                     ↑                  ↑
//                                  Entity class      ID type
interface DevilFruitSpringRepository {

    // ========================================================================
    // BUILT-IN CRUD METHODS (Provided by JpaRepository)
    // ========================================================================

    /**
     * save() - Insert or Update
     *
     * WHAT: Saves entity to database
     * HOW IT WORKS:
     *   - If entity.getId() == null → INSERT (new record)
     *   - If entity.getId() != null → UPDATE (existing record)
     *
     * SQL GENERATED:
     *   INSERT: INSERT INTO devil_fruits (name, type, price) VALUES (?, ?, ?)
     *   UPDATE: UPDATE devil_fruits SET name=?, type=?, price=? WHERE id=?
     *
     * WHEN TO USE:
     *   - Creating new records
     *   - Updating existing records
     *
     * EXAMPLE:
     *   DevilFruitEntity fruit = new DevilFruitEntity("Gomu Gomu", "Paramecia", 1000000.0);
     *   fruit = repository.save(fruit);  // Returns saved entity with generated ID
     */
    DevilFruitEntity save(DevilFruitEntity fruit);

    /**
     * findById() - Find by Primary Key
     *
     * WHAT: Retrieves entity by ID
     * HOW IT WORKS: Executes SELECT query with WHERE id = ?
     *
     * SQL GENERATED:
     *   SELECT * FROM devil_fruits WHERE id = ?
     *
     * RETURN TYPE (in real app):
     *   Optional<DevilFruitEntity>  ← May or may not exist
     *
     * WHY Optional?
     *   - ID might not exist in database
     *   - Forces you to handle "not found" case
     *   - Prevents NullPointerException
     *
     * USAGE:
     *   Optional<DevilFruitEntity> optional = repository.findById(1L);
     *   if (optional.isPresent()) {
     *       DevilFruitEntity fruit = optional.get();
     *   } else {
     *       // Handle not found
     *   }
     *
     *   // Or use orElseThrow:
     *   DevilFruitEntity fruit = repository.findById(1L)
     *       .orElseThrow(() -> new NotFoundException("Fruit not found"));
     */
    DevilFruitEntity findById(Long id);

    /**
     * findAll() - Get All Records
     *
     * WHAT: Retrieves all entities from table
     * SQL GENERATED: SELECT * FROM devil_fruits
     *
     * WARNING: Can be slow for large tables!
     * BETTER: Use pagination (findAll(Pageable))
     *
     * WHEN TO USE:
     *   - Small tables (< 1000 records)
     *   - Admin interfaces
     *   - Testing
     */
    List<DevilFruitEntity> findAll();

    /**
     * deleteById() - Delete by Primary Key
     *
     * WHAT: Deletes entity by ID
     * HOW IT WORKS:
     *   1. Checks if entity exists
     *   2. If exists, executes DELETE
     *   3. If not exists, throws EmptyResultDataAccessException
     *
     * SQL GENERATED:
     *   SELECT * FROM devil_fruits WHERE id = ?  (check exists)
     *   DELETE FROM devil_fruits WHERE id = ?
     *
     * ALTERNATIVE: delete(entity) - Deletes by entity object
     */
    void deleteById(Long id);

    /**
     * existsById() - Check if Exists
     *
     * WHAT: Checks if record with ID exists
     * SQL GENERATED: SELECT COUNT(*) FROM devil_fruits WHERE id = ?
     * RETURNS: true if exists, false otherwise
     *
     * WHEN TO USE:
     *   - Before deleting
     *   - Validation
     *   - Conditional logic
     */
    boolean existsById(Long id);

    /**
     * count() - Count All Records
     *
     * WHAT: Returns total number of records
     * SQL GENERATED: SELECT COUNT(*) FROM devil_fruits
     *
     * WHEN TO USE:
     *   - Statistics
     *   - Pagination (total pages)
     *   - Dashboard metrics
     */
    long count();

    // ========================================================================
    // CUSTOM QUERY METHODS - SPRING GENERATES SQL FROM METHOD NAME!
    // ========================================================================

    /**
     * SPRING DATA JPA QUERY DERIVATION
     *
     * HOW IT WORKS:
     * Spring parses the method name and generates SQL automatically!
     *
     * NAMING PATTERN:
     * findBy + PropertyName + Operator + OrderBy + Property + Direction
     *
     * EXAMPLES:
     * - findByName → WHERE name = ?
     * - findByPriceGreaterThan → WHERE price > ?
     * - findByTypeAndPriceLessThan → WHERE type = ? AND price < ?
     * - findByNameContaining → WHERE name LIKE %?%
     * - findByTypeOrderByPriceDesc → WHERE type = ? ORDER BY price DESC
     *
     * SUPPORTED KEYWORDS:
     * - And, Or
     * - LessThan, GreaterThan, Between
     * - Like, Containing, StartingWith, EndingWith
     * - IsNull, IsNotNull
     * - OrderBy...Asc, OrderBy...Desc
     * - Top, First (limit results)
     */

    /**
     * findByType() - Find by Type
     *
     * METHOD NAME BREAKDOWN:
     *   findBy + Type
     *   ↑        ↑
     *   Action   Property name (must match field in entity)
     *
     * SQL GENERATED:
     *   SELECT * FROM devil_fruits WHERE type = ?
     *
     * USAGE:
     *   List<DevilFruitEntity> logiaFruits = repository.findByType("Logia");
     */
    List<DevilFruitEntity> findByType(String type);

    /**
     * findByPriceLessThan() - Find Cheap Fruits
     *
     * METHOD NAME BREAKDOWN:
     *   findBy + Price + LessThan
     *   ↑        ↑       ↑
     *   Action   Field   Comparison operator
     *
     * SQL GENERATED:
     *   SELECT * FROM devil_fruits WHERE price < ?
     *
     * OTHER OPERATORS:
     *   - GreaterThan: price > ?
     *   - LessThanEqual: price <= ?
     *   - GreaterThanEqual: price >= ?
     */
    List<DevilFruitEntity> findByPriceLessThan(Double price);

    /**
     * findByPriceBetween() - Find in Price Range
     *
     * METHOD NAME BREAKDOWN:
     *   findBy + Price + Between
     *
     * SQL GENERATED:
     *   SELECT * FROM devil_fruits WHERE price BETWEEN ? AND ?
     *
     * USAGE:
     *   List<DevilFruitEntity> midRange = repository.findByPriceBetween(100000.0, 500000.0);
     */
    List<DevilFruitEntity> findByPriceBetween(Double minPrice, Double maxPrice);

    /**
     * findByNameContaining() - Search by Keyword
     *
     * METHOD NAME BREAKDOWN:
     *   findBy + Name + Containing
     *
     * SQL GENERATED:
     *   SELECT * FROM devil_fruits WHERE name LIKE %?%
     *
     * SIMILAR METHODS:
     *   - StartingWith: name LIKE ?%
     *   - EndingWith: name LIKE %?
     *   - Like: name LIKE ? (you provide wildcards)
     *
     * USAGE:
     *   List<DevilFruitEntity> results = repository.findByNameContaining("Gomu");
     *   // Finds "Gomu Gomu no Mi", "Gomu Gomu", etc.
     */
    List<DevilFruitEntity> findByNameContaining(String keyword);

    /**
     * findByTypeOrderByPriceDesc() - Find and Sort
     *
     * METHOD NAME BREAKDOWN:
     *   findBy + Type + OrderBy + Price + Desc
     *   ↑        ↑      ↑         ↑       ↑
     *   Action   Filter Sort      Field   Direction
     *
     * SQL GENERATED:
     *   SELECT * FROM devil_fruits WHERE type = ? ORDER BY price DESC
     *
     * USAGE:
     *   List<DevilFruitEntity> expensive = repository.findByTypeOrderByPriceDesc("Logia");
     *   // Returns Logia fruits from most to least expensive
     */
    List<DevilFruitEntity> findByTypeOrderByPriceDesc(String type);

    // ========================================================================
    // CUSTOM QUERIES WITH @Query ANNOTATION
    // ========================================================================

    /**
     * WHEN TO USE @Query:
     * - Complex queries that can't be expressed in method name
     * - Joins across multiple tables
     * - Aggregations (SUM, AVG, COUNT)
     * - Performance optimization
     *
     * TWO TYPES:
     * 1. JPQL (Java Persistence Query Language) - Uses entity names
     * 2. Native SQL - Uses actual table/column names
     */

    /**
     * findExpensiveFruitsByType() - Custom JPQL Query
     *
     * @Query("SELECT f FROM DevilFruitEntity f WHERE f.type = :type AND f.price > :minPrice")
     *        ↑                                                  ↑                    ↑
     *        JPQL syntax                                   Named param         Named param
     *
     * JPQL vs SQL:
     *   JPQL: SELECT f FROM DevilFruitEntity f WHERE f.type = :type
     *   SQL:  SELECT * FROM devil_fruits WHERE type = ?
     *
     * JPQL uses:
     *   - Entity class names (DevilFruitEntity)
     *   - Field names (type, price)
     *   - Named parameters (:type, :minPrice)
     *
     * WHY JPQL?
     *   - Database independent
     *   - Type safe
     *   - Works with entity relationships
     *
     * USAGE:
     *   List<DevilFruitEntity> fruits = repository.findExpensiveFruitsByType("Logia", 500000.0);
     */
    // @Query("SELECT f FROM DevilFruitEntity f WHERE f.type = :type AND f.price > :minPrice")
    List<DevilFruitEntity> findExpensiveFruitsByType(String type, Double minPrice);

    /**
     * findExpensiveFruitsNative() - Native SQL Query
     *
     * @Query(value = "SELECT * FROM devil_fruits WHERE price > ?1", nativeQuery = true)
     *        ↑                                                 ↑     ↑
     *        Native SQL                                   Positional  Enable native SQL
     *                                                     param (1-indexed)
     *
     * WHEN TO USE NATIVE SQL:
     *   - Database-specific features (PostgreSQL arrays, JSON)
     *   - Complex queries that JPQL can't handle
     *   - Performance optimization with database-specific syntax
     *
     * DRAWBACK:
     *   - Not database independent
     *   - If you switch from PostgreSQL to MySQL, might need changes
     *
     * PARAMETER STYLES:
     *   - Positional: ?1, ?2, ?3 (1-indexed)
     *   - Named: :paramName (requires @Param annotation)
     */
    // @Query(value = "SELECT * FROM devil_fruits WHERE price > ?1", nativeQuery = true)
    List<DevilFruitEntity> findExpensiveFruitsNative(Double minPrice);

    // ========================================================================
    // ADVANCED: PAGINATION AND SORTING
    // ========================================================================

    /**
     * WHY PAGINATION?
     * - Loading 1 million records crashes your app
     * - Users don't need all data at once
     * - Improves performance and user experience
     *
     * HOW TO USE (in real Spring Boot app):
     *
     * // In Repository:
     * Page<DevilFruitEntity> findByType(String type, Pageable pageable);
     *
     * // In Service:
     * Pageable pageable = PageRequest.of(0, 20);  // Page 0, size 20
     * Page<DevilFruitEntity> page = repository.findByType("Logia", pageable);
     *
     * // Get data:
     * List<DevilFruitEntity> fruits = page.getContent();  // Current page items
     * int totalPages = page.getTotalPages();              // Total pages
     * long totalElements = page.getTotalElements();       // Total items
     * boolean hasNext = page.hasNext();                   // More pages?
     *
     * // With sorting:
     * Pageable pageable = PageRequest.of(0, 20, Sort.by("price").descending());
     */
}

/**
 * User Repository
 */
interface UserSpringRepository {
    UserEntity save(UserEntity user);
    UserEntity findById(Long id);
    UserEntity findByUsername(String username);
    UserEntity findByEmail(String email);
    List<UserEntity> findAll();
    boolean existsByUsername(String username);
    boolean existsByEmail(String email);
}

// ============================================================================
// LAYER 3: DTO LAYER (Data Transfer Objects)
// ============================================================================

/**
 * DTOs are used to transfer data between layers
 * They decouple the API from the database schema
 */
class DevilFruitDTO {
    private Long id;
    private String name;
    private String type;
    private Double price;

    // Constructors
    public DevilFruitDTO() {}

    public DevilFruitDTO(Long id, String name, String type, Double price) {
        this.id = id;
        this.name = name;
        this.type = type;
        this.price = price;
    }

    // Static factory method to convert from Entity
    public static DevilFruitDTO fromEntity(DevilFruitEntity entity) {
        return new DevilFruitDTO(
            entity.getId(),
            entity.getName(),
            entity.getType(),
            entity.getPrice()
        );
    }

    // Convert to Entity
    public DevilFruitEntity toEntity() {
        DevilFruitEntity entity = new DevilFruitEntity();
        entity.setId(this.id);
        entity.setName(this.name);
        entity.setType(this.type);
        entity.setPrice(this.price);
        return entity;
    }

    // Getters and Setters
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }

    public String getName() { return name; }
    public void setName(String name) { this.name = name; }

    public String getType() { return type; }
    public void setType(String type) { this.type = type; }

    public Double getPrice() { return price; }
    public void setPrice(Double price) { this.price = price; }
}

/**
 * Request DTO for creating a trade
 */
class CreateTradeRequest {
    private Long userId;
    private Long fruitId;
    private Double amount;

    // Getters and Setters
    public Long getUserId() { return userId; }
    public void setUserId(Long userId) { this.userId = userId; }

    public Long getFruitId() { return fruitId; }
    public void setFruitId(Long fruitId) { this.fruitId = fruitId; }

    public Double getAmount() { return amount; }
    public void setAmount(Double amount) { this.amount = amount; }
}

/**
 * Response DTO for API responses
 */
class ApiResponseDTO<T> {
    private boolean success;
    private String message;
    private T data;
    private String errorCode;

    public static <T> ApiResponseDTO<T> success(T data) {
        ApiResponseDTO<T> response = new ApiResponseDTO<>();
        response.success = true;
        response.data = data;
        response.message = "Success";
        return response;
    }

    public static <T> ApiResponseDTO<T> error(String message, String errorCode) {
        ApiResponseDTO<T> response = new ApiResponseDTO<>();
        response.success = false;
        response.message = message;
        response.errorCode = errorCode;
        return response;
    }

    // Getters and Setters
    public boolean isSuccess() { return success; }
    public void setSuccess(boolean success) { this.success = success; }

    public String getMessage() { return message; }
    public void setMessage(String message) { this.message = message; }

    public T getData() { return data; }
    public void setData(T data) { this.data = data; }

    public String getErrorCode() { return errorCode; }
    public void setErrorCode(String errorCode) { this.errorCode = errorCode; }
}

// ============================================================================
// LAYER 4: SERVICE LAYER (Business Logic)
// ============================================================================

/**
 * ============================================================================
 * SERVICE LAYER - WHERE BUSINESS LOGIC LIVES
 * ============================================================================
 *
 * WHAT IS A SERVICE?
 * A class that contains business logic and orchestrates operations between
 * controllers and repositories.
 *
 * WHY DO WE NEED A SERVICE LAYER?
 * 1. SEPARATION OF CONCERNS
 *    - Controller handles HTTP (requests/responses)
 *    - Service handles business logic (validation, calculations)
 *    - Repository handles database (CRUD operations)
 *
 * 2. REUSABILITY
 *    - Same service can be used by multiple controllers
 *    - Can be called from scheduled tasks, message listeners, etc.
 *
 * 3. TESTABILITY
 *    - Easy to test business logic without HTTP layer
 *    - Can mock repository for unit tests
 *
 * 4. TRANSACTION MANAGEMENT
 *    - @Transactional on service methods ensures data consistency
 *
 * WHAT GOES IN A SERVICE?
 * ✅ Business validation (price > 0, name unique)
 * ✅ Business calculations (discounts, totals)
 * ✅ Orchestration (call multiple repositories)
 * ✅ DTO ↔ Entity conversion
 * ✅ Exception handling
 *
 * WHAT DOESN'T GO IN A SERVICE?
 * ❌ HTTP-specific code (HttpServletRequest, @PathVariable)
 * ❌ Direct SQL queries (use repository)
 * ❌ Presentation logic (formatting for display)
 *
 * ============================================================================
 */

// @Service  ← WHAT: Marks this class as a service component
//              WHY: Spring creates instance and manages it
//              HOW: Spring scans for @Service, creates bean, stores in container
//              WHEN: On classes containing business logic
//              RESULT: Available for dependency injection

class DevilFruitService {

    // ========================================================================
    // DEPENDENCY INJECTION - THE SPRING WAY
    // ========================================================================

    /**
     * DEPENDENCY INJECTION EXPLAINED
     *
     * WHAT IS THIS?
     * Instead of creating DevilFruitSpringRepository ourselves, Spring provides it.
     *
     * OLD WAY (Bad):
     *   private DevilFruitSpringRepository repository = new DevilFruitSpringRepository();
     *   ❌ Tightly coupled
     *   ❌ Hard to test (can't inject mock)
     *   ❌ Can't swap implementations
     *
     * SPRING WAY (Good):
     *   private final DevilFruitSpringRepository repository;
     *   public DevilFruitService(DevilFruitSpringRepository repository) {
     *       this.repository = repository;
     *   }
     *   ✅ Loosely coupled
     *   ✅ Easy to test (inject mock repository)
     *   ✅ Can swap implementations
     *
     * HOW SPRING INJECTS:
     * 1. Spring sees DevilFruitService needs DevilFruitSpringRepository
     * 2. Spring looks in its container for a DevilFruitSpringRepository bean
     * 3. Spring finds it (created from interface extending JpaRepository)
     * 4. Spring calls: new DevilFruitService(repositoryBean)
     * 5. Your service is ready with repository injected!
     *
     * WHY 'final'?
     * - Makes field immutable (can't be changed after construction)
     * - Ensures dependency is always set
     * - Prevents accidental reassignment
     */

    // @Autowired  ← OPTIONAL on constructors (Spring auto-detects)
    //               WHAT: Tells Spring to inject dependency
    //               WHY: Spring needs to know what to inject
    //               WHEN: On constructor (recommended), setter, or field
    //               NOTE: Since Spring 4.3, @Autowired is optional on single constructor

    private final DevilFruitSpringRepository repository;

    /**
     * CONSTRUCTOR INJECTION (BEST PRACTICE)
     *
     * WHY CONSTRUCTOR INJECTION?
     * ✅ Dependencies are required (can't create service without them)
     * ✅ Enables immutability (final fields)
     * ✅ Works without Spring (easier to test)
     * ✅ Makes dependencies explicit
     *
     * ALTERNATIVES (NOT RECOMMENDED):
     *
     * 1. FIELD INJECTION:
     *    @Autowired
     *    private DevilFruitSpringRepository repository;
     *    ❌ Can't make final
     *    ❌ Hard to test (need Spring context)
     *    ❌ Hidden dependencies
     *
     * 2. SETTER INJECTION:
     *    @Autowired
     *    public void setRepository(DevilFruitSpringRepository repository) { ... }
     *    ❌ Dependencies are optional (might be null)
     *    ❌ Can be called multiple times
     */
    public DevilFruitService(DevilFruitSpringRepository repository) {
        this.repository = repository;
        // WHAT HAPPENS HERE:
        // 1. Spring calls this constructor
        // 2. Passes in the repository bean from its container
        // 3. We store it in our field
        // 4. Service is now ready to use!
    }

    // ========================================================================
    // BUSINESS METHODS
    // ========================================================================

    /**
     * getAllFruits() - Retrieve All Devil Fruits
     *
     * WHAT THIS DOES:
     * 1. Calls repository to get all entities from database
     * 2. Converts entities to DTOs (Data Transfer Objects)
     * 3. Returns DTOs to controller
     *
     * WHY CONVERT TO DTO?
     * - Entities contain JPA annotations and database details
     * - DTOs are clean objects for API responses
     * - Prevents exposing internal structure
     * - Avoids lazy loading issues (N+1 queries)
     *
     * HOW IT WORKS LINE BY LINE:
     */
    public List<DevilFruitDTO> getAllFruits() {
        // Step 1: Get all entities from database
        // SQL executed: SELECT * FROM devil_fruits
        List<DevilFruitEntity> entities = repository.findAll();

        // Step 2: Convert each entity to DTO using Stream API
        return entities.stream()                    // Create stream from list
            .map(DevilFruitDTO::fromEntity)         // Transform each entity to DTO
            .collect(java.util.stream.Collectors.toList());  // Collect to list

        // EQUIVALENT WITHOUT STREAMS:
        // List<DevilFruitDTO> dtos = new ArrayList<>();
        // for (DevilFruitEntity entity : entities) {
        //     dtos.add(DevilFruitDTO.fromEntity(entity));
        // }
        // return dtos;
    }

    /**
     * getFruitById() - Retrieve Single Devil Fruit
     *
     * WHAT THIS DOES:
     * 1. Calls repository to find entity by ID
     * 2. If not found, throws exception
     * 3. If found, converts to DTO and returns
     *
     * WHY THROW EXCEPTION?
     * - Controller can catch and return 404 Not Found
     * - Prevents returning null (NullPointerException risk)
     * - Clear error message for debugging
     *
     * BEST PRACTICE:
     * Use custom exception (NotFoundException) instead of RuntimeException
     */
    public DevilFruitDTO getFruitById(Long id) {
        // Step 1: Try to find entity in database
        // SQL executed: SELECT * FROM devil_fruits WHERE id = ?
        DevilFruitEntity entity = repository.findById(id);

        // Step 2: Check if found
        if (entity == null) {
            // Not found - throw exception
            // In real app: throw new NotFoundException("Fruit not found with id: " + id);
            throw new RuntimeException("Fruit not found with id: " + id);
        }

        // Step 3: Convert to DTO and return
        return DevilFruitDTO.fromEntity(entity);

        // IN REAL SPRING BOOT APP (using Optional):
        // return repository.findById(id)
        //     .map(DevilFruitDTO::fromEntity)
        //     .orElseThrow(() -> new NotFoundException("Fruit not found"));
    }

    /**
     * createFruit() - Create New Devil Fruit
     *
     * WHAT THIS DOES:
     * 1. Receives DTO from controller
     * 2. Validates business rules (in real app)
     * 3. Converts DTO to entity
     * 4. Saves to database
     * 5. Converts saved entity back to DTO
     * 6. Returns DTO to controller
     *
     * WHY CONVERT DTO → ENTITY → DTO?
     * - DTO comes from client (JSON request)
     * - Entity is what database understands
     * - Saved entity has generated ID
     * - Return DTO with ID to client
     *
     * BUSINESS VALIDATION (should add):
     * - Name is not empty
     * - Name is unique
     * - Price is positive
     * - Type is valid (Logia, Paramecia, Zoan)
     */
    public DevilFruitDTO createFruit(DevilFruitDTO dto) {
        // STEP 1: VALIDATE (in real app)
        // if (dto.getName() == null || dto.getName().trim().isEmpty()) {
        //     throw new ValidationException("Name is required");
        // }
        // if (dto.getPrice() == null || dto.getPrice() <= 0) {
        //     throw new ValidationException("Price must be positive");
        // }
        // if (repository.existsByName(dto.getName())) {
        //     throw new ValidationException("Fruit with this name already exists");
        // }

        // Step 2: Convert DTO to Entity
        DevilFruitEntity entity = dto.toEntity();
        // entity.setId(null);  // Ensure ID is null for new entity

        // Step 3: Save to database
        // SQL executed: INSERT INTO devil_fruits (name, type, price, ...) VALUES (?, ?, ?, ...)
        DevilFruitEntity saved = repository.save(entity);
        // 'saved' now has the generated ID from database

        // Step 4: Convert saved entity back to DTO
        return DevilFruitDTO.fromEntity(saved);
        // Return DTO with ID to client
    }

    /**
     * updateFruit() - Update Existing Devil Fruit
     *
     * WHAT THIS DOES:
     * 1. Finds existing entity by ID
     * 2. Updates fields with new values
     * 3. Saves updated entity
     * 4. Returns updated DTO
     *
     * HOW JPA KNOWS IT'S AN UPDATE:
     * - Entity has non-null ID → JPA executes UPDATE instead of INSERT
     */
    public DevilFruitDTO updateFruit(Long id, DevilFruitDTO dto) {
        // Step 1: Find existing entity
        DevilFruitEntity existing = repository.findById(id);
        if (existing == null) {
            throw new RuntimeException("Fruit not found with id: " + id);
        }

        // Step 2: Update fields
        existing.setName(dto.getName());
        existing.setType(dto.getType());
        existing.setPrice(dto.getPrice());
        existing.setUpdatedAt(java.time.LocalDateTime.now());

        // Step 3: Save (SQL: UPDATE devil_fruits SET ... WHERE id = ?)
        DevilFruitEntity updated = repository.save(existing);
        return DevilFruitDTO.fromEntity(updated);
    }

    /**
     * deleteFruit() - Delete Devil Fruit
     *
     * WHAT THIS DOES:
     * 1. Checks if fruit exists
     * 2. Deletes it from database
     *
     * SQL EXECUTED: DELETE FROM devil_fruits WHERE id = ?
     */
    public void deleteFruit(Long id) {
        if (!repository.existsById(id)) {
            throw new RuntimeException("Fruit not found with id: " + id);
        }
        repository.deleteById(id);
    }

    /**
     * getFruitsByType() - Filter by Type
     *
     * DEMONSTRATES: Custom query method
     * SQL: SELECT * FROM devil_fruits WHERE type = ?
     */
    public List<DevilFruitDTO> getFruitsByType(String type) {
        List<DevilFruitEntity> entities = repository.findByType(type);
        return entities.stream()
            .map(DevilFruitDTO::fromEntity)
            .collect(java.util.stream.Collectors.toList());
    }

    /**
     * getFruitsByPriceRange() - Filter by Price Range
     *
     * DEMONSTRATES: Query method with multiple parameters
     * SQL: SELECT * FROM devil_fruits WHERE price BETWEEN ? AND ?
     */
    public List<DevilFruitDTO> getFruitsByPriceRange(Double minPrice, Double maxPrice) {
        List<DevilFruitEntity> entities = repository.findByPriceBetween(minPrice, maxPrice);
        return entities.stream()
            .map(DevilFruitDTO::fromEntity)
            .collect(java.util.stream.Collectors.toList());
    }

    // ========================================================================
    // @TRANSACTIONAL EXPLAINED
    // ========================================================================

    /**
     * WHAT IS @Transactional?
     * Wraps method in a database transaction - all operations succeed or all fail.
     *
     * WHY USE IT?
     * Ensures data consistency when multiple database operations are involved.
     *
     * EXAMPLE: Transfer money between users
     * @Transactional
     * public void transferMoney(Long fromId, Long toId, Double amount) {
     *     User from = userRepo.findById(fromId);
     *     User to = userRepo.findById(toId);
     *     from.setBalance(from.getBalance() - amount);  // Deduct from sender
     *     userRepo.save(from);
     *     // If crash happens here, both operations are rolled back!
     *     to.setBalance(to.getBalance() + amount);      // Add to receiver
     *     userRepo.save(to);
     * }
     *
     * WITHOUT @Transactional:
     * - Money deducted from sender
     * - Crash occurs
     * - Money never added to receiver
     * - Money disappeared! 💸
     *
     * WITH @Transactional:
     * - If any step fails, ALL changes are undone
     * - Database returns to state before method started
     * - Data consistency guaranteed! ✅
     *
     * WHEN TO USE:
     * ✅ Methods that modify data (create, update, delete)
     * ✅ Methods with multiple database operations
     * ✅ Methods that must be atomic (all-or-nothing)
     *
     * HOW IT WORKS:
     * 1. Spring starts transaction before method
     * 2. All database operations are part of this transaction
     * 3. If method completes → COMMIT (save all changes)
     * 4. If exception occurs → ROLLBACK (undo all changes)
     */
}

/**
 * Trade Service - handles business logic for trades
 */
// @Service
class TradeService {
    private final UserSpringRepository userRepository;
    private final DevilFruitSpringRepository fruitRepository;

    public TradeService(UserSpringRepository userRepository,
                       DevilFruitSpringRepository fruitRepository) {
        this.userRepository = userRepository;
        this.fruitRepository = fruitRepository;
    }

    /**
     * Process a trade with business logic validation
     * This is a @Transactional method in real Spring Boot
     */
    // @Transactional
    public TradeResult processTrade(CreateTradeRequest request) {
        TradeResult result = new TradeResult();

        try {
            // 1. Validate user exists
            UserEntity user = userRepository.findById(request.getUserId());
            if (user == null) {
                result.setSuccess(false);
                result.setMessage("User not found");
                return result;
            }

            // 2. Validate fruit exists
            DevilFruitEntity fruit = fruitRepository.findById(request.getFruitId());
            if (fruit == null) {
                result.setSuccess(false);
                result.setMessage("Devil Fruit not found");
                return result;
            }

            // 3. Check user balance
            if (user.getBalance() < request.getAmount()) {
                result.setSuccess(false);
                result.setMessage("Insufficient balance");
                return result;
            }

            // 4. Process the trade
            user.setBalance(user.getBalance() - request.getAmount());
            userRepository.save(user);

            // 5. Create trade record
            TradeEntity trade = new TradeEntity();
            trade.setUser(user);
            trade.setFruit(fruit);
            trade.setAmount(request.getAmount());
            trade.setStatus("COMPLETED");

            result.setSuccess(true);
            result.setMessage("Trade completed successfully");
            result.setTransactionId("TXN-" + System.currentTimeMillis());

        } catch (Exception e) {
            result.setSuccess(false);
            result.setMessage("Error processing trade: " + e.getMessage());
        }

        return result;
    }
}

// ============================================================================
// LAYER 5: CONTROLLER LAYER (REST API)
// ============================================================================

/**
 * REST Controller for Devil Fruits
 *
 * In real Spring Boot app, annotate with @RestController
 * @RequestMapping("/api/fruits") sets base path
 */
// @RestController
// @RequestMapping("/api/fruits")
class DevilFruitController {
    // @Autowired
    private final DevilFruitService fruitService;

    public DevilFruitController(DevilFruitService fruitService) {
        this.fruitService = fruitService;
    }

    /**
     * GET /api/fruits - Get all fruits
     * @GetMapping
     */
    public ApiResponseDTO<List<DevilFruitDTO>> getAllFruits() {
        try {
            List<DevilFruitDTO> fruits = fruitService.getAllFruits();
            return ApiResponseDTO.success(fruits);
        } catch (Exception e) {
            return ApiResponseDTO.error(e.getMessage(), "GET_ALL_ERROR");
        }
    }

    /**
     * GET /api/fruits/{id} - Get fruit by ID
     * @GetMapping("/{id}")
     */
    public ApiResponseDTO<DevilFruitDTO> getFruitById(Long id) {
        try {
            DevilFruitDTO fruit = fruitService.getFruitById(id);
            return ApiResponseDTO.success(fruit);
        } catch (Exception e) {
            return ApiResponseDTO.error(e.getMessage(), "NOT_FOUND");
        }
    }

    /**
     * POST /api/fruits - Create new fruit
     * @PostMapping
     */
    public ApiResponseDTO<DevilFruitDTO> createFruit(DevilFruitDTO dto) {
        try {
            DevilFruitDTO created = fruitService.createFruit(dto);
            return ApiResponseDTO.success(created);
        } catch (Exception e) {
            return ApiResponseDTO.error(e.getMessage(), "CREATE_ERROR");
        }
    }

    /**
     * PUT /api/fruits/{id} - Update fruit
     * @PutMapping("/{id}")
     */
    public ApiResponseDTO<DevilFruitDTO> updateFruit(Long id, DevilFruitDTO dto) {
        try {
            DevilFruitDTO updated = fruitService.updateFruit(id, dto);
            return ApiResponseDTO.success(updated);
        } catch (Exception e) {
            return ApiResponseDTO.error(e.getMessage(), "UPDATE_ERROR");
        }
    }

    /**
     * DELETE /api/fruits/{id} - Delete fruit
     * @DeleteMapping("/{id}")
     */
    public ApiResponseDTO<Void> deleteFruit(Long id) {
        try {
            fruitService.deleteFruit(id);
            return ApiResponseDTO.success(null);
        } catch (Exception e) {
            return ApiResponseDTO.error(e.getMessage(), "DELETE_ERROR");
        }
    }

    /**
     * GET /api/fruits/search?type=Logia - Search by type
     * @GetMapping("/search")
     */
    public ApiResponseDTO<List<DevilFruitDTO>> searchByType(String type) {
        try {
            List<DevilFruitDTO> fruits = fruitService.getFruitsByType(type);
            return ApiResponseDTO.success(fruits);
        } catch (Exception e) {
            return ApiResponseDTO.error(e.getMessage(), "SEARCH_ERROR");
        }
    }
}

/**
 * Trade Controller
 */
// @RestController
// @RequestMapping("/api/trades")
class TradeController {
    private final TradeService tradeService;

    public TradeController(TradeService tradeService) {
        this.tradeService = tradeService;
    }

    /**
     * POST /api/trades - Create a new trade
     * @PostMapping
     */
    public ApiResponseDTO<TradeResult> createTrade(CreateTradeRequest request) {
        try {
            TradeResult result = tradeService.processTrade(request);
            if (result.isSuccess()) {
                return ApiResponseDTO.success(result);
            } else {
                return ApiResponseDTO.error(result.getMessage(), "TRADE_FAILED");
            }
        } catch (Exception e) {
            return ApiResponseDTO.error(e.getMessage(), "TRADE_ERROR");
        }
    }
}

// ============================================================================
// CONFIGURATION AND DATABASE SETUP
// ============================================================================

/**
 * APPLICATION.PROPERTIES CONFIGURATION
 *
 * This file configures your Spring Boot application.
 * Place this in src/main/resources/application.properties
 *
 * ============================================================================
 * CLOUD DATABASE CONFIGURATION - POSTGRESQL
 * ============================================================================
 *
 * # Database Configuration (PostgreSQL on AWS RDS, Heroku, or other cloud)
 * spring.datasource.url=jdbc:postgresql://your-db-host.rds.amazonaws.com:5432/onepiece_trading
 * spring.datasource.username=your_username
 * spring.datasource.password=your_password
 * spring.datasource.driver-class-name=org.postgresql.Driver
 *
 * # JPA/Hibernate Configuration
 * spring.jpa.database-platform=org.hibernate.dialect.PostgreSQLDialect
 * spring.jpa.hibernate.ddl-auto=update
 * spring.jpa.show-sql=true
 * spring.jpa.properties.hibernate.format_sql=true
 *
 * # Connection Pool Configuration (HikariCP - default in Spring Boot)
 * spring.datasource.hikari.maximum-pool-size=10
 * spring.datasource.hikari.minimum-idle=5
 * spring.datasource.hikari.connection-timeout=20000
 *
 * # Application Configuration
 * server.port=8080
 * spring.application.name=onepiece-trading-platform
 *
 * ============================================================================
 * ALTERNATIVE: MYSQL ON CLOUD
 * ============================================================================
 *
 * spring.datasource.url=jdbc:mysql://your-db-host:3306/onepiece_trading
 * spring.datasource.username=your_username
 * spring.datasource.password=your_password
 * spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver
 * spring.jpa.database-platform=org.hibernate.dialect.MySQL8Dialect
 *
 * ============================================================================
 * ENVIRONMENT-SPECIFIC CONFIGURATION
 * ============================================================================
 *
 * For production, use environment variables instead of hardcoding:
 *
 * spring.datasource.url=${DATABASE_URL}
 * spring.datasource.username=${DB_USERNAME}
 * spring.datasource.password=${DB_PASSWORD}
 *
 * ============================================================================
 */

/**
 * POM.XML DEPENDENCIES
 *
 * Add these dependencies to your pom.xml file:
 *
 * <dependencies>
 *     <!-- Spring Boot Starter Web -->
 *     <dependency>
 *         <groupId>org.springframework.boot</groupId>
 *         <artifactId>spring-boot-starter-web</artifactId>
 *     </dependency>
 *
 *     <!-- Spring Boot Starter Data JPA -->
 *     <dependency>
 *         <groupId>org.springframework.boot</groupId>
 *         <artifactId>spring-boot-starter-data-jpa</artifactId>
 *     </dependency>
 *
 *     <!-- PostgreSQL Driver -->
 *     <dependency>
 *         <groupId>org.postgresql</groupId>
 *         <artifactId>postgresql</artifactId>
 *         <scope>runtime</scope>
 *     </dependency>
 *
 *     <!-- Validation -->
 *     <dependency>
 *         <groupId>org.springframework.boot</groupId>
 *         <artifactId>spring-boot-starter-validation</artifactId>
 *     </dependency>
 *
 *     <!-- Lombok (optional, reduces boilerplate) -->
 *     <dependency>
 *         <groupId>org.projectlombok</groupId>
 *         <artifactId>lombok</artifactId>
 *         <optional>true</optional>
 *     </dependency>
 * </dependencies>
 */

/**
 * Main Spring Boot Application Class
 *
 * This is the entry point of your Spring Boot application
 */
// @SpringBootApplication
class OnePieceTradingApplication {

    public static void main(String[] args) {
        // SpringApplication.run(OnePieceTradingApplication.class, args);
        System.out.println("One Piece Trading Platform - Spring Boot Application");
        System.out.println("This would start the embedded Tomcat server on port 8080");
        System.out.println("API would be available at: http://localhost:8080/api/fruits");
    }
}

/*
================================================================================
WHAT HAPPENS WHEN YOU RUN A SPRING BOOT APPLICATION?
================================================================================

Let's trace exactly what happens from start to finish:

STEP 1: YOU RUN THE APPLICATION
--------------------------------
Command: java -jar onepiece-trading.jar
Or: mvn spring-boot:run
Or: Click "Run" in your IDE

STEP 2: MAIN METHOD EXECUTES
-----------------------------
@SpringBootApplication
public class OnePieceTradingApplication {
    public static void main(String[] args) {
        SpringApplication.run(OnePieceTradingApplication.class, args);
        ↑ This single line does EVERYTHING
    }
}

STEP 3: SPRING BOOT AUTO-CONFIGURATION
---------------------------------------
Spring Boot looks at your classpath (what libraries you have) and auto-configures:

Found spring-boot-starter-web?
  ✅ Configure embedded Tomcat server
  ✅ Set up Spring MVC
  ✅ Configure JSON serialization (Jackson)
  ✅ Set up error handling

Found spring-boot-starter-data-jpa?
  ✅ Configure Hibernate
  ✅ Set up EntityManager
  ✅ Configure transaction management
  ✅ Create JPA repositories

Found PostgreSQL driver?
  ✅ Configure PostgreSQL dialect
  ✅ Set up connection pool (HikariCP)
  ✅ Read database URL from application.properties

STEP 4: COMPONENT SCANNING
---------------------------
Spring scans your code for components:

Scanning package: com.onepiece.trading
  Found @Entity classes:
    ✅ DevilFruitEntity → Create table mapping
    ✅ UserEntity → Create table mapping
    ✅ TradeEntity → Create table mapping

  Found @Repository interfaces:
    ✅ DevilFruitRepository → Create proxy implementation
    ✅ UserRepository → Create proxy implementation

  Found @Service classes:
    ✅ DevilFruitService → Create bean
    ✅ TradeService → Create bean

  Found @RestController classes:
    ✅ DevilFruitController → Create bean, map endpoints
    ✅ TradeController → Create bean, map endpoints

STEP 5: DEPENDENCY RESOLUTION
------------------------------
Spring analyzes dependencies:

DevilFruitController needs DevilFruitService
  ↓
DevilFruitService needs DevilFruitRepository
  ↓
DevilFruitRepository needs EntityManager
  ↓
EntityManager needs DataSource (database connection)

Spring creates dependency graph and determines creation order.

STEP 6: BEAN CREATION
----------------------
Spring creates beans in correct order:

1. Create DataSource (database connection pool)
2. Create EntityManager (JPA)
3. Create DevilFruitRepository (proxy)
4. Create DevilFruitService (inject repository)
5. Create DevilFruitController (inject service)

All beans are stored in ApplicationContext (Spring's container).

STEP 7: DATABASE INITIALIZATION
--------------------------------
If spring.jpa.hibernate.ddl-auto=update:

Hibernate connects to database
Hibernate reads @Entity classes
Hibernate compares with existing tables
Hibernate generates DDL:
  CREATE TABLE IF NOT EXISTS devil_fruits (
      id BIGSERIAL PRIMARY KEY,
      name VARCHAR(255) NOT NULL UNIQUE,
      type VARCHAR(255) NOT NULL,
      price DOUBLE PRECISION NOT NULL,
      created_at TIMESTAMP,
      updated_at TIMESTAMP
  );

Tables are created/updated automatically!

STEP 8: ENDPOINT MAPPING
-------------------------
Spring maps controller methods to URLs:

@GetMapping("/api/fruits")
  → GET http://localhost:8080/api/fruits → getAllFruits()

@PostMapping("/api/fruits")
  → POST http://localhost:8080/api/fruits → createFruit()

@GetMapping("/api/fruits/{id}")
  → GET http://localhost:8080/api/fruits/1 → getFruitById(1)

@PutMapping("/api/fruits/{id}")
  → PUT http://localhost:8080/api/fruits/1 → updateFruit(1, dto)

@DeleteMapping("/api/fruits/{id}")
  → DELETE http://localhost:8080/api/fruits/1 → deleteFruit(1)

STEP 9: SERVER STARTUP
-----------------------
Embedded Tomcat server starts:
  ✅ Listening on port 8080
  ✅ Ready to accept HTTP requests
  ✅ All endpoints registered

Console output:
  Started OnePieceTradingApplication in 3.456 seconds

STEP 10: READY TO SERVE REQUESTS!
----------------------------------
Application is now running and waiting for requests.

WHAT HAPPENS WHEN A REQUEST COMES IN?
======================================

Example: POST /api/fruits with JSON body

REQUEST FLOW:
-------------
1. Tomcat receives HTTP request
2. Spring MVC routes to DevilFruitController.createFruit()
3. Jackson converts JSON to DevilFruitDTO object
4. Controller calls DevilFruitService.createFruit(dto)
5. Service validates and converts DTO to Entity
6. Service calls DevilFruitRepository.save(entity)
7. Repository proxy generates SQL: INSERT INTO devil_fruits...
8. Hibernate executes SQL on database
9. Database returns generated ID
10. Entity with ID flows back through layers
11. Service converts Entity to DTO
12. Controller returns DTO
13. Jackson converts DTO to JSON
14. Tomcat sends HTTP response to client

COMPLETE FLOW DIAGRAM:
----------------------
Client
  ↓ HTTP Request (JSON)
Tomcat (Web Server)
  ↓
Spring MVC (Request Routing)
  ↓
Controller (REST API)
  ↓ DTO
Service (Business Logic)
  ↓ Entity
Repository (Data Access)
  ↓ SQL
Hibernate (ORM)
  ↓
Database (PostgreSQL)
  ↓ Result
Hibernate
  ↓ Entity
Repository
  ↓ Entity
Service
  ↓ DTO
Controller
  ↓ JSON
Spring MVC
  ↓
Tomcat
  ↓ HTTP Response (JSON)
Client

EVERY LAYER HAS A PURPOSE:
--------------------------
Controller: Handle HTTP, validate input, return responses
Service: Business logic, orchestration, transactions
Repository: Database operations, queries
Entity: Database table representation

This separation makes code:
✅ Testable (mock each layer)
✅ Maintainable (change one layer without affecting others)
✅ Scalable (add features easily)
✅ Professional (industry standard)

================================================================================
*/

/**
 * SPRING FRAMEWORK DEMO
 */
class SpringFrameworkDemo {
    public static void runDemo() {
        System.out.println("\n" + "=".repeat(80));
        System.out.println("TOPIC 7: SPRING FRAMEWORK DEMO");
        System.out.println("=".repeat(80));

        System.out.println("\n--- Spring Boot Application Structure ---");
        System.out.println("✓ Entity Layer: DevilFruitEntity, UserEntity, TradeEntity");
        System.out.println("✓ Repository Layer: DevilFruitSpringRepository (extends JpaRepository)");
        System.out.println("✓ Service Layer: DevilFruitService, TradeService");
        System.out.println("✓ Controller Layer: DevilFruitController, TradeController");
        System.out.println("✓ DTO Layer: DevilFruitDTO, ApiResponseDTO");

        System.out.println("\n--- Cloud Database Integration ---");
        System.out.println("Spring Boot connects to cloud databases like:");
        System.out.println("1. PostgreSQL on AWS RDS");
        System.out.println("2. MySQL on Google Cloud SQL");
        System.out.println("3. PostgreSQL on Heroku");
        System.out.println("4. Azure Database for PostgreSQL");

        System.out.println("\n--- Key Differences: Local vs Cloud Database ---");
        System.out.println("LOCAL (ArrayList):");
        System.out.println("  - Data stored in memory");
        System.out.println("  - Lost when application restarts");
        System.out.println("  - No concurrent access from multiple servers");
        System.out.println("  - Not suitable for production");

        System.out.println("\nCLOUD DATABASE (PostgreSQL/MySQL):");
        System.out.println("  - Data persisted on disk");
        System.out.println("  - Survives application restarts");
        System.out.println("  - Multiple servers can access same data");
        System.out.println("  - Automatic backups and replication");
        System.out.println("  - Scalable and production-ready");

        System.out.println("\n--- REST API Endpoints ---");
        System.out.println("GET    /api/fruits           - Get all fruits");
        System.out.println("GET    /api/fruits/{id}      - Get fruit by ID");
        System.out.println("POST   /api/fruits           - Create new fruit");
        System.out.println("PUT    /api/fruits/{id}      - Update fruit");
        System.out.println("DELETE /api/fruits/{id}      - Delete fruit");
        System.out.println("GET    /api/fruits/search    - Search fruits");
        System.out.println("POST   /api/trades           - Create trade");

        System.out.println("\n--- Example API Request/Response ---");
        System.out.println("POST /api/fruits");
        System.out.println("Request Body:");
        System.out.println("{");
        System.out.println("  \"name\": \"Gomu Gomu no Mi\",");
        System.out.println("  \"type\": \"Paramecia\",");
        System.out.println("  \"price\": 1000000");
        System.out.println("}");
        System.out.println("\nResponse:");
        System.out.println("{");
        System.out.println("  \"success\": true,");
        System.out.println("  \"message\": \"Success\",");
        System.out.println("  \"data\": {");
        System.out.println("    \"id\": 1,");
        System.out.println("    \"name\": \"Gomu Gomu no Mi\",");
        System.out.println("    \"type\": \"Paramecia\",");
        System.out.println("    \"price\": 1000000");
        System.out.println("  }");
        System.out.println("}");

        System.out.println("\n" + "=".repeat(80));
        System.out.println("KEY TAKEAWAYS:");
        System.out.println("1. Spring Boot simplifies enterprise application development");
        System.out.println("2. Layered architecture: Controller -> Service -> Repository -> Database");
        System.out.println("3. Spring Data JPA eliminates boilerplate database code");
        System.out.println("4. Cloud databases provide persistence and scalability");
        System.out.println("5. DTOs decouple API from database schema");
        System.out.println("6. Dependency Injection makes code testable and maintainable");
        System.out.println("7. REST APIs follow standard HTTP methods (GET, POST, PUT, DELETE)");
        System.out.println("8. Configuration externalized in application.properties");
        System.out.println("=".repeat(80));
    }
}

/*
================================================================================
TOPIC 8: DATABASE INTEGRATION (JPA/HIBERNATE)
================================================================================

JPA (Java Persistence API) is the standard for ORM (Object-Relational Mapping)
in Java. Hibernate is the most popular JPA implementation.

WHY JPA/HIBERNATE MATTERS IN ENTERPRISE:
1. Database Independence: Switch databases without changing code
2. Object-Oriented: Work with objects, not SQL
3. Automatic CRUD: No need to write basic SQL
4. Relationship Mapping: Handle complex relationships easily
5. Caching: Built-in caching for performance
6. Transaction Management: Automatic transaction handling

KEY CONCEPTS:
- Entity: Java class mapped to database table
- EntityManager: Interface to interact with persistence context
- Persistence Context: Set of managed entity instances
- Transaction: Unit of work (ACID properties)
- Lazy Loading: Load data only when needed
- Eager Loading: Load data immediately
- Cascade: Propagate operations to related entities

JPA ANNOTATIONS:
- @Entity: Mark class as entity
- @Table: Specify table name
- @Id: Primary key
- @GeneratedValue: Auto-generate ID
- @Column: Column mapping
- @OneToOne: One-to-one relationship
- @OneToMany: One-to-many relationship
- @ManyToOne: Many-to-one relationship
- @ManyToMany: Many-to-many relationship
- @JoinColumn: Foreign key column
- @Transactional: Transaction boundary

HIBERNATE FEATURES:
- HQL (Hibernate Query Language): Object-oriented queries
- Criteria API: Type-safe queries
- Caching: First-level (session) and second-level (application)
- Batch Processing: Efficient bulk operations
- Dirty Checking: Automatic change detection

BEST PRACTICES:
1. Use @Transactional for data modification
2. Avoid N+1 query problem (use JOIN FETCH)
3. Use pagination for large result sets
4. Configure connection pooling
5. Use DTOs to avoid lazy loading issues
6. Index frequently queried columns
7. Use native queries for complex operations
================================================================================
*/

/**
 * ADVANCED JPA ENTITY EXAMPLES
 */

/**
 * Complete Devil Fruit Entity with all JPA features
 */
// @Entity
// @Table(name = "devil_fruits", indexes = {
//     @Index(name = "idx_type", columnList = "type"),
//     @Index(name = "idx_price", columnList = "price")
// })
class CompleteDevilFruitEntity {

    // @Id
    // @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    // @Column(nullable = false, unique = true, length = 100)
    private String name;

    // @Column(nullable = false, length = 50)
    // @Enumerated(EnumType.STRING)
    private String type; // In real app, use enum

    // @Column(nullable = false, precision = 10, scale = 2)
    private Double price;

    // @Column(columnDefinition = "TEXT")
    private String description;

    // @Column(name = "is_legendary")
    private Boolean isLegendary;

    // @Column(name = "created_at", nullable = false, updatable = false)
    // @CreationTimestamp
    private java.time.LocalDateTime createdAt;

    // @Column(name = "updated_at")
    // @UpdateTimestamp
    private java.time.LocalDateTime updatedAt;

    // @Version (Optimistic locking)
    private Long version;

    // One-to-Many relationship
    // @OneToMany(mappedBy = "fruit", cascade = CascadeType.ALL, orphanRemoval = true)
    private List<TradeEntity> trades = new ArrayList<>();

    // Many-to-Many relationship
    // @ManyToMany
    // @JoinTable(
    //     name = "fruit_abilities",
    //     joinColumns = @JoinColumn(name = "fruit_id"),
    //     inverseJoinColumns = @JoinColumn(name = "ability_id")
    // )
    private List<AbilityEntity> abilities = new ArrayList<>();

    // Lifecycle callbacks
    // @PrePersist
    protected void onCreate() {
        createdAt = java.time.LocalDateTime.now();
        updatedAt = java.time.LocalDateTime.now();
    }

    // @PreUpdate
    protected void onUpdate() {
        updatedAt = java.time.LocalDateTime.now();
    }

    // Getters and Setters
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }

    public String getName() { return name; }
    public void setName(String name) { this.name = name; }

    public String getType() { return type; }
    public void setType(String type) { this.type = type; }

    public Double getPrice() { return price; }
    public void setPrice(Double price) { this.price = price; }

    public String getDescription() { return description; }
    public void setDescription(String description) { this.description = description; }

    public Boolean getIsLegendary() { return isLegendary; }
    public void setIsLegendary(Boolean isLegendary) { this.isLegendary = isLegendary; }

    public List<TradeEntity> getTrades() { return trades; }
    public void setTrades(List<TradeEntity> trades) { this.trades = trades; }

    public List<AbilityEntity> getAbilities() { return abilities; }
    public void setAbilities(List<AbilityEntity> abilities) { this.abilities = abilities; }
}

/**
 * Ability Entity for Many-to-Many relationship
 */
// @Entity
// @Table(name = "abilities")
class AbilityEntity {
    // @Id
    // @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    // @Column(nullable = false, unique = true)
    private String name;

    private String description;

    // @ManyToMany(mappedBy = "abilities")
    private List<CompleteDevilFruitEntity> fruits = new ArrayList<>();

    // Getters and Setters
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }

    public String getName() { return name; }
    public void setName(String name) { this.name = name; }

    public String getDescription() { return description; }
    public void setDescription(String description) { this.description = description; }
}

/**
 * User Inventory - One-to-One relationship example
 */
// @Entity
// @Table(name = "user_inventory")
class UserInventoryEntity {
    // @Id
    // @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    // @OneToOne
    // @JoinColumn(name = "user_id", unique = true)
    private UserEntity user;

    // @Column(name = "total_fruits")
    private Integer totalFruits;

    // @Column(name = "total_value")
    private Double totalValue;

    // Getters and Setters
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }

    public UserEntity getUser() { return user; }
    public void setUser(UserEntity user) { this.user = user; }

    public Integer getTotalFruits() { return totalFruits; }
    public void setTotalFruits(Integer totalFruits) { this.totalFruits = totalFruits; }

    public Double getTotalValue() { return totalValue; }
    public void setTotalValue(Double totalValue) { this.totalValue = totalValue; }
}

/**
 * ADVANCED REPOSITORY WITH CUSTOM QUERIES
 */
interface AdvancedDevilFruitRepository {

    // ========================================================================
    // QUERY METHODS (Spring Data generates SQL from method name)
    // ========================================================================

    // Find by single property
    List<CompleteDevilFruitEntity> findByType(String type);

    // Find by multiple properties
    List<CompleteDevilFruitEntity> findByTypeAndIsLegendary(String type, Boolean isLegendary);

    // Find with comparison operators
    List<CompleteDevilFruitEntity> findByPriceGreaterThan(Double price);
    List<CompleteDevilFruitEntity> findByPriceLessThanEqual(Double price);
    List<CompleteDevilFruitEntity> findByPriceBetween(Double minPrice, Double maxPrice);

    // Find with string operations
    List<CompleteDevilFruitEntity> findByNameContaining(String keyword);
    List<CompleteDevilFruitEntity> findByNameStartingWith(String prefix);
    List<CompleteDevilFruitEntity> findByNameEndingWith(String suffix);

    // Find with null checks
    List<CompleteDevilFruitEntity> findByDescriptionIsNull();
    List<CompleteDevilFruitEntity> findByDescriptionIsNotNull();

    // Find with ordering
    List<CompleteDevilFruitEntity> findByTypeOrderByPriceDesc(String type);
    List<CompleteDevilFruitEntity> findByTypeOrderByNameAsc(String type);

    // Find with limiting
    List<CompleteDevilFruitEntity> findTop5ByOrderByPriceDesc();
    List<CompleteDevilFruitEntity> findFirst10ByType(String type);

    // Count queries
    long countByType(String type);
    long countByPriceGreaterThan(Double price);

    // Exists queries
    boolean existsByName(String name);
    boolean existsByTypeAndPriceGreaterThan(String type, Double price);

    // Delete queries
    void deleteByType(String type);
    long deleteByPriceLessThan(Double price);

    // ========================================================================
    // CUSTOM QUERIES WITH @Query
    // ========================================================================

    // JPQL Query
    // @Query("SELECT f FROM CompleteDevilFruitEntity f WHERE f.type = :type AND f.price > :minPrice")
    List<CompleteDevilFruitEntity> findExpensiveFruitsByType(String type, Double minPrice);

    // JPQL with JOIN
    // @Query("SELECT f FROM CompleteDevilFruitEntity f JOIN f.abilities a WHERE a.name = :abilityName")
    List<CompleteDevilFruitEntity> findByAbilityName(String abilityName);

    // JPQL with aggregation
    // @Query("SELECT f.type, AVG(f.price) FROM CompleteDevilFruitEntity f GROUP BY f.type")
    List<Object[]> getAveragePriceByType();

    // Native SQL Query
    // @Query(value = "SELECT * FROM devil_fruits WHERE price > ?1 ORDER BY price DESC LIMIT 10",
    //        nativeQuery = true)
    List<CompleteDevilFruitEntity> findTop10ExpensiveFruitsNative(Double minPrice);

    // Update query
    // @Modifying
    // @Query("UPDATE CompleteDevilFruitEntity f SET f.price = f.price * :multiplier WHERE f.type = :type")
    int updatePricesByType(String type, Double multiplier);

    // Delete query
    // @Modifying
    // @Query("DELETE FROM CompleteDevilFruitEntity f WHERE f.price < :minPrice")
    int deleteInexpensiveFruits(Double minPrice);

    // ========================================================================
    // PAGINATION AND SORTING
    // ========================================================================

    // Using Pageable
    // Page<CompleteDevilFruitEntity> findByType(String type, Pageable pageable);

    // Using Sort
    // List<CompleteDevilFruitEntity> findByType(String type, Sort sort);
}

/**
 * ADVANCED SERVICE WITH TRANSACTIONS
 */
// @Service
class AdvancedDevilFruitService {

    private final AdvancedDevilFruitRepository repository;

    public AdvancedDevilFruitService(AdvancedDevilFruitRepository repository) {
        this.repository = repository;
    }

    /**
     * Transaction example - all operations succeed or all fail
     */
    // @Transactional
    public void transferFruit(Long fromUserId, Long toUserId, Long fruitId) {
        // All database operations in this method are part of one transaction
        // If any operation fails, all changes are rolled back

        // 1. Remove fruit from first user
        // 2. Add fruit to second user
        // 3. Create transfer record

        // If step 3 fails, steps 1 and 2 are automatically rolled back
    }

    /**
     * Read-only transaction (optimization)
     */
    // @Transactional(readOnly = true)
    public List<CompleteDevilFruitEntity> getExpensiveFruits(Double minPrice) {
        return repository.findByPriceGreaterThan(minPrice);
    }

    /**
     * Transaction with custom isolation level
     */
    // @Transactional(isolation = Isolation.SERIALIZABLE)
    public void criticalOperation() {
        // Highest isolation level - prevents all concurrency issues
    }

    /**
     * Transaction with custom propagation
     */
    // @Transactional(propagation = Propagation.REQUIRES_NEW)
    public void independentOperation() {
        // Always creates a new transaction, even if one exists
    }

    /**
     * Batch processing for performance
     */
    // @Transactional
    public void importFruitsInBatch(List<CompleteDevilFruitEntity> fruits) {
        int batchSize = 50;
        for (int i = 0; i < fruits.size(); i++) {
            repository.save(fruits.get(i));

            // Flush and clear every batch to avoid memory issues
            if (i % batchSize == 0 && i > 0) {
                // entityManager.flush();
                // entityManager.clear();
            }
        }
    }
}

/**
 * DATABASE CONNECTION EXAMPLES
 */
class DatabaseConnectionExamples {

    /**
     * EXAMPLE 1: PostgreSQL on AWS RDS
     *
     * application.properties:
     * spring.datasource.url=jdbc:postgresql://mydb.abc123.us-east-1.rds.amazonaws.com:5432/onepiece
     * spring.datasource.username=admin
     * spring.datasource.password=${DB_PASSWORD}
     * spring.jpa.database-platform=org.hibernate.dialect.PostgreSQLDialect
     *
     * AWS RDS Setup:
     * 1. Create RDS PostgreSQL instance in AWS Console
     * 2. Configure security group to allow your IP
     * 3. Note the endpoint URL
     * 4. Create database: CREATE DATABASE onepiece;
     * 5. Update application.properties with connection details
     */

    /**
     * EXAMPLE 2: PostgreSQL on Heroku
     *
     * Heroku automatically provides DATABASE_URL environment variable:
     *
     * application.properties:
     * spring.datasource.url=${DATABASE_URL}
     * spring.jpa.database-platform=org.hibernate.dialect.PostgreSQLDialect
     *
     * Heroku Setup:
     * 1. Create Heroku app: heroku create onepiece-trading
     * 2. Add PostgreSQL addon: heroku addons:create heroku-postgresql:hobby-dev
     * 3. Deploy your Spring Boot app
     * 4. Database URL is automatically configured
     */

    /**
     * EXAMPLE 3: MySQL on Google Cloud SQL
     *
     * application.properties:
     * spring.datasource.url=jdbc:mysql://35.123.456.789:3306/onepiece
     * spring.datasource.username=root
     * spring.datasource.password=${DB_PASSWORD}
     * spring.jpa.database-platform=org.hibernate.dialect.MySQL8Dialect
     *
     * Google Cloud Setup:
     * 1. Create Cloud SQL MySQL instance
     * 2. Create database: onepiece
     * 3. Configure authorized networks
     * 4. Use Cloud SQL Proxy for secure connection
     */

    /**
     * EXAMPLE 4: Connection Pooling Configuration
     *
     * application.properties:
     * # HikariCP (default in Spring Boot)
     * spring.datasource.hikari.maximum-pool-size=20
     * spring.datasource.hikari.minimum-idle=5
     * spring.datasource.hikari.connection-timeout=30000
     * spring.datasource.hikari.idle-timeout=600000
     * spring.datasource.hikari.max-lifetime=1800000
     *
     * Why Connection Pooling?
     * - Reuse database connections (expensive to create)
     * - Better performance under load
     * - Control concurrent database connections
     * - Essential for production applications
     */

    /**
     * EXAMPLE 5: Multiple Database Configuration
     */
    // @Configuration
    // @EnableTransactionManagement
    class MultiDatabaseConfig {

        // Primary Database (PostgreSQL)
        // @Primary
        // @Bean(name = "primaryDataSource")
        // @ConfigurationProperties(prefix = "spring.datasource.primary")
        public javax.sql.DataSource primaryDataSource() {
            // return DataSourceBuilder.create().build();
            return null;
        }

        // Secondary Database (MySQL)
        // @Bean(name = "secondaryDataSource")
        // @ConfigurationProperties(prefix = "spring.datasource.secondary")
        public javax.sql.DataSource secondaryDataSource() {
            // return DataSourceBuilder.create().build();
            return null;
        }
    }
}

/**
 * REAL-WORLD DATABASE SCHEMA
 *
 * This is what the actual database tables would look like:
 */
class DatabaseSchema {

    /**
     * SQL Schema for PostgreSQL
     *
     * -- Users table
     * CREATE TABLE users (
     *     id BIGSERIAL PRIMARY KEY,
     *     username VARCHAR(50) NOT NULL UNIQUE,
     *     email VARCHAR(100) NOT NULL UNIQUE,
     *     balance DECIMAL(10, 2) NOT NULL DEFAULT 0,
     *     created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
     *     updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
     * );
     *
     * -- Devil Fruits table
     * CREATE TABLE devil_fruits (
     *     id BIGSERIAL PRIMARY KEY,
     *     name VARCHAR(100) NOT NULL UNIQUE,
     *     type VARCHAR(50) NOT NULL,
     *     price DECIMAL(10, 2) NOT NULL,
     *     description TEXT,
     *     is_legendary BOOLEAN DEFAULT FALSE,
     *     created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
     *     updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
     *     version BIGINT DEFAULT 0
     * );
     *
     * -- Create indexes for better query performance
     * CREATE INDEX idx_devil_fruits_type ON devil_fruits(type);
     * CREATE INDEX idx_devil_fruits_price ON devil_fruits(price);
     *
     * -- Trades table
     * CREATE TABLE trades (
     *     id BIGSERIAL PRIMARY KEY,
     *     user_id BIGINT NOT NULL REFERENCES users(id),
     *     fruit_id BIGINT NOT NULL REFERENCES devil_fruits(id),
     *     amount DECIMAL(10, 2) NOT NULL,
     *     status VARCHAR(20) NOT NULL,
     *     trade_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
     * );
     *
     * CREATE INDEX idx_trades_user_id ON trades(user_id);
     * CREATE INDEX idx_trades_fruit_id ON trades(fruit_id);
     * CREATE INDEX idx_trades_status ON trades(status);
     *
     * -- Abilities table
     * CREATE TABLE abilities (
     *     id BIGSERIAL PRIMARY KEY,
     *     name VARCHAR(100) NOT NULL UNIQUE,
     *     description TEXT
     * );
     *
     * -- Fruit-Abilities junction table (Many-to-Many)
     * CREATE TABLE fruit_abilities (
     *     fruit_id BIGINT NOT NULL REFERENCES devil_fruits(id),
     *     ability_id BIGINT NOT NULL REFERENCES abilities(id),
     *     PRIMARY KEY (fruit_id, ability_id)
     * );
     *
     * -- User Inventory table (One-to-One)
     * CREATE TABLE user_inventory (
     *     id BIGSERIAL PRIMARY KEY,
     *     user_id BIGINT NOT NULL UNIQUE REFERENCES users(id),
     *     total_fruits INTEGER DEFAULT 0,
     *     total_value DECIMAL(10, 2) DEFAULT 0
     * );
     */
}

/**
 * PERFORMANCE OPTIMIZATION TIPS
 */
class PerformanceOptimization {

    /**
     * 1. N+1 Query Problem and Solution
     *
     * BAD (N+1 queries):
     * List<User> users = userRepository.findAll();
     * for (User user : users) {
     *     List<Trade> trades = user.getTrades(); // Separate query for each user!
     * }
     *
     * GOOD (1 query with JOIN):
     * @Query("SELECT u FROM User u LEFT JOIN FETCH u.trades")
     * List<User> findAllWithTrades();
     */

    /**
     * 2. Pagination for Large Result Sets
     *
     * // Instead of loading all records
     * List<DevilFruit> allFruits = repository.findAll(); // BAD for 1 million records
     *
     * // Use pagination
     * Pageable pageable = PageRequest.of(0, 20); // Page 0, size 20
     * Page<DevilFruit> page = repository.findAll(pageable);
     */

    /**
     * 3. Projection for Specific Fields
     *
     * // Instead of loading entire entity
     * List<DevilFruit> fruits = repository.findAll(); // Loads all columns
     *
     * // Use projection to load only needed fields
     * @Query("SELECT new com.example.FruitNamePrice(f.name, f.price) FROM DevilFruit f")
     * List<FruitNamePrice> findNameAndPrice();
     */

    /**
     * 4. Caching
     *
     * @Cacheable("fruits")
     * public DevilFruit getFruitById(Long id) {
     *     return repository.findById(id);
     * }
     *
     * @CacheEvict(value = "fruits", key = "#id")
     * public void deleteFruit(Long id) {
     *     repository.deleteById(id);
     * }
     */

    /**
     * 5. Batch Operations
     *
     * // Instead of saving one by one
     * for (DevilFruit fruit : fruits) {
     *     repository.save(fruit); // Multiple database calls
     * }
     *
     * // Use batch save
     * repository.saveAll(fruits); // Single batch operation
     */
}

/**
 * DATABASE INTEGRATION DEMO
 */
class DatabaseIntegrationDemo {
    public static void runDemo() {
        System.out.println("\n" + "=".repeat(80));
        System.out.println("TOPIC 8: DATABASE INTEGRATION (JPA/HIBERNATE) DEMO");
        System.out.println("=".repeat(80));

        System.out.println("\n--- JPA Entity Relationships ---");
        System.out.println("1. @OneToOne: User <-> UserInventory");
        System.out.println("2. @OneToMany: DevilFruit -> Trades");
        System.out.println("3. @ManyToOne: Trade -> DevilFruit");
        System.out.println("4. @ManyToMany: DevilFruit <-> Abilities");

        System.out.println("\n--- Spring Data JPA Query Methods ---");
        System.out.println("✓ findByType(String type)");
        System.out.println("✓ findByPriceGreaterThan(Double price)");
        System.out.println("✓ findByNameContaining(String keyword)");
        System.out.println("✓ findByTypeOrderByPriceDesc(String type)");
        System.out.println("✓ findTop5ByOrderByPriceDesc()");

        System.out.println("\n--- Custom JPQL Queries ---");
        System.out.println("@Query(\"SELECT f FROM DevilFruit f WHERE f.type = :type\")");
        System.out.println("@Query(\"SELECT f FROM DevilFruit f JOIN f.abilities a\")");
        System.out.println("@Query(\"SELECT AVG(f.price) FROM DevilFruit f GROUP BY f.type\")");

        System.out.println("\n--- Transaction Management ---");
        System.out.println("@Transactional - Ensures ACID properties");
        System.out.println("  - Atomicity: All or nothing");
        System.out.println("  - Consistency: Valid state transitions");
        System.out.println("  - Isolation: Concurrent transactions don't interfere");
        System.out.println("  - Durability: Committed changes persist");

        System.out.println("\n--- Cloud Database Setup Steps ---");
        System.out.println("1. Choose cloud provider (AWS, Google Cloud, Heroku, Azure)");
        System.out.println("2. Create database instance (PostgreSQL/MySQL)");
        System.out.println("3. Configure security (firewall rules, SSL)");
        System.out.println("4. Get connection details (host, port, database name)");
        System.out.println("5. Update application.properties with connection URL");
        System.out.println("6. Add database driver dependency to pom.xml");
        System.out.println("7. Deploy Spring Boot application");
        System.out.println("8. Hibernate auto-creates tables (ddl-auto=update)");

        System.out.println("\n--- Database Schema Example ---");
        System.out.println("CREATE TABLE devil_fruits (");
        System.out.println("    id BIGSERIAL PRIMARY KEY,");
        System.out.println("    name VARCHAR(100) NOT NULL UNIQUE,");
        System.out.println("    type VARCHAR(50) NOT NULL,");
        System.out.println("    price DECIMAL(10, 2) NOT NULL,");
        System.out.println("    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP");
        System.out.println(");");

        System.out.println("\n--- Performance Optimization ---");
        System.out.println("1. Use JOIN FETCH to avoid N+1 queries");
        System.out.println("2. Implement pagination for large datasets");
        System.out.println("3. Use projections to load only needed fields");
        System.out.println("4. Enable caching for frequently accessed data");
        System.out.println("5. Use batch operations for bulk inserts/updates");
        System.out.println("6. Create indexes on frequently queried columns");
        System.out.println("7. Configure connection pooling (HikariCP)");

        System.out.println("\n--- Production Checklist ---");
        System.out.println("✓ Use environment variables for credentials");
        System.out.println("✓ Enable SSL for database connections");
        System.out.println("✓ Set up automated backups");
        System.out.println("✓ Configure connection pool size");
        System.out.println("✓ Monitor slow queries");
        System.out.println("✓ Use read replicas for scaling");
        System.out.println("✓ Implement proper error handling");
        System.out.println("✓ Set up database monitoring and alerts");

        System.out.println("\n" + "=".repeat(80));
        System.out.println("KEY TAKEAWAYS:");
        System.out.println("1. JPA/Hibernate eliminates manual SQL for CRUD operations");
        System.out.println("2. Entities map Java objects to database tables");
        System.out.println("3. Relationships (@OneToMany, @ManyToOne) handle foreign keys");
        System.out.println("4. Spring Data JPA generates queries from method names");
        System.out.println("5. @Transactional ensures data consistency");
        System.out.println("6. Cloud databases provide persistence and scalability");
        System.out.println("7. Connection pooling is essential for performance");
        System.out.println("8. Always optimize queries and use pagination");
        System.out.println("=".repeat(80));
    }
}

/*
================================================================================
FINAL COMPREHENSIVE DEMO - RUN ALL TOPICS
================================================================================
*/

class ComprehensiveTutorialDemo {
    public static void main(String[] args) {
        System.out.println("\n");
        System.out.println("╔" + "═".repeat(78) + "╗");
        System.out.println("║" + " ".repeat(15) + "JAVA ENTERPRISE DEVELOPMENT TUTORIAL" + " ".repeat(27) + "║");
        System.out.println("║" + " ".repeat(20) + "One Piece Trading Platform" + " ".repeat(32) + "║");
        System.out.println("╚" + "═".repeat(78) + "╝");

        // Run all topic demos
        ExceptionHandlingDemo.runDemo();
        GenericsDemo.runDemo();
        LambdaStreamDemo.runDemo();
        MultithreadingDemo.runDemo();
        FileIODemo.runDemo();
        DesignPatternsDemo.runDemo();
        SpringFrameworkDemo.runDemo();
        DatabaseIntegrationDemo.runDemo();

        // Final Summary
        System.out.println("\n");
        System.out.println("╔" + "═".repeat(78) + "╗");
        System.out.println("║" + " ".repeat(30) + "TUTORIAL COMPLETE!" + " ".repeat(29) + "║");
        System.out.println("╚" + "═".repeat(78) + "╝");

        System.out.println("\n🎓 CONGRATULATIONS! You've completed all 8 advanced Java topics!");
        System.out.println("\n📚 Topics Covered:");
        System.out.println("   1. ✅ Exception Handling - Custom exceptions, try-catch, retry logic");
        System.out.println("   2. ✅ Generics - Type safety, wildcards, generic classes");
        System.out.println("   3. ✅ Lambda & Streams - Functional programming, data processing");
        System.out.println("   4. ✅ Multithreading - Concurrency, ExecutorService, CompletableFuture");
        System.out.println("   5. ✅ File I/O - Reading/writing files, serialization");
        System.out.println("   6. ✅ Design Patterns - Singleton, Factory, Strategy, Observer, etc.");
        System.out.println("   7. ✅ Spring Framework - REST APIs, Dependency Injection, layered architecture");
        System.out.println("   8. ✅ Database Integration - JPA/Hibernate, cloud databases, transactions");

        System.out.println("\n🚀 Next Steps:");
        System.out.println("   1. Build a complete Spring Boot application");
        System.out.println("   2. Deploy to cloud (Heroku, AWS, Google Cloud)");
        System.out.println("   3. Connect to PostgreSQL or MySQL database");
        System.out.println("   4. Implement authentication with Spring Security");
        System.out.println("   5. Add unit tests with JUnit and Mockito");
        System.out.println("   6. Create a React or Angular frontend");
        System.out.println("   7. Implement CI/CD pipeline");
        System.out.println("   8. Learn microservices with Spring Cloud");

        System.out.println("\n💼 Enterprise Skills Acquired:");
        System.out.println("   ✓ Production-ready error handling");
        System.out.println("   ✓ Type-safe generic programming");
        System.out.println("   ✓ Functional programming with streams");
        System.out.println("   ✓ Concurrent and asynchronous programming");
        System.out.println("   ✓ File operations and data persistence");
        System.out.println("   ✓ Industry-standard design patterns");
        System.out.println("   ✓ RESTful API development with Spring Boot");
        System.out.println("   ✓ Database integration with JPA/Hibernate");
        System.out.println("   ✓ Cloud database connectivity");

        System.out.println("\n🌟 You're now ready for enterprise Java development!");
        System.out.println("   These are the exact skills used at companies like:");
        System.out.println("   - Google, Amazon, Microsoft, Netflix");
        System.out.println("   - Banks and financial institutions");
        System.out.println("   - E-commerce platforms");
        System.out.println("   - SaaS companies");

        System.out.println("\n📖 Keep Learning:");
        System.out.println("   - Spring Security for authentication/authorization");
        System.out.println("   - Spring Cloud for microservices");
        System.out.println("   - Docker and Kubernetes for containerization");
        System.out.println("   - Apache Kafka for event streaming");
        System.out.println("   - Redis for caching");
        System.out.println("   - Elasticsearch for search");

        System.out.println("\n" + "=".repeat(80));
        System.out.println("Happy Coding! 🎉");
        System.out.println("=".repeat(80) + "\n");
    }
}
