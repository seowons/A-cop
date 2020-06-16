package com.github.dudgns0507.keras;

public class Data {
    private int id;
    private String name;
    private int drawable;
    private int thumbnail;

    public Data(int id, String name, int drawable, int thumbnail) {
        this.id = id;
        this.name = name;
        this.drawable = drawable;
        this.thumbnail = thumbnail;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getDrawable() {
        return drawable;
    }

    public void setDrawable(int drawable) {
        this.drawable = drawable;
    }

    public int getThumbnail() {
        return thumbnail;
    }

    public void setThumbnail(int thumbnail) {
        this.thumbnail = thumbnail;
    }
}
