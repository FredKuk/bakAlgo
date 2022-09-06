
public class test {
    public interface Ibattery {

        String toString();

    }
    public static class Battery {

        private Ibattery ibattery;

        public Battery(Ibattery ibattery) {

            this.ibattery = ibattery;

        }

        @Override
        public String toString() {

            return ibattery.toString();

        }

    }

    public static class A implements Ibattery {
        @Override

        public String toString() {

            return "a BATTERY";

        }

    }

    public static class B implements Ibattery {

        @Override

        public String toString() {

            return "b BATTERY";

        }

    }

    public static void main(String args[]) {

        Battery a = new Battery(new A());
        System.out.println(a.toString());
        Battery b = new Battery(new B());
        System.out.println(b.toString());
    }
}
