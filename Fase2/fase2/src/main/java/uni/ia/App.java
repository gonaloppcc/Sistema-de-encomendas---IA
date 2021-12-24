package uni.ia;

import org.jpl7.Atom;
import org.jpl7.JPL;
import org.jpl7.Variable;

/**
 * Hello world!
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        Atom jose = new Atom("jose");

        Variable v = new Variable("X");
        JPL.init(args);

        for(String s : JPL.getActualInitArgs())
            System.out.println(s);


        System.out.println(v.name);
        System.out.println(jose.name());
        
    }
}
