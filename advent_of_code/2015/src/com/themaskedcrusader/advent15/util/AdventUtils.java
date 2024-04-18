package com.themaskedcrusader.advent15.util;

import java.io.*;
import java.util.ArrayList;

public class AdventUtils {

    private BufferedReader getFileHandle(File directory, String problem) throws IOException {
        File input = new File(directory.getAbsolutePath() + File.separator + problem.concat(".txt"));
        BufferedReader in = new BufferedReader(new FileReader(input));
        return in;
    }

    private void commonExceptionCatch(Exception e) {
        System.err.println("Could not read from file, Cannot Continue");
        e.printStackTrace();
        System.exit(Constants.FILE_READ_ERROR);
    }

    public String get_first_line(File directory, String problem) {
        String ret = "";
        try {
            BufferedReader input = getFileHandle(directory, problem);
            ret = input.readLine();
            input.close();

        } catch (IOException e) {
            commonExceptionCatch(e);
        }
        return ret;
    }

    public ArrayList<String> getInputArray(File directory, String problem) {
        ArrayList<String> ret = new ArrayList<>();
        try {
            BufferedReader input = getFileHandle(directory, problem);
            String line;
            while ((line = input.readLine()) != null) {
                ret.add(line);
            }
            input.close();
        } catch (IOException e) {
            commonExceptionCatch(e);
        }
        return ret;
    }
}
