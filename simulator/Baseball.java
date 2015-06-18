/*
 * Baseball game simulation 
 * Given player data from .csv files
 * this program simulates a baseball game
 * via probability theory
 * 
 * Future features:
 * More advanced data: hitting splits for outs, baserunners
 * Incorporate pitching and defense
 * 
 * Created by Keith Gladstone, 2015
 * 
 */
public class Baseball
{
    private static int[] bases;
    private static int inningOuts;
    private static int inningHits;
    private static int inningRuns;

    public static void main(String[] args)
    {
        StdOut.println("***********************Welcome to the MLB Simulation Game***********************");
        StdOut.println("Using real probability simulations based on player stats...\n");
        
        //BattingOrder Mets = new BattingOrder("mets.csv", "New York Mets", 9);
        //BattingOrder Phillies = new BattingOrder("phillies.csv", "Philadelphia Phillies", 9);
        BattingOrder NL = new BattingOrder("nl.csv", "National League", 9);
        BattingOrder AL = new BattingOrder("al.csv", "American League", 9);
        
        
        StdOut.println("Introducing the");
        StdOut.println(NL);
        StdOut.println("****************");
        StdOut.println("Introducing the");
        StdOut.println(AL);
        StdOut.println("****************");
        
        // Simulate Game
        bases = new int[3];
        inningOuts = 0;
        inningRuns = 0;
        inningHits = 0;
        for (int k = 1; k <= 9; k++) // Can adjust number of innings
        {
            simInning(NL, k);
            simInning(AL, k);
        }
        
      
        StdOut.println("Game Summary:");
        StdOut.println(scoreToString(NL));
        StdOut.println(scoreToString(AL));
        
    }
    
    
    /**************************************************************************/
    
    /*
     * Simulate an inning for a team
     */
    private static void simInning(BattingOrder team, int inning)
    {
        StdOut.println("Inning No. " + inning + " for " + team.teamName());
        while (inningOuts < 3)
            simAtBat(team);
        
        // Inning Over
        StdOut.println("Inning Summary: " + inningRuns
                           + " runs\t " + inningHits + " hits");
        bases = new int[3]; // clear bases
        inningOuts = 0; // clear outs
        inningHits = 0;
        inningRuns = 0;
        StdOut.println("****************");
    }
    
    /*
     * Simulate a turn at-bat for a player
     */
    private static void simAtBat(BattingOrder team)
    {
        Batter batter = team.batterAtBat();
        StdOut.println(batter.name() + " comes up to the plate");
        if (batter.hasHittingStats())
            StdOut.println(batter.name() + " has hitting stats: " + batter.statLine());
        boolean hit = hit(batter);
        
        if (hit == true) {
            inningHits++;
            team.addHits(1);
            int TB = simTotalBases(batter);
            StdOut.println("Hit: " + hitType(TB));
            printBaseHit(TB);
            // Advance runners according to force only
            advanceRunners(team, TB); 
        }
        else {
            StdOut.println(batter.name() + " is out!");
            inningOuts++; }
            
        StdOut.println(basesToString());
    }
    
    /*
     * Return hit type via symbol table
     */
    private static String hitType(int i)
    {
        String[] hits = {"Single", "Double", "Triple", "Home-Run"};
        return hits[i - 1];
    }
    
    /*
     * Assuming a hit, return which kind {1, 2, 3, 4}
     */
    private static int simTotalBases(Batter batter)
    {
        if (batter.hasHittingStats())
        {
            int singleThreshold = batter.season1B(); 
            int doubleThreshold = singleThreshold + batter.season2B();
            int tripleThreshold = doubleThreshold + batter.season3B();
            
            int random = StdRandom.uniform(batter.seasonHits());
            
            if (random < singleThreshold)
                return 1;
            if (random < doubleThreshold)
                return 2;
            if (random < tripleThreshold)
                return 3;
            else
                return 4;
        }
        else
            return StdRandom.uniform(4) + 1;
    }
        
    /*
     * Advances the runners on base by TB
     */
    private static void advanceRunners(BattingOrder team, int TB)
    {
        int binaryBases = bases[0] + bases[1] * 2 + bases[2] * 4; // Map bases array to binary number
        int RBI = 0;
        
        // First shift
        binaryBases *= 2;
        if (binaryBases > 7)
            {
                team.addRuns(1);
                RBI++;
            }
        binaryBases += 1; // Add current runner
        binaryBases %= 8;


        // Following shifts (do in for-loop)
        for (int j = 0; j < TB - 1; j++)
        {
            binaryBases *= 2;
            if (binaryBases > 7)
            {
                team.addRuns(1);
                RBI++;
            }   
            binaryBases %= 8;
        }
        
        // Convert back to bases array
        for (int i = 2; i >= 0; i--) {
            if ((binaryBases & (1 << i)) != 0)
                bases[i] = 1;
            else
                bases[i] = 0;
        }
        
        // Print RBI if any
        if (RBI > 0)
            StdOut.println(RBI + " RBI");
    }
    
    /*
     * Call hit() method on batter's average
     */
    private static boolean hit(Batter batter)
    {
        return hit(batter.AVG());
    }
    
    /*
     * Simulate a Bernoulli Variable w.p battingAVG
     */
    private static boolean hit(double battingAVG)
    {
        int random = StdRandom.uniform(1000);
        if (random < battingAVG * 1000)
            return true;
        else
            return false;

    }
    
    private static String basesToString()
    {
        String result = "";
        if (bases[0] == 1)
            result += "Runner on first\n";
        if (bases[1] == 1)
            result += "Runner on second\n";
        if (bases[2] == 1)
            result += "Runner on third\n";
        result += inningOuts + " Out\n";
        return result; 
    }
    
    private static String scoreToString(BattingOrder team)
    {
        return team.teamName() + ": " + team.getRuns() + " runs\t " + team.getHits() + " hits";
    }
    
    private static void printBaseHit(int TB)
    {
        if (TB == 1)
            StdOut.println(
                               " ***    ******\n" +
                               "****    **   **\n" +
                               " ***    *****\n" +
                               " ***    **   **\n" +
                               " ***    ******\n");
        if (TB == 2)
            StdOut.println(
                               " ******     ******\n" +
                               "**    **    **   **\n" +
                               "    ***     *****\n" +
                               "   ***      **   **\n" +
                               "********    ******\n");
        if (TB == 3)
            StdOut.println(
                               " ******    ******\n" +
                               "**    **   **   **\n" +
                               "    ***    *****\n" +
                               "**    **   **   **\n" +
                               " ******    ******\n");
        if (TB == 4)
            StdOut.println(
                               "**    **    ******\n" +
                               "**    **    **   **\n" +
                               "********    *****\n" +
                               "**    **    **   **\n" +
                               "**    **    **   **\n");
                               
    }
}