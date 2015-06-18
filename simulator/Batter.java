/*
 * Stores data for a specific batter 
 * Created by Keith Gladstone, 2015
 */
public class Batter {
    private double battingAVG;
    private String name;
    private int seasonAB;
    private int seasonHits;
    private int season1B;
    private int season2B;
    private int season3B;
    private int seasonHR;
    private boolean hittingStats;
    
    public Batter(String name, Double battingAVG)
    {
        this.battingAVG = battingAVG;
        this.name = name;
        this.hittingStats = false;
    }
    
    /*
     * If available, set hitting stats accordingly
     */
    public void setHittingStats(int seasonAB, int seasonHits, int season2B, int season3B, int seasonHR)
    {
        this.hittingStats = true;
        this.seasonAB = seasonAB;
        this.seasonHits = seasonHits;
        
        this.battingAVG = ((double) seasonHits) / seasonAB; // recalculate batting AVG
        this.season1B = seasonHits - season2B - season3B - seasonHR;
        this.season2B = season2B;
        this.season3B = season3B;
        
        this.seasonHR = seasonHR;
    }
    
    public int seasonHits()
    {
        return seasonHits;
    }
    
    public int season1B()
    {
        return season1B;
    }
    
    public int season2B()
    {
        return season2B;
    }
    
    public int season3B()
    {
        return season3B;
    }
    
    public int seasonHR()
    {
        return seasonHR;
    }
    
    public double AVG()
    {
        return battingAVG;
    }
    
    public String name()
    {
        return name;
    }
    
    public boolean hasHittingStats()
    {
        return hittingStats;
    }
    
    public String toString()
    {
        String result = name();
        for (int j = name.length(); j < 25; j++)
            result += " ";
        return result + roundAVG();
    }
    
    /*
     * Properly round batting avg to three decimal places
     */
    public String roundAVG()
    {
        int intAVG = (int) (battingAVG * 1000);
        String roundAVG =  "" + (((double) intAVG) / 1000);
        int length = roundAVG.length();
        for (int i = 5; i > length; i--)
        {
            roundAVG += "0";
        }
        return roundAVG;
    }
    
    public String hittingSplits()
    {
        return "1B: " + season1B + " | 2B: " + season2B + " | 3B: " + season3B + " | HR: " + seasonHR;
    }
    
}