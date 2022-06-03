package Lab1;

import java.util.ArrayList;
import java.util.Scanner;

public class FCFS {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String processStr;
        String burstTimeStr;

        //deciding the number of processes, input with the number of processes with ','
	  //ex: p1,p2,p3,p4 & 34,22,33,12
        processStr = sc.next();
        burstTimeStr = sc.next();
        int size = 1;
        for (int i = 0; i < processStr.length(); i++) {
            if (processStr.charAt(i) == ',') {
                size++;
            }
        }

        //turns burst input into int array
        String[] processArrayStr = new String[size];
        String[] burstTimeArrayStr = new String[size];
        int[] burstTimeArrayInt = new int[size];
        processArrayStr = processStr.split(",");
        burstTimeArrayStr = burstTimeStr.split(",");
        for (int i = 0; i < size; i++) {
            burstTimeArrayInt[i] = Integer.parseInt(burstTimeArrayStr[i]);
        }

        //output
        int[] waitingTime = new int[size];
        int[] turnAround = new int[size];

        waitingTime = getWaiting(burstTimeArrayInt, size);
        turnAround = getTurnAround(burstTimeArrayInt, size);
        System.out.println("Output:\nProcesses\tBurst\tWaiting\tTurn Around");
        for (int i = 0; i < size; i++) {
            System.out.println(processArrayStr[i] + "\t\t" + burstTimeArrayInt[i] + "\t" + waitingTime[i] + "\t" + turnAround[i]);
        }

        System.out.println("Average Waiting Time = " + getWaitingAvg(waitingTime) + "\nAverage Turn Around Time: " + getTurnAroundAvg(turnAround));

    }
    //Turnaround Time = completion of a process – submission of a process
    //Waiting Time = turnaround time – burst time

    //Waiting Time method
    public static int[] getWaiting(int[] burstTimeArrayInt, int size) {
        int[] waitingTime = new int[size];
        int waitingValue = 0;
        waitingTime[0] = 0;
        for (int i = 1; i < size; i++) {
            waitingValue += burstTimeArrayInt[i - 1];
            waitingTime[i] = waitingValue;
        }
        return waitingTime;
    }

    public static double getWaitingAvg(int[] waitingTime) {
        double sum = 0, avg;
        for (int i = 0; i < waitingTime.length; i++) {
            sum += waitingTime[i];
        }
        avg = sum / waitingTime.length;
        return avg;
    }

    //Turn Around method
    public static int[] getTurnAround(int[] burstTimeArrayInt, int size) {
        int[] turnAround = new int[size];
        int turnAroundValue = 0;
        for (int i = 0; i < size; i++) {
            turnAroundValue += burstTimeArrayInt[i];
            turnAround[i] += turnAroundValue;
        }
        return turnAround;
    }

    public static double getTurnAroundAvg(int[] turnAround) {
        double sum = 0, avg;
        for (int i = 0; i < turnAround.length; i++) {
            sum += turnAround[i];
        }
        avg = sum / turnAround.length;
        return avg;
    }
}
